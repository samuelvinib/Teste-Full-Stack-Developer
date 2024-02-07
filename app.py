from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', result=0)


@app.route('/calculate', methods=['POST'])
def calculate():
    triangle_top = [request.form['top']]
    triangle_third = [request.form['third_1'], request.form['third_2']]
    triangle_second = [request.form['second_1'], request.form['second_2'], request.form['second_3']]
    triangle_base = [request.form['base_1'], request.form['base_2'], request.form['base_3'], request.form['base_4']]
    triangle = [triangle_top, triangle_third, triangle_second, triangle_base]

    for i in range(len(triangle) - 2, -1, -1):

        for j in range(len(triangle[i])):
            triangle[i][j] += max(triangle[i + 1][j], triangle[i + 1][j + 1])

    max_total = triangle[0][0]
    triangle_sum = 0
    for line in max_total:
        triangle_sum += sum(int(digit) for digit in str(line))

    return render_template('index.html', result=triangle_sum)


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
