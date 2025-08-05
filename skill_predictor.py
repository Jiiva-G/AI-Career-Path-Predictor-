import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import pickle

# Load dataset
df = pd.read_csv("data/jobs_dataset.csv")

# Vectorize skills
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(df["skills"])
y = df["career_path"]

# Train model
model = MultinomialNB()
model.fit(X, y)

# Save model
def predict_career(skills_input):
    with open("models/career_model.pkl", "rb") as f:
        vectorizer, model = pickle.load(f)
    input_vector = vectorizer.transform([skills_input])
    prediction = model.predict(input_vector)[0]
    return prediction