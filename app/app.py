from flask import Flask, render_template
from methods import get_data

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def index():
    return render_template('index.html', totales=get_data.push_data_totales(), totales_line=get_data.push_data_totales_line(), top_5_2018=get_data.push_data_top_5_2018(), top_10_totales=get_data.push_data_top_10_totales(), cusco_la_libertad=get_data.push_data_cusco_la_libertad())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
