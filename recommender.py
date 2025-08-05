# Learning Path Recommender
def recommend_courses(career_path):
    recommendations = {
        "Data Scientist": ["Coursera ML", "Kaggle Python", "DeepLearning.AI"],
        "Frontend Developer": ["freeCodeCamp", "FrontendMasters", "JavaScript.info"],
        "AI Engineer": ["Udemy Deep Learning", "Udemy Machine Learning", "Udemy Python","Coursera ML", "fast.ai", "Kaggle"],
        "Backend Developer": ["Udemy Python", "Udemy Java", "Udemy C++"],
        "I/UX Designer" : ["Google UX Design Certificate, Interaction Design Foundation, Adobe XD & Figma Tutorials"],
        "Data Analyst":["Google Data Analytics Certificate, Mode SQL tutorials, DataCamp Analyst Track"],
        "DevOps Engineer": ["Udacity Cloud DevOps Nanodegree, Linux Foundation DevOps, KodeKloud DevOps Courses"],
        "LLM Engineer": ["Hugging Face NLP Course, OpenAI API Docs, LangChain Docs, DeepLearning.AI NLP"],
        "Android Developer":["Google Android Developer Course, Kotlin Android Tutorials, Udemy Android Bootcamp"],
        "iOS Developer": ["iOS App Dev with Swift (Apple), Stanford iOS Course, Hacking with Swift"],
        "Full Stack Developer": ["The Odin Project, Full Stack Open, MERN Stack Tutorials (freeCodeCamp, Udemy)"],
        "Business Analyst": ["Coursera Business Analytics, Excel for Business, SQL & Tableau Courses"],
        "Software Developer": ["CS50 by Harvard, Python/Java Programming (Udemy), LeetCode Practice"],
        "Computer Vision Engineer": ["PyImageSearch Courses, Coursera Computer Vision, OpenCV Docs"],
        "Prompt Engineer": ["OpenAI Prompt Engineering Guide, DeepLearning.AI Prompt Engineering Course"],
        "Prompt Engineer" : ["OpenAI Cookbook", "Learn Prompting", "DeepLearning.AI"],
        "Conversational AI Engineer" : ["OpenAI Cookbook", "Learn Prompting", "DeepLearning.AI","Hugging Face", "DeepLearning.AI NLP"],
    }
    return recommendations.get(career_path, ["No recommendations found"])
