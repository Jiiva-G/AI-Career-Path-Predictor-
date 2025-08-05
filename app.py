import streamlit as st 
from skill_predictor import predict_career
from recommender import recommend_courses
from gpt_interview import generate_mock_questions

st.title("Personal AI Career Path Predictor")

skills = st.text_area("Enter your skills (comma separated):")
if st.button("Predict Career Path"):
    career = predict_career(skills)
    st.success(f"🎯 Predicted Career Path: {career}")
    
    st.markdown("### 📚 Recommended Learning Path")
    for course in recommend_courses(career):
        st.write(f"- {course}")
    
    st.markdown("### 🤖 Possible Mock Interview Questions")
    st.write(generate_mock_questions(career))
