from flask import Flask, render_template, request, flash, url_for, redirect, session
from data import *
app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


@app.route('/')
@app.route('/indexs')
def index():
    return render_template("indexs.html")

@app.route('/result',methods = ['POST', 'GET'])
def result():
    if request.method == 'POST':
        data = request.form.to_dict()
        DataPackage(data,PriceInvoice)
    return render_template("indexs.html", PriceInvoice = DataPackage(data,PriceInvoice),
     Weight = DataPackage(data,Weight), Repackag = DataPackage(data,Repackag), Transmission = DataPackage(data,Transmission))
app.run(debug=True)