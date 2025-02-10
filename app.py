import os
import streamlit as st
from dotenv import load_dotenv
from resume_parser import parse_resume
from career_model import CareerPathRecommender

# Load environment variables
load_dotenv()

# Streamlit app
st.title("Career Path Recommendation System")

st.sidebar.header("Upload Your Resume")
uploaded_file = st.sidebar.file_uploader("Choose a PDF file", type=["pdf"])

if uploaded_file:
    st.write("**Uploaded File:**", uploaded_file.name)
    
    try:
        # Parse the resume
        st.write("Parsing the resume...")
        resume_data = parse_resume(uploaded_file)
        st.success("Resume parsed successfully!")
        
        # Initialize the recommender
        recommender = CareerPathRecommender()

        # Get recommendations
        st.write("Generating career path recommendations...")
        career_paths = recommender.get_recommendations(resume_data)
        
        if isinstance(career_paths, str):
            st.success("Recommendations:")
            st.write(career_paths)
        else:
            st.error("No recommendations available.")
    except Exception as e:
        st.error(f"An error occurred: {e}")
else:
    st.info("Please upload a PDF resume to get career path recommendations.")
