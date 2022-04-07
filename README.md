# api-calculator
api-calculator is a calculator made with Python using APIs. It calculates simple mathematical expressions.

## Quick Tutorial
To run the project you will need to create a Python3 Virtual Environment (be sure you have python3 and pip installed) and activate it, the commands are:

    python3 -m venv /path/to/venv
    path/to/venv> /bin/activate

Now you need to install flask, you can do it by entering:

    pip install Flask

Finally, to run the API use:

    (virtualenv)path/to/api-calculator> python app.py

## Interacting with the API
The URLs are:

*Home - http://0.0.0.0:5000/
*Show calculation history: http://0.0.0.0:5000/results
*Operate: http://0.0.0.0:5000/operate?operation=x*y

## Operating
The API can add, subtract, multiply and divide. At the moment, only integers are accepted.

Examples:

    http://0.0.0.0:5000/operate?operation=10+10
    http://0.0.0.0:5000/operate?operation=10-10
    http://0.0.0.0:5000/operate?operation=10*10
    http://0.0.0.0:5000/operate?operation=10/10