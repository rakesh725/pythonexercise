PYTHONEXCERSICE

# Overview
Python is a multi-purpose programming langauge, what does that mean? it can be used for create many types of applications. For example: web applicaion, data analytics, machine learning, web service, automated tasks and so on. 

Review this pdf to get an overview on python: https://4techblog.com/wp-content/uploads/2023/02/Introduction-To-Python.pdf

This excercise provides step by step python exercises to learn advance python

# Github
You are already reading this on github. I would recommend creating your own github account adding your own branch to this repository, I have created Arav directory for you to use.

Learn more about github here: https://docs.github.com/en/get-started/quickstart/hello-world

# Python IDE
An editor is required to write and run python code. [Pycharm](https://www.jetbrains.com/pycharm/) is the most popular one but in our exercise we will use [VSCode](https://code.visualstudio.com/Download). 

- [Download VSCode]((https://code.visualstudio.com/Download)) 
- Install [python extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python)

## Excercise 1: Python script to take user input to add/subtract/multiply/divide
- Use python input function to take user input 
- Review exercise_1.py once you have completed your script

## Using venv
Its recommended that you use Python virtual environment when developing python applications.
venv (for Python 3) and virtualenv (for Python 2) allow you to manage separate package installations for different projects. 

Install venv:
````
python3 -m pip install --user virtualenv
````
Create a venv for your project:
````
python3 -m venv <project_name>
````

Active venv:
````
source <project_name>/bin/activate
````

Thats it, now write your project code and test. 
When you install and use a python library, its best to create requirement.txt file whch will list all libariries/modules you use in your project. Use following command to create requirement.txt file:
````
pip3 freeze > requirements.txt
````
Installing packages from requirements.txt:
````
pip3 install -r requirements.txt
````
As you code your application, keep requirements file updated using following command:
````
install -U -r requirements.txt
````

## Excercise 2:
Use venv to run your script from exercise 1

## Excercise 3:
- Create JSON file which stores all Make and Model of pick-up trucks available in USA in an array of dictonary. 
- Create a function to return pick-ups by brand amd type, reading the JSON file
- Write a test for this function

Example:
````
pickups =[
  {
    "brand": "Ford",
    "model": "F-150",
    "type": "Gasoline"
  },
  {
    "brand": "Ford",
    "model": "Lightning",
    "type": "Electric"
  }
]
````


