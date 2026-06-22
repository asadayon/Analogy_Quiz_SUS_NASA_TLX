import streamlit as st
import random
import matplotlib.pyplot as plt
from supabase import create_client
from quiz import load_questions
from quiz import load_survey
import time
from datetime import datetime, timezone

SUPABASE_URL = st.secrets["SUP_URL"]
SUPABASE_KEY = st.secrets["SUP_KEY"]

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

def store_answer(question_number, selected_option):
    st.session_state.answers[question_number] = selected_option

    
def update_quiz_database(question_number, text, selected_option, correct, is_correct):
     if not st.session_state["quiz_database"]:    
        resp = (
                supabase.table("quiz_response")
                .insert({
                    "username": st.session_state["username"] ,
                    "scenario": st.session_state["student_name"],
                    "question_id": question_number,
                    "user_answer": selected_option,
                    "is_correct":is_correct,
                    "question_text": text,
                    "correct_answer": correct
                })
                .execute()
            )
def update_quiz_result():
    if st.session_state["quiz_result"]>0:
            now_utc = datetime.now(timezone.utc).isoformat()
            response = (
                supabase.table("quiz_user")
                .update({"quiz_end_time": now_utc,
                         "total_score": st.session_state["quiz_result"]})
                .eq("username", st.session_state["username"])
                .eq("scenario", st.session_state["student_name"])
                .execute()
            )
            st.session_state["quiz_result"]=0
                    
    

def update_survey_database(question_number, selected_option,text):
     if not st.session_state["survey_submitted"]:    
        resp = (
                supabase.table("survey_response")
                .insert({
                    "username": st.session_state["username"] ,
                    "scenario": st.session_state["student_name"],
                    "version":  st.session_state["version"],
                    "question_id": question_number,
                    "question_text": text,
                    "user_response": selected_option
                })
                .execute()
            )
        

def store_survey_answer(question_number, selected_option):
    st.session_state.post_quiz_answers[question_number] = selected_option 


def add_user():
    """
    Start a new session for a given user and scenario.
    Inserts a row into the 'session' table.
    Returns the new session info (including generated session_id).
    """
   
    resp = (
            supabase.table("quiz_user")
            .insert({
                "username": st.session_state["username"] ,
                "scenario": st.session_state["student_name"],
                "version":  st.session_state["version"] 
            })
            .execute()
        )
 


def reset():
    for key in list(st.session_state.keys()):
        if key.startswith("q_"):   # only reset quiz-related keys
            del st.session_state[key]

st.session_state.submitted=False


# Run the quiz
if "page" not in st.session_state:
    st.session_state.page = "home"

if st.session_state.page == "home":
    st.title("Student Advisor Recommender System Quiz")
    user_names=['Emily Zhang', 'Amina Rahman','David Chen', 'Sara Lee']
    student_name = st.selectbox("Select a student scenario", user_names)
    version = st.selectbox("Select a student scenario", ["v1","v2"])
    username = st.text_input("Enter your name")


    if st.button("Start Quiz"):
        st.session_state.page = "quiz"
        st.session_state["student_name"] = student_name
        st.session_state["username"] = username.strip()
        st.session_state["version"] = version
        st.session_state["quiz_start_time"] = time.time()
        st.session_state["quiz_database"]=False
        st.session_state["survey_submitted"] = False
        st.session_state["quiz_result"]=0
        add_user()
        st.rerun()


if st.session_state.page == "quiz":
    if "quiz_questions" not in st.session_state:
        questions=load_questions(st.session_state.student_name)
        st.session_state.quiz_questions = questions
    if "answers" not in st.session_state:
        st.session_state.answers = {}

    if not st.session_state["submitted"]:
        st.title("Student Advisor Recommender System Quiz")
        st.markdown(f"**User:** {st.session_state['username']}")
        st.write("---")
        user_answers = []
        correct_count = 0
    
        for i, question in enumerate(st.session_state.quiz_questions):
            q_num=question['question_number']
            st.markdown(f"**Q{question['question_number']}. {question['question']}**")
            user_answer = st.radio(
                "Choose your answer:",
                question["options"],
                key=f"q_{q_num}",
                index= None
            )
            st.markdown("")

        st.write("---")

        num_answered = len([ k for k, v in st.session_state.items() if k.startswith("q_") and v is not None])
        total_qs = len(st.session_state["quiz_questions"])
        st.info(f"**{num_answered} out of {total_qs}** questions answered.")
        
        if st.button("Submit"):
            for i in range(1,21):
                key=f"q_{i}"
                store_answer(i, st.session_state[key])
                
            st.session_state["submitted"] = True
            st.session_state.page = "quiz_submission"
            st.rerun()
            
if st.session_state.page == "quiz_submission":
    username = st.session_state.get("username", "anonymous")
    answers = st.session_state["answers"]
    questions = st.session_state["quiz_questions"]
    # Compute score
    # Score
    num_correct = 0
    
    for q in questions:
        qid = q["question_number"]
        selected = answers.get(qid)
        if selected is None:
            continue

        # Get the original index of selected option
        correct = q["answer"]

        # Check if this original index matches correct_index
        if selected == correct:
            num_correct += 1
        update_quiz_database(qid, q["question"],selected, correct, selected == correct)
    st.session_state["quiz_result"]=num_correct
    update_quiz_result()
    st.session_state["quiz_database"]=True
    
    st.success(f"Thanks, **{username}**! You answered **{num_correct}** questions correctly.")

    st.write("---")
    # Show per-question feedback
    # Show per-question feedback
    for idx, q in enumerate(questions):
        qid = q["question_number"]
        prompt = q["question"]
        chosen = answers.get(qid)
        
        st.markdown(f"**Q{idx + 1}. {prompt}**")

        if chosen is None:
            st.markdown("<span style='color:gray;'>No answer selected.</span>", unsafe_allow_html=True)
            st.markdown(f"<span style='color:gray;'><b>Correct answer:</b> {correct}</span>", unsafe_allow_html=True)
            continue

        correct = q["answer"]
        is_correct = chosen == correct

        color = "green" if is_correct else "red"
        status = "Correct" if is_correct else "Incorrect"
       

        st.markdown(
            f"<span style='color:{color};'><b>Your answer:</b> {chosen}</span><br>"
            f"<span style='color:{color};'><i>{status}</i></span>",
            unsafe_allow_html=True
        )
        

    if st.button("Go To Survey"):
        st.session_state.page = "post_quiz"
        st.rerun()

if st.session_state.page == "post_quiz":
    username = st.session_state.get("username", "anonymous")

    st.markdown("### Post-Quiz Survey")
    st.markdown("---")
    st.write(f"Hello, {username}")

    st.write("#### 📝 Please complete the following survey")
    st.markdown(
        """
        This survey helps us understand the usability of this version of the advisor recommender system
        and the workload required to understand its explanations and complete the task.
        """
    )

    st.write("---")

    # -------------------------
    # Load SUS and NASA-TLX only
    # -------------------------
    if "post_quiz_questions" not in st.session_state:
        st.session_state.post_quiz_questions = {
            "sus": load_sus(),
            "nasa_tlx": load_nasa_tlx()
        }

    # -------------------------
    # SUS: 5-point Likert scale
    # -------------------------
    sus_opts = list(range(1, 6))

    st.markdown("### System Usability Scale (SUS)")
    st.caption("Scale: 1 = Strongly Disagree, 5 = Strongly Agree")

    for item in st.session_state.post_quiz_questions["sus"]:
        qid = item["id"]
        question = item["question"]

        st.markdown(f"**{qid}. {question}**")

        col1, col2, col3 = st.columns([2.5, 6, 2])

        with col1:
            st.markdown(
                """
                <div style='display:flex; align-items:center; height:100%; padding-top:0.5rem'>
                    Strongly Disagree
                </div>
                """,
                unsafe_allow_html=True
            )

        with col2:
            st.radio(
                label=f"{qid}. {question}",
                label_visibility="collapsed",
                options=sus_opts,
                index=None,
                key=f"pq_{qid}",
                horizontal=True
            )

        with col3:
            st.markdown(
                """
                <div style='display:flex; align-items:center; height:100%; padding-top:0.5rem'>
                    Strongly Agree
                </div>
                """,
                unsafe_allow_html=True
            )

        st.markdown("")

    st.write("---")

    # -------------------------
    # NASA-TLX: 1–7 scale
    # -------------------------
    nasa_opts = list(range(1, 8))

    st.markdown("### NASA-TLX Workload Survey")
    st.caption("Scale: 1 = Very Low, 7 = Very High")

    for item in st.session_state.post_quiz_questions["nasa_tlx"]:
        qid = item["id"]
        dimension = item["dimension"]
        question = item["question"]

        st.markdown(f"**{qid}. {dimension}: {question}**")

        col1, col2, col3 = st.columns([2.5, 6, 2])

        with col1:
            st.markdown(
                """
                <div style='display:flex; align-items:center; height:100%; padding-top:0.5rem'>
                    Very Low
                </div>
                """,
                unsafe_allow_html=True
            )

        with col2:
            st.radio(
                label=f"{qid}. {question}",
                label_visibility="collapsed",
                options=nasa_opts,
                index=None,
                key=f"pq_{qid}",
                horizontal=True
            )

        with col3:
            st.markdown(
                """
                <div style='display:flex; align-items:center; height:100%; padding-top:0.5rem'>
                    Very High
                </div>
                """,
                unsafe_allow_html=True
            )

        st.markdown("")

    # -------------------------
    # Submit
    # -------------------------
    if st.button("Submit"):
        survey_items = (
            st.session_state.post_quiz_questions["sus"]
            + st.session_state.post_quiz_questions["nasa_tlx"]
        )

        unanswered = [
            item["id"]
            for item in survey_items
            if st.session_state.get(f"pq_{item['id']}") is None
        ]

        if unanswered:
            st.error("Please answer all questions before submitting.")
        else:
            for item in survey_items:
                qid = item["id"]
                answer = st.session_state[f"pq_{qid}"]

                if qid.startswith("SUS"):
                    question_text = item["question"]
                    survey_type = "SUS"
                    dimension = None

                elif qid.startswith("NTLX"):
                    question_text = item["question"]
                    survey_type = "NASA-TLX"
                    dimension = item["dimension"]

                # Option 1: store only question id and answer
                store_survey_answer(qid, answer)

                # Option 2: store full survey metadata
                update_survey_database(
                    qid,
                    answer,
                    question_text,
                    survey_type=survey_type,
                    dimension=dimension
                )

            st.session_state["survey_submitted"] = True
            st.session_state.page = "post_quiz_submission"
            st.rerun()


if st.session_state.page == "post_quiz_submission":
    st.title("Thank you!")





        


