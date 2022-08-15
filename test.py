from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/post')
def post():
    response = render_template('index.html',title='POST送信')
    return response

@app.route('/next', methods=['POST'])
def next():
    a = int(request.form['a'])
    b = int(request.form['b'])
    c = int(request.form['c'])
    D = (b*b - 4*a*c)**0.5
    x_1 = (-b + D)/(2*a)
    x_2 = (-b - D)/(2*a)
    response = render_template('result.html',title='送信後ページ',x1=x_1,x2=x_2,a=a,b=b,c=c)
    return response

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000, debug=True)