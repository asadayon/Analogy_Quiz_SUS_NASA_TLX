import streamlit as st
import random
import matplotlib.pyplot as plt
from supabase import create_client
from quiz import load_questions
from quiz import load_survey
import time

SUPABASE_URL = st.secrets["SUP_URL"]
SUPABASE_KEY = st.secrets["SUP_KEY"]

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

def store_answer(question_number, selected_option):
    st.session_state.answers[question_number] = selected_option 

def store_survey_answer(question_number, selected_option):
    st.session_state.post_quiz_answers[question_number] = selected_option 
    
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
    username = st.text_input("Enter your name")


    if st.button("Start Quiz"):
        st.session_state.page = "quiz"
        st.session_state["student_name"] = student_name
        st.session_state["username"] = username.strip()
        st.session_state["quiz_start_time"] = time.time()
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
        if not is_correct:
            st.markdown(f"<span style='color:gray;'><b>Correct answer:</b> {correct}</span>", unsafe_allow_html=True)


    if st.button("Go To Survey"):
        st.session_state.page = "post_quiz"
        st.rerun()

if st.session_state.page == "post_quiz":
    username = st.session_state.get("username", "anonymous")
    st.markdown("### Post Quiz Survey")
    st.markdown("---")

    st.write(f"Hello, {username}")
    opts = list(range(1,8))
    likert_labels = {
        1: "Strongly Disagree",
        2: "Disagree",
        3: "Somewhat Disagree",
        4: "Neutral",
        5: "Somewhat Agree",
        6: "Agree",
        7: "Strongly Agree"
    }
    if opts[-1] == 5:
        likert_labels = {
            1: "Strongly Disagree",
            2: "Disagree",
            3: "Neutral",
            4: "Agree",
            5: "Strongly Agree"
        }

        
    st.write("#### 📝 Please complete the following survey")
    st.markdown(
      """This survey helps us understand how well the system’s explanations supported your understanding of the advisor recommendation process and your trust in its recommendations. Your feedback will help us improve the clarity and usefulness of the explanations for future users, whether delivered through static text or an interactive interface."""

    )
    
    st.write("---")
    if "post_quiz_questions" not in st.session_state:        
        post_quiz_questions = load_survey()

        st.session_state.post_quiz_questions = post_quiz_questions
        st.session_state.post_quiz_answers = {}
        
    for idx,q in enumerate (st.session_state.post_quiz_questions):

        question = q
        qid = idx+1
        
        st.markdown(f"**Q{idx+1}. {question}**")
        col1,col2,col3 = st.columns([2.5, 6, 2])
        with col1:
            st.markdown("""
            <div style='display:flex; align-items:center; height:100%; padding-top:0.5rem'>
                Strongly Disagree
            </div>
            """, unsafe_allow_html=True)
        with col2:
            st.radio(
                label=f"Q{idx+1}. {question}",
                label_visibility = "collapsed",
                options=opts,
                index=None,
                key=f"pq_{qid}",
                horizontal = True
            )
        with col3:
            st.markdown("""
            <div style='display:flex; align-items:center; height:100%; padding-top:0.5rem'>
                Strongly Agree
            </div>
            """, unsafe_allow_html=True)
        st.markdown("")
    if st.button("Submit"):
        unanswered =  len([ k for k, v in st.session_state.items() if k.startswith("pq_") and v is None])

        if unanswered:
            st.error("Please answer all questions before submitting.")
        else:
            for i in range(1,len(st.session_state.post_quiz_questions)+1):
                    key=f"pq_{i}"
                    store_answer(i, st.session_state[key])
            st.session_state["survey_submitted"] = True
            st.session_state.page = "post_quiz_submission"
            st.rerun()

if st.session_state.page == "post_quiz_submission":
    st.title("Thank you!")





        

