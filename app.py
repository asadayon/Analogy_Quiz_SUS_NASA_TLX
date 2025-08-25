import streamlit as st
import random
import matplotlib.pyplot as plt
from supabase import create_client
from quiz import load_questions
import time

SUPABASE_URL = st.secrets["SUP_URL"]
SUPABASE_KEY = st.secrets["SUP_KEY"]

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)


 def update_answer(question_number, selected_option):
    st.session_state.answers[question_number] = selected_option 




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
            st.write(f"Q{i+1}: {question['question']}")
            q_num=question['question_number']
            st.markdown(f"**Q{question['question_number']}. {question['question']}**")
            user_answer = st.radio(
                "Choose your answer:",
                question["options"],
                key=f"q{q_num}"
                index=st.session_state.answers[q_num] if q_num in st.session_state.answers else None,
                on_change=update_answer,   # Trigger function
                args=(q_num, st.session_state.get(f"q{q_num}"))
            )
            
 
