from app import app
from flask import render_template, request
from app.models import model, formopener

@app.route('/')
@app.route('/index')
@app.route('/index.html')
def index():
    return render_template('/index.html')

@app.route('/')
@app.route('/lifespan')
@app.route('/lifespan.html', methods=["POST","GET"])
def lifespan():
    if request.method == "GET":
        return "Please use form"
    else:
        age = 70
        userdata = request.form
        gender = userdata["gender"]
        activity = userdata["activity"]
        user_age = userdata["age"]
        health = userdata["health"]
        user_weight = userdata["weight"]
        height= userdata["height"]
        drugs= userdata["drugs"]
        
        
        if gender == "female":
            age = age + 10
        elif gender == "male":
            age = age + 2
        
        if activity == "yes" or activity == "occasionally":
            age = age + 5
        elif activity == "no":
            age = age - 5
    
        if user_weight == "underweight" or user_weight == "overweight":
            age = age - 5
        elif user_weight == "average":
            age = age + 8
        elif user_weight == "obese":
            age = age -10
    
        if height== "short":
            age= age + 3
        elif height == "average":
            age = age + 8
        elif height== "tall":
            age = age - 2
    
        if health == "yes":
            age = age - 3
        elif health == "no":
            age = age + 3
        elif health == "unsure":
            age = age
        
        if drugs== "yes":
            age = age - 5
        elif drugs== "no":
            age= age + 2
        
        
    return render_template('/lifespan.html', age = age)