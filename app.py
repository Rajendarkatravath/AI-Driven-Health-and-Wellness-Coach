import streamlit as st
from langchain import LLMChain, PromptTemplate
from dotenv import load_dotenv
import os
from langchain_groq import ChatGroq

# Load environment variables
load_dotenv()

# GROQ API key
GROQ_API_KEY = os.getenv('GROQ_API_KEY')

# Initialize Llama 3 model using ChatGroq with the GROQ API
llama3_model = ChatGroq(api_key=GROQ_API_KEY, model_name="llama3-70b-8192")

# Set up Streamlit UI with a custom theme and wide layout
st.set_page_config(page_title="AI-Driven Health and Wellness Coach", layout="wide")

# Customize the sidebar
st.sidebar.title("AI-Driven Health and Wellness Coach")
st.sidebar.write("Get personalized health and wellness advice, including fitness routines, diet plans, and mental health tips.")

# Header section with custom styling
st.markdown("""
    <style>
        .main-title {
            font-size: 3em;
            font-weight: bold;
            color: green;  /* Changed color to green */
            text-align: center;
            margin-bottom: 0.5em;
        }
        .subheader {
            font-size: 1.5em;
            color: green;  /* Changed color to green */
            margin-top: 1em;
        }
        .footer {
            text-align: center;
            font-size: 0.9em;
            color: #888888;
            margin-top: 3em;
        }
        .input-section {
            margin-left: 2em;
            width: 90%;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown('<h1 class="main-title">AI-Driven Health and Wellness Coach</h1>', unsafe_allow_html=True)

# User profile inputs
st.sidebar.header("User Profile")
user_name = st.sidebar.text_input("Name")
age = st.sidebar.number_input("Age", min_value=0)
gender = st.sidebar.selectbox("Gender", ["Male", "Female", "Other"])
fitness_level = st.sidebar.selectbox("Fitness Level", ["Beginner", "Intermediate", "Advanced"])

user_profile = {
    "name": user_name,
    "age": age,
    "gender": gender,
    "fitness_level": fitness_level
}

# Health-related question input section
st.markdown('<h2 class="subheader">Ask for Health and Wellness Advice</h2>', unsafe_allow_html=True)

st.markdown('<div class="input-section">', unsafe_allow_html=True)
health_question = st.text_input("", placeholder="Type your health or wellness question here...")
st.markdown('</div>', unsafe_allow_html=True)

if health_question:
    # Define prompt templates for different tasks
    fitness_template = """Provide a personalized fitness routine based on the following details:
    Name: {name}
    Age: {age}
    Gender: {gender}
    Fitness Level: {fitness_level}
    Question: {question}
    Routine:"""

    diet_template = """Create a personalized diet plan based on the following details:
    Name: {name}
    Age: {age}
    Gender: {gender}
    Fitness Level: {fitness_level}
    Question: {question}
    Diet Plan:"""

    mental_health_template = """Provide mental health tips based on the following details:
    Name: {name}
    Age: {age}
    Gender: {gender}
    Fitness Level: {fitness_level}
    Question: {question}
    Tips:"""

    # Create prompt templates using LangChain
    fitness_prompt = PromptTemplate(template=fitness_template, input_variables=["name", "age", "gender", "fitness_level", "question"])
    diet_prompt = PromptTemplate(template=diet_template, input_variables=["name", "age", "gender", "fitness_level", "question"])
    mental_health_prompt = PromptTemplate(template=mental_health_template, input_variables=["name", "age", "gender", "fitness_level", "question"])

    # Create LLM Chains using ChatGroq LLM and templates
    fitness_chain = LLMChain(llm=llama3_model, prompt=fitness_prompt)
    diet_chain = LLMChain(llm=llama3_model, prompt=diet_prompt)
    mental_health_chain = LLMChain(llm=llama3_model, prompt=mental_health_prompt)

    # Task selection section
    st.markdown('<h2 class="subheader">Select a Type of Advice</h2>', unsafe_allow_html=True)
    advice_type = st.selectbox("Choose an advice type:", ["Fitness Routine", "Diet Plan", "Mental Health Tips"])

    if advice_type == "Fitness Routine":
        with st.spinner("Generating fitness routine..."):
            fitness_routine = fitness_chain.run({
                "name": user_name,
                "age": age,
                "gender": gender,
                "fitness_level": fitness_level,
                "question": health_question
            })
            st.subheader("Personalized Fitness Routine")
            st.write(fitness_routine)

    elif advice_type == "Diet Plan":
        with st.spinner("Generating diet plan..."):
            diet_plan = diet_chain.run({
                "name": user_name,
                "age": age,
                "gender": gender,
                "fitness_level": fitness_level,
                "question": health_question
            })
            st.subheader("Personalized Diet Plan")
            st.write(diet_plan)

    elif advice_type == "Mental Health Tips":
        with st.spinner("Finding mental health tips..."):
            mental_health_tips = mental_health_chain.run({
                "name": user_name,
                "age": age,
                "gender": gender,
                "fitness_level": fitness_level,
                "question": health_question
            })
            st.subheader("Mental Health Tips")
            st.write(mental_health_tips)

# Footer section
st.markdown('<div class="footer">Developed by Your katravath Rajendar. All rights reserved.</div>', unsafe_allow_html=True)
