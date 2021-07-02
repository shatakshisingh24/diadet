from flask import Flask, render_template, redirect, request
import DTEMP1

app=Flask(__name__)


@app.route('/')
def hello():
    return render_template("index.html")

@app.route('/', methods= ['POST'])
def marks():
    if request.method == 'POST':
        age =  request.form['age']
        fpg = request.form['fpg']
        diabp = int(request.form['diabp'])
        sysbp = float(request.form['sysbp'])
        bmi= float(request.form['bmi'])
        avgsugar= float(request.form['avgsugar'])
        wcir = float(request.form['wcir'])
        hcir = float(request.form['hcir'])
        chol = float(request.form['chol'])
        ogtt = float(request.form['ogtt'])

        result= DTEMP1.pred(age, fpg, diabp, sysbp, bmi, avgsugar, wcir, hcir, chol, ogtt)
        result_dic={
            'Result':result
        }
        
    return render_template("index.html", result_out= result_dic)


if __name__=='__main__':
    app.run(debug=True)

