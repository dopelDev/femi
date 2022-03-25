from flask import Flask, render_template
from methods import get_data

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def index():
    return render_template('index.html', totales=get_data.push_data_totales(), totales_line=get_data.push_data_totales_line())

if __name__ == '__main__':
    app.run()
