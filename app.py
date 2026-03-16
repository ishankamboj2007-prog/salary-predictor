import os
import gdown
import joblib

MODEL_PATH = "salary_pipeline.joblib"
FILE_ID = "1S3qzL8xvFRuO9JKza24LgF9BnjzGrrXo"

if not os.path.exists(MODEL_PATH):
    url = f"https://drive.google.com/uc?id={FILE_ID}"
    gdown.download(url, MODEL_PATH, quiet=False)

model = joblib.load(MODEL_PATH)






import streamlit as st
import joblib
import pandas as pd
from insights import get_salary_vs_exp, get_salary_vs_edu, get_skill_suggestions, get_market_positioning, get_career_growth

# Load the pipeline
pipeline = joblib.load('salary_pipeline.joblib')

# Predefined options
exp_ranges = ["0–1", "1–3", "3–5", "5–8", "8–12", "12+"]
educations = ["Diploma", "Bachelor", "Master", "PhD"]
genders = ["Male", "Female", "Non-binary", "Prefer not to say"]
job_titles = ["Software Engineer", "Data Scientist", "Product Manager", "Business Analyst", "DevOps Engineer", "UX Designer", "Marketing Specialist", "HR Manager", "Sales Executive", "Consultant"]
cities = ["Mumbai", "Delhi", "Bangalore", "Hyderabad", "Chennai", "Pune", "Kolkata", "Ahmedabad", "Jaipur", "Surat"]
industries = ["Technology", "Finance", "Healthcare", "Education", "Manufacturing", "Retail", "Consulting", "Media", "Energy", "Real Estate"]
skills_list = ["Python", "Java", "Machine Learning", "Data Analysis", "SQL", "Cloud Computing", "Project Management", "UI/UX Design", "Marketing", "Leadership"]

# Custom CSS for attractiveness
# Custom CSS for attractiveness (updated for better contrast and readability)
st.markdown("""
    <style>
    section[data-testid="stAppViewContainer"]   /* Changed to white for clear text visibility */
    .stButton>button {background-color: #4CAF50; color: white; border-radius: 10px;}
    .stSelectbox, .stMultiselect {border-radius: 5px;}
    h1, h2, h3 {color: #2E86AB;}  /* Kept blue for headers; adjust if needed */
    section[data-testid="stSidebar"]   /* Light blue for sidebar */
     /* Ensures body text is dark for contrast on white background */
    </style>
""", unsafe_allow_html=True)

st.title("💼 Salary Prediction App")
st.markdown("### Predict Your Annual Salary in INR & Unlock Career Insights! 🚀")
st.write("Enter your details below to get a personalized salary estimate and actionable advice.")

# Sidebar for inputs
with st.sidebar:
    st.header("📝 Your Details")
    exp_range = st.selectbox("Experience Range", exp_ranges, help="Years of professional experience.")
    education = st.selectbox("Education Level", educations, help="Highest qualification.")
    gender = st.selectbox("Gender", genders, help="For inclusive insights.")
    job_title = st.selectbox("Job Title", job_titles, help="Your current or target role.")
    city = st.selectbox("City", cities, help="Location of work.")
    industry = st.selectbox("Industry", industries, help="Sector you work in.")
    selected_skills = st.multiselect("Skills (select all that apply)", skills_list, help="Technical and soft skills you possess.")
    skills_count = len(selected_skills)
    
    predict_button = st.button("🔮 Predict Salary", type="primary")
    reset_button = st.button("🔄 Reset")

if reset_button:
    st.rerun()

if predict_button:
    # Progress bar for fun
    progress = st.progress(0)
    for i in range(100):
        progress.progress(i + 1)
    
    # Map experience to numeric
    exp_map = {"0–1": 0.5, "1–3": 2, "3–5": 4, "5–8": 6.5, "8–12": 10, "12+": 15}
    exp_numeric = exp_map[exp_range]
    
    # Prepare input
    input_data = pd.DataFrame([{
        'Education Level': education,
        'Gender': gender,
        'Job Title': job_title,
        'City': city,
        'Industry': industry,
        'Experience Numeric': exp_numeric,
        'Skills Count': skills_count
    }])
    
    # Predict
    prediction = pipeline.predict(input_data)[0]
    lower = prediction * 0.9
    upper = prediction * 1.1
    
    # Main result
    col1, col2 = st.columns([2, 1])
    with col1:
        st.success(f"🎉 Predicted Annual Salary: ₹{lower:,.0f} - ₹{upper:,.0f}")
        st.write("This range is based on market data and your inputs.")
    with col2:
        st.image("https://via.placeholder.com/150x150.png?text=Salary+Chart", caption="Visual Placeholder", width=150)  # Placeholder image; replace with real if needed
    
    # Career Insights Dashboard
    st.header("📊 Career Insights Dashboard")
    st.write("Dive deeper into your career potential!")
    
    # Charts in columns
    col3, col4 = st.columns(2)
    with col3:
        with st.expander("📈 Salary vs Experience Range"):
            chart_exp = get_salary_vs_exp()
            st.bar_chart(chart_exp)
    with col4:
        with st.expander("📈 Salary vs Education Level"):
            chart_edu = get_salary_vs_edu()
            st.bar_chart(chart_edu)
    
    # Suggestions
    st.subheader("💡 Skill Improvement Suggestions")
    skill_sugs = get_skill_suggestions(skills_count)
    for sug in skill_sugs:
        st.write(f"• {sug}")
    
    st.subheader("🏆 Market Positioning")
    positioning = get_market_positioning(prediction)
    st.info(positioning)
    
    st.subheader("🚀 Career Growth Suggestions")
    growth_sugs = get_career_growth(exp_range, education, skills_count)
    for sug in growth_sugs:
        st.write(f"• {sug}")

# Footer
st.markdown("---")
st.write("Built with ❤️ using Streamlit. Data is synthetic for demonstration.")
st.write("Build By Ishan Kamboj")