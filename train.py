import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import Pipeline
import joblib
from data import generate_data

# Generate data
df = generate_data(50000)

# Map experience to numeric
exp_map = {"0–1": 0.5, "1–3": 2, "3–5": 4, "5–8": 6.5, "8–12": 10, "12+": 15}
df['Experience Numeric'] = df['Experience Range'].map(exp_map)

# Features (added Gender)
cat_features = ['Education Level', 'Gender', 'Job Title', 'City', 'Industry']
num_features = ['Experience Numeric', 'Skills Count']

# Pipeline
preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), num_features),
        ('cat', OneHotEncoder(handle_unknown='ignore'), cat_features)
    ]
)

pipeline = Pipeline([
    ('preprocessor', preprocessor),
    ('model', RandomForestRegressor(n_estimators=100, random_state=42))
])

# Train
X = df[cat_features + num_features]
y = df['Salary']
pipeline.fit(X, y)

# Save
joblib.dump(pipeline, 'salary_pipeline.joblib')
print("Pipeline trained and saved as salary_pipeline.joblib")