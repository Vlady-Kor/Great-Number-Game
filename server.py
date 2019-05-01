from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.route('/')
def count():
    session['server_num'] = random.randint(1,100)
    session['server_num'] = 5
    return render_template("index.html", x=session['server_num'])

@app.route('/calculate', methods=['POST'])
def fxn():
    result = ""
    user_num=int(request.form['guess'])
    if 'server_name' in session:
        session['server_name'] -=1
    if user_num == session['server_num']:
        result = "Got it"
    elif user_num < session['server_num']:
        result = "Too Low"
    else:
        result = "Too high"

    return redirect("/", int(calc=result))



if __name__=="__main__":
    app.run(debug=True)