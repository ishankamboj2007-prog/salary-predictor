import pandas as pd
from data import generate_data

# Generate a smaller dataset for insights (to avoid loading large data in app)
df = generate_data(10000)
avg_salary = df['Salary'].mean()

def get_salary_vs_exp():
    return df.groupby('Experience Range')['Salary'].mean()

def get_salary_vs_edu():
    return df.groupby('Education Level')['Salary'].mean()

def get_skill_suggestions(skills_count):
    suggestions = []
    if skills_count < 3:
        suggestions.append("Consider acquiring more technical skills like Python or Machine Learning to boost your salary.")
    if skills_count < 5:
        suggestions.append("Add soft skills such as Leadership or Project Management for better career prospects.")
    if skills_count >= 5:
        suggestions.append("Your skills are strong; focus on specialization in high-demand areas.")
    return suggestions

def get_market_positioning(prediction):
    if prediction < avg_salary * 0.9:
        return "Below average: Your predicted salary is lower than the market average. Consider upskilling or negotiating."
    elif prediction > avg_salary * 1.1:
        return "Above average: You're positioned well above the market average. Great job!"
    else:
        return "At average: Your predicted salary aligns with the market average."

def get_career_growth(exp_range, education, skills_count):
    suggestions = []
    if exp_range in ["0–1", "1–3"]:
        suggestions.append("Gain more experience by taking on challenging projects or roles.")
    if education in ["Diploma", "Bachelor"]:
        suggestions.append("Pursue higher education like a Master's to unlock higher-paying opportunities.")
    if skills_count < 4:
        suggestions.append("Build a diverse skill set to accelerate career growth.")
    suggestions.append("Network in your industry and seek mentorship for faster advancement.")
    return suggestions