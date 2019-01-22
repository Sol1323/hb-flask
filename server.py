"""Greeting Flask app."""

from random import choice

from flask import Flask, request

# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible',
    'wonderful', 'smashing', 'lovely']

GOOD = ['good', 'nice', 'okay', 'catty']

DISS = ["mean", "bad", "bossy", "annoying"]

INSULTS = ["awful", "worst", "None", "False"]


@app.route("/")
def start_here():
    """Home page."""

    return """<!doctype html><html>Hi! This is the 
        <a href="/hello"> home page</a></html>"""


@app.route("/hello")
def say_hello():
    """Say hello and prompt for user's name."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/greet">
        <h2>COMPLIMENT</h2>
          What's your name? 
          <input type="text" name="person">
          <br>
          Compliment:
           <label>
                <input class="with-gap" type="radio" name="compliment" value="mild">mild</input>
           </label>
           <input type="radio" name="compliment" value="extreme">extreme!</input>
           <br>
          <input type="submit" value="Submit">
        </form>
        <br>
        <h2>DISS</h2>
        <form action="/diss">
          What's your name? 
          <input type="text" name="person">
          <br>
          Insults:
           <input type="radio" name="insults" value="mild">mild</input>
           <input type="radio" name="insults" value="extreme">extreme!</input>
          <input type="submit" value="Submit">
        </form>

      </body>
    </html>
    """


@app.route("/test")
def populate_input_forms:

    radio_buttons = ""

    for word in AWESOMENESS:
        my_string = 

    return """
    <!doctype html>
    <html>
    <head>
        <title>Test Input Forms</title>
    </head>
    <body>

    Insults:
           <input type="radio" name="insults" value="mild">mild</input>
           <input type="radio" name="insults" value="extreme">extreme!</input>
          <input type="submit" value="Submit">
    </body>
    </html>
    """


@app.route("/greet")
def greet_person():
    """Get user by name."""

    player = request.args.get("person")
    compliment_level = request.args.get("compliment")

    if compliment_level == "mild": 
        compliment = choice(GOOD)
    else:
        compliment = choice(AWESOMENESS)

    return """
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {}! I think you're {}!
      </body>
    </html>
    """.format(player, compliment)



@app.route("/diss")
def diss_person():
    """Get user by name."""

    player = request.args.get("person")
    insult_level = request.args.get("insults")

    if insult_level == "mild": 
        insult = choice(DISS)
    else:
        insult = choice(INSULTS)

    return """
    <!doctype html>
    <html>
      <head>
        <title>A Diss</title>
      </head>
      <body>
        Hi, {}! I think you're {}!
      </body>
    </html>
    """.format(player, insult)

if __name__ == "__main__":
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True, host="0.0.0.0")
