from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    triangle = request.form['triangle']
    return f'Você enviou: {triangle}'


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
