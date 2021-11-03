from flask import Flask, render_template, request, flash

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')
    
@app.route('/EJ')
def EJ():
    return render_template('EJ.html')
    
@app.route('/PM')
def PM():
    return render_template('PM.html')

@app.route('/SS')
def SS():
    return render_template('SS.html')

@app.route('/TJS')
def TJS():
    return render_template('TJS.html')

@app.route('/VF')
def VF():
    return render_template('VF.html')

@app.route('/FR')
def FR():
    return render_template('FR.html')

@app.route('/JC')
def JC():
    return render_template('JC.html')

@app.route('/FC')
def FC():
    return render_template('FC.html')

@app.route('/OG')
def OG():
    return render_template('OG.html')

@app.route('/GC')
def GC():
    return render_template('GC.html')

@app.route('/PE')
def PE():
    return render_template('PE.html')

if __name__ == "__main__":
    app.run(debug=True)
