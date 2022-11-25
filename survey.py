from flask import Flask, render_template, request, redirect
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/result' ,  methods=['POST'])         
def resullt():
    print(request.form)
    name = request.form['username']
    dojolocation = request.form['dojolocation']
    favlang = request.form['favlang']
    comment = request.form['comment']

    return render_template("result.html" , name = name , dojolocation = dojolocation , favlang = favlang , comment = comment)



if __name__=="__main__":   
    app.run(debug=True)    
