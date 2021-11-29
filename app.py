from flask import Flask, render_template,request
app =Flask(__name__)
import re

@app.route('/')
def fun_1():
    return render_template('index.html')
@app.route('/',methods=['GET','POST'])
def home():
    if request.method == 'POST' :
        target = request.form.get('input_str')
        regex = request.form.get('input_regex')
        lst =re.findall(regex,target)
        length = len(lst)
        return render_template("index.html",target = target, regex = regex , lst = lst , length = length)

if __name__=="__main__":
    app.run(debug=True)

  