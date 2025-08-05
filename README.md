AI Career Path Predictor

AI Career Path Predictor is an intelligent web application that guides individuals in exploring future career paths based on their current skills and interests. By leveraging machine learning and GPT-powered models, it suggests suitable job roles, personalized learning resources, and even generates realistic, role-specific mock interview questions for comprehensive skill preparation.
Features

    Personalized Career Suggestions: Matches your skills and interests with trending career paths.

    Learning Recommendations: Offers curated learning resources to bridge skill gaps.

    Mock Interview Generator: Uses GPT to create custom questions tailored to your target career.

    User-Friendly Interface: Simple, interactive app built with Streamlit.

Installation

    Clone the repository

bash
git clone <your-repo-url>
cd ai-career-path-predictor

Install Python (>= 3.8)
Make sure Python 3.8 or higher is installed.

Create a Virtual Environment (Recommended)

bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

Install Python Dependencies

bash
pip install -r requirements.txt

Configure the OpenAI API Key

    Obtain an API key from OpenAI.

    Set the API key as an environment variable or place it in the project’s config file as instructed in the code.

Run the Application

    bash
    streamlit run app.py

Usage

    Open your browser to the local URL provided by Streamlit after launch.

    Select your current role and input your skills.

    Review the suggested career paths and recommended learning resources.

    Use the mock interview feature to practice with GPT-generated questions related to your target job role.

Configuration

    OpenAI API Key:
    Add your OpenAI key as an environment variable, e.g.,

    bash
    export OPENAI_API_KEY=sk-...

    Alternatively, follow the instructions in the code to set the key programmatically.

    Dataset Extension:
    To support emerging careers, you can add roles and skills to the dataset (data/roles_skills.csv or similar).

Technical Overview

    Tech Stack: Python, Streamlit, scikit-learn, Hugging Face Transformers, OpenAI API, pandas

    Core Modules:

        skill_predictor.py: Predicts and suggests career paths.

        gpt_interview.py: Generates GPT-based interview questions.

        app.py: Streamlit web interface and orchestration.

    Architecture:

        User inputs are vectorized (TF-IDF/embeddings) and matched to a curated roles dataset.

        GPT is called to generate custom, context-aware interview questions.

Troubleshooting

    Dependency Issues: Ensure your Python version meets requirements.

    API Errors: Verify your OpenAI API key and quota.

    Dataset Issues: Extend or update the dataset to cover niche domains as needed.
