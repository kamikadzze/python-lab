from flask import Flask, render_template, request
import os
from datetime import datetime

app = Flask(__name__)

my_skills = [
    "Python",
    "c++",
    "php",
    "c#",
    "java",
    "HTML",
    "CSS",
    "JavaScript",
    "SQL",
    "Git",
]


@app.route('/skills')
@app.route('/skills/<int:id>')
def display_skills(id=None):
    if id is None:
        total_skills = len(my_skills)
        return render_template('skills.html', skills=my_skills, total_skills=total_skills)
    elif id < len(my_skills):
        return render_template('skills.html', skills=[my_skills[id]])
    else:
        return "Немає значення з таким id"
my_resume = [
    {"company": "Globl soft", "experience": "5 years", "role": "m-Dev"},
    {"company": "Google", "experience": "3 years", "role": "Web-Dev"}
]

@app.route('/resume')
@app.route('/resume/<int:id>')
def display_resume(id=None):
    if id is None:
        total_resume = len(my_resume)
        return render_template('resume.html', resume=my_resume, total_resume=total_resume)
    elif 0 <= id < len(my_resume):
        return render_template('resume.html', resume=[my_resume[id]])
    else:
        return "Немає значення з таким id"

@app.route('/')
def home():
    os_info = os.name
    user_agent = request.user_agent.string
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return render_template('general.html', os_info=os_info, user_agent=user_agent, current_time=current_time)

@app.route('/portfolio')
def portfolio():
    os_info = os.name
    user_agent = request.user_agent.string
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return render_template('portfolio.html', os_info=os_info, user_agent=user_agent, current_time=current_time)

@app.route('/skills')
def skills():
    os_info = os.name
    user_agent = request.user_agent.string
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return render_template('skills.html',  os_info=os_info, user_agent=user_agent, current_time=current_timee)

@app.route('/resume')
def resume():
    os_info = os.name
    user_agent = request.user_agent.string
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return render_template('resume.html', os_info=os_info, user_agent=user_agent, current_time=current_time)

if __name__ == '__main__':
    app.run(debug=True)
