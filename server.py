from flask import Flask, render_template, request, session
import random
app = Flask(__name__)
app.secret_key = "baconinthesink"

@app.route('/' method =['GET', 'POST'])
def count_gold():
    if not total_gold in session:
       session['total_gold'] = 0
    if request.method == 'POST':
        if request.form['add_gold'] == 'farm':
            session['total_gold'] += random.randint(10,21)
        elif request.form['add_gold'] == 'cave':
            session['total_gold'] += random.randint(5,10)
        elif request.form['add_gold'] == 'house':
            session['total_gold'] += random.randint(2,5)
        elif request.form['add_gold'] == 'casino':
            session['total_gold'] += random.randint(-50,50)
    elif request.method == 'GET':
        return render_template('index.html')


app.run (debug=True)
