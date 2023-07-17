# Put your app in here.


# ***/add***   Adds ***a*** and ***b*** and returns result as the body.

# ***/sub***   Same, subtracting ***b*** from ***a***.

# ***/mult***   Same, multiplying ***a*** and ***b***.

# ***/div***   Same, dividing ***a*** by ***b***.

from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route("/add", methods=["GET"])
def add_num():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    
    return str(add(a, b))

@app.route("/sub", methods=["GET"])
def sub_num():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    
    return str(sub(a, b))

@app.route("/mult", methods=["GET"])
def mult_num():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    
    return str(mult(a, b))

@app.route("/div", methods=["GET"])
def div_num():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    
    return str(div(a, b))

@app.route("/math/<operation>", methods=["GET"])
def math(operation):
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    if operation == 'add':
        return str(add(a, b))
    elif operation == 'sub':
        return str(sub(a, b))
    elif operation == 'mult':
        return str(mult(a, b))
    elif operation == 'div':
        return str(div(a, b))