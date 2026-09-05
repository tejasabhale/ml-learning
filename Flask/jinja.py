from flask import Flask, render_template, request

### Jinja 2 Template Engine
'''
{{ }} expression to print output in html
{%...%} conditions, for loops
{#...#} this is for comments
'''

app = Flask(__name__)

@app.route("/")
def welcome():
    return "<html><h1>Welcome to the Flask App</h1></html>"

## Variable Rule
@app.route('/successres/<int:score>')
def successres(score):
    if score>=50:
        res="PASSED"
    else:
        res="FAILED"

    exp={'score': score, 'res': res}

    return render_template('result1.html',results=exp)

## Variable Rule
@app.route('/success_results/<int:score>')
def success(score):
    if score>=50:
        res="PASSED"
    else:
        res="FAILED"

    return render_template('result.html',result=res)

if __name__ == "__main__":
    app.run(debug=True)