from flask import Flask, render_template, request, session, redirect, flash
import random
app = Flask(__name__)
app.secret_key = "baconinthesink"

@app.route('/', methods =['GET', 'POST'])
def count_gold():
    if 'total_gold' not in session:
       session['total_gold'] = 0
    return render_template('index.html')
    

@app.route('/process_money', methods=['POST'])
def method_name():
    if request.method == 'POST':
        x = session['total_gold']
        if request.form['submit'] == 'farm':
            session['total_gold'] += random.randint(10, 21)
            flash ( "from the farm: " + str(session['total_gold'] - x )+ " gold")
        elif request.form['submit'] == 'cave':
            session['total_gold'] += random.randint(5, 10)
            flash("from the cave: " + str(session['total_gold'] - x) + " gold")
        elif request.form['submit'] == 'house':
            session['total_gold'] += random.randint(2, 5)
            flash("from the house: " + str(session['total_gold'] - x) + " gold")
        elif request.form['submit'] == 'casino':
            session['total_gold'] += random.randint(-50, 50)
            flash("from the casino: " + str(session['total_gold'] - x) + " gold")
    return redirect('/')

app.run (debug=True)
