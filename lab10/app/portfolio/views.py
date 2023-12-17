from flask import render_template, request
from . import portfolio
from datetime import datetime
import os

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
my_resume = [
    {"company": "Globl soft", "experience": "5 years", "role": "m-Dev"},
    {"company": "Google", "experience": "3 years", "role": "Web-Dev"}
]
@portfolio.route('/')
def home():
    os_info = os.name
    user_agent = request.user_agent.string
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return render_template('portfolio.html', os_info=os_info, user_agent=user_agent, current_time=current_time)

@portfolio.route('/portfolio')
def portfolios():
    os_info = os.name
    user_agent = request.user_agent.string
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return render_template('portfolio.html', os_info=os_info, user_agent=user_agent, current_time=current_time)

@portfolio.route('/skills')
@portfolio.route('/skills/<int:id>')
def skills(id=None):
    if id is None:
        total_skills = len(my_skills)
        return render_template('skills.html', skills=my_skills, total_skills=total_skills)
    elif id < len(my_skills):
        return render_template('skill.html', skills=[my_skills[id]], id=id)
    else:
        return "Немає навички з таким id"
    
@portfolio.route('/resume')
@portfolio.route('/resume/<int:resume_id>')
def resume(resume_id=None):
    if resume_id is None:
        total_resume = len(my_resume)
        return render_template('resume.html', resume=my_resume, total_resume=total_resume)
    elif 0 <= resume_id < len(my_resume):
        return render_template('resume.html', resume=[my_resume[resume_id]])
    else:
        return "Немає значення з таким id"