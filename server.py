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
        session['farm'] = random.randrage(10,21)

    if not 'cave' in session:
        session['cave'] = random.randrage(5,11)

    if not 'house' in session:
        session['house'] = random.randrage(2,6)

    if not 'casino' in session:
        session['casino'] = random.randrage(-50,51)

    print(session['totalGold'])
    print(session['farm'])
    print(session['cave'])
    print(session['house'])
    print(session['casino'])
    

    return render_template("index.html")




# @app.route('/process_money', methods=['POST'])
def process_money():
    



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
