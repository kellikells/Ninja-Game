from flask import Flask, render_template, request, redirect, session

import random   # to create random gold amounts
app = Flask(__name__)

app.secret_key = 'ThisIsSecret'   # secret key required for session 

# =======================================
@app.route('/')
def index():

    if not 'totalGold' in session:
        session['totalGold'] = 0

    if not 'farm' in session:
        session['farm'] = random.randrange(10, 21) 

    if not 'cave' in session:
        session['cave'] = random.randrange(5, 11)

    if not 'house' in session:
        session['house'] = random.randrange(2, 6)

    if not 'casino' in session:
        session['casino'] = random.randrange(-50, 51)
    
    if not 'activites' in session:
        session['activites'] = ""

    print("totalGold:", session['totalGold'])
    print("farm", session['farm'])
    print("cave", session['cave'])
    print("house", session['house'])
    print("casino", session['casino'])

    return render_template("index.html")



# =======================================
# add to totalGold according to hidden input value (ex: farm)
@app.route('/process_money', methods=['POST'])
def process_money():
    
    print(request.form['building'])
    
    if request.form['building'] == "farm":

        session['totalGold'] += session['farm']
        
        print("farm:", session['farm'])
        print("new total gold:", session['totalGold'])

        session['activities'] = ('Earned', session['farm'], 'gold from farm')   
      

        session['farm'] = random.randrange(10, 21) 

    if request.form['building'] == "cave":
        session['totalGold'] += session['cave']
        session['activities'] = ('Earned', session['cave'], 'gold from cave') 
        session['cave'] = random.randrange(5, 11)


    if request.form['building'] == "house":
        session['totalGold'] += session['house']
        session['activities'] = ('Earned', session['house'], 'gold from house') 
        session['house'] = random.randrange(2, 6)

    if request.form['building'] == "casino":
        session['totalGold'] += session['casino']
        session['activities'] = ('Earned', session['casino'], 'gold from casino') 
        session['casino'] = random.randrange(-50, 51)

    return redirect('/')

    



# route to handle clearing session 
# =======================================
# @app.route('/destroy_session')
# def destroySession():
#     session.clear()
#     return redirect('/')  





# =======================================
if __name__=="__main__":
  # run our server
    app.run(debug=True) 
