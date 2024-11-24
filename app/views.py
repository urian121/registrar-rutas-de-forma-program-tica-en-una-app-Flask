from flask import render_template
base_page = "pages"

def home():
    return render_template(f'{base_page}/index.html')

def about():
    return render_template(f'{base_page}/about.html')

def contact():
    return render_template(f'{base_page}/contact.html')

def services():
    return render_template(f'{base_page}/services.html')

def greet_user(username):
    return render_template(f'{base_page}/greetings.html', username=username)
