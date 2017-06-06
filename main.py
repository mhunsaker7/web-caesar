from flask import Flask, request
from caesar import rotate_string
app = Flask(__name__)
app.config['DEBUG'] = True


form = """
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px
            }}
            textarea {{
                margin: 10px 0;
                width: 520px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
        <form action="/rot" method = "post">
            <div>
                <label for="rot">Rotate by:</label>
                <input id ="rot" type="text" name="rot" value="0"/>
            </div>
            <textarea type="text" name="text" />{0}</textarea>
            <br>
            <input type="submit" value="submit query" />
        </form>    
    </body>
</html>
"""


@app.route("/")
def index():
    return form.format("")

@app.route("/rot", methods=['POST'])
def encrypt():
    rotate_by_string = request.form['rot']
    rot = int(rotate_by_string)
    text = request.form['text']
    new_string = rotate_string(text, rot)
    return form.format(new_string)


app.run()