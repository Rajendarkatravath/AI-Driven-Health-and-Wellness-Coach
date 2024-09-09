# AI-Driven Health and Wellness Coach

## Overview

The AI-Driven Health and Wellness Coach is a web application built using Streamlit and powered by LangChain's ChatGroq Llama 3 model. The application provides personalized fitness routines, diet plans, and mental health tips based on user input. It is designed to offer customized advice to help users achieve their health and wellness goals.

## Features

- **Personalized Fitness Routine**: Generate a customized fitness plan based on user details.
- **Personalized Diet Plan**: Create a tailored diet plan based on user input.
- **Mental Health Tips**: Provide mental health tips to enhance overall well-being.
- **User Profile Input**: Collect and use user information such as name, age, gender, and fitness level.
- **Interactive UI**: Easy-to-use interface with options for asking health-related questions and receiving personalized advice.

## Requirements

- Python 3.7 or higher
- Streamlit
- LangChain
- dotenv
- langchain_groq

## Setup

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/health-wellness-coach.git
   cd health-wellness-coach

2. **Create and Activate a Virtual Environment:**
   ```bash
   python -m venv venv

   On Windows:
   ```bash
   venv\Scripts\activate

   On macOS/Linux:
   ```bash
   source venv/bin/activate
   
2. **install Dependencies:**

   ```bash
   pip install -r requirements.txt

3. **Set Up Environment Variables:**
   Create a .env file in the root directory and add your GROQ API key:
   GROQ_API_KEY=your_groq_api_key

4. **Run the Application:**
   ```bash
   streamlit run app.py
Usage
Input User Profile: Enter your name, age, gender, and fitness level in the sidebar.
Ask for Health Advice: Type your health-related question and select the type of advice you need (Fitness Routine, Diet Plan, or Mental Health Tips).
Receive Personalized Advice: View the generated advice or plan based on your input.
Code Overview
app.py: Main application file that sets up the Streamlit interface and handles user input.
.env: Configuration file for storing environment variables.
Customization
Modify the fitness_template, diet_template, and mental_health_template in app.py to change the content and format of the generated advice.
Update styling and UI elements in the Streamlit code as needed.
Contributing
Feel free to fork the repository and submit pull requests. Contributions to improve the application are welcome!

License
This project is licensed under the MIT License. See the LICENSE file for details.

Contact
Developed by Katravath Rajendar. For any questions or feedback, please contact katravathrajendar18@gmail.com.