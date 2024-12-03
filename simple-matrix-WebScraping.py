from flask import Flask, render_template_string, request
import numpy as np

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        matrix1_data = request.form['matrix1'].strip().splitlines()
        matrix2_data = request.form['matrix2'].strip().splitlines()
        operation = request.form['operation']

        matrix1 = np.array([[int(num) for num in row.split()] for row in matrix1_data])
        matrix2 = np.array([[int(num) for num in row.split()] for row in matrix2_data])

        if operation == 'Add':
            result = matrix1 + matrix2
        elif operation == 'Subtract':
            result = matrix1 - matrix2
        elif operation == 'Multiply':
            result = matrix1 @ matrix2

    html_template = """
    <!doctype html>
    <html lang="en">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
        <title>Matrix Calculator</title>
    </head>
    <body>
        <h1>Matrix Calculator by yusef emam</h1>
        <form method="post">
            <h2>Matrix 1</h2>
            <textarea name="matrix1" rows="4" cols="20" placeholder="Enter Matrix 1 values..."></textarea>
            <h2>Matrix 2</h2>
            <textarea name="matrix2" rows="4" cols="20" placeholder="Enter Matrix 2 values..."></textarea>
            <h2>Operation</h2>
            <select name="operation">
                <option value="Add">Add</option>
                <option value="Subtract">Subtract</option>
                <option value="Multiply">Multiply</option>
            </select>
            <button type="submit">Calculate</button>
        </form>

        {% if result is not none %}
            <h2>Result:</h2>
            <pre>{{ result }}</pre>
        {% endif %}
    </body>
    </html>
    """

    return render_template_string(html_template, result=result)

if __name__ == '__main__':
    app.run(debug=True)
