from flask import Flask, url_for, render_template, request

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

@app.route("/")
def render_main():
    return render_template('index.html')

@app.route("/burrito")
def render_burrito():
    money = float(request.args['money'])
    # The request object stores information about the request sent to the server.
    # args is a MultiDict (like a dictionary but can have multiple values for the same keys
    # The information in args is visible in the url for the page being requested (ex. .../response?color=blue)
    num_burritos = roundFloat(money/8.5)
    return render_template('burrito.html', response = num_burritos)

@app.route("/meter")
def render_meter():
    meters = float(request.args['meters'])
    centimeters = roundFloat(meters*100)
    return render_template('meter_to_centimeter.html')

if __name__=="__main__":
    app.run(debug=False, port=54321)

def roundFloat(num):
    return int(num*100) / 100.0
