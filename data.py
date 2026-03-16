import pandas as pd
import numpy as np

def generate_data(n=50000):
    exp_ranges = ["0–1", "1–3", "3–5", "5–8", "8–12", "12+"]
    educations = ["Diploma", "Bachelor", "Master", "PhD"]
    genders = ["Male", "Female", "Non-binary", "Prefer not to say"]
    job_titles = ["Software Engineer", "Data Scientist", "Product Manager", "Business Analyst", "DevOps Engineer", "UX Designer", "Marketing Specialist", "HR Manager", "Sales Executive", "Consultant"]
    cities = ["Mumbai", "Delhi", "Bangalore", "Hyderabad", "Chennai", "Pune", "Kolkata", "Ahmedabad", "Jaipur", "Surat"]
    industries = ["Technology", "Finance", "Healthcare", "Education", "Manufacturing", "Retail", "Consulting", "Media", "Energy", "Real Estate"]
    
    exp_map = {"0–1": 0.5, "1–3": 2, "3–5": 4, "5–8": 6.5, "8–12": 10, "12+": 15}
    
    data = []
    for _ in range(n):
        exp = np.random.choice(exp_ranges)
        edu = np.random.choice(educations)
        gen = np.random.choice(genders)
        job = np.random.choice(job_titles)
        city = np.random.choice(cities)
        ind = np.random.choice(industries)
        skills = np.random.randint(0, 11)  # 0-10
        
        # Salary logic (added gender multiplier for realism, e.g., slight variation)
        base = 300000
        exp_val = exp_map[exp]
        edu_mult = {"Diploma": 1, "Bachelor": 1.2, "Master": 1.4, "PhD": 1.6}[edu]
        gen_mult = {"Male": 1.0, "Female": 1.0, "Non-binary": 1.0, "Prefer not to say": 1.0}[gen]  # Neutral for inclusivity
        job_mult = {"Software Engineer": 1.2, "Data Scientist": 1.5, "Product Manager": 1.3, "Business Analyst": 1.1, "DevOps Engineer": 1.25, "UX Designer": 1.1, "Marketing Specialist": 1.0, "HR Manager": 1.05, "Sales Executive": 1.0, "Consultant": 1.4}[job]
        city_mult = {"Mumbai": 1.1, "Delhi": 1.05, "Bangalore": 1.2, "Hyderabad": 1.0, "Chennai": 0.95, "Pune": 1.0, "Kolkata": 0.9, "Ahmedabad": 0.95, "Jaipur": 0.85, "Surat": 0.8}[city]
        ind_mult = {"Technology": 1.2, "Finance": 1.3, "Healthcare": 1.1, "Education": 0.9, "Manufacturing": 1.0, "Retail": 0.95, "Consulting": 1.2, "Media": 1.0, "Energy": 1.1, "Real Estate": 1.05}[ind]
        skill_bonus = skills * 50000
        salary = base * exp_val * edu_mult * gen_mult * job_mult * city_mult * ind_mult + skill_bonus
        salary += np.random.normal(0, 100000)
        salary = max(salary, 200000)
        
        data.append({
            "Experience Range": exp,
            "Education Level": edu,
            "Gender": gen,
            "Job Title": job,
            "City": city,
            "Industry": ind,
            "Skills Count": skills,
            "Salary": salary
        })
    
    return pd.DataFrame(data)