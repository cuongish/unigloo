from flask import Flask
from flask import render_template

from handler import main

app = Flask(__name__)
final_dataframes = main()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/gloves', methods=("POST", "GET"))
def show_gloves_tables():
    data = final_dataframes.gloves
    return render_template('simple.html', tables=[data.to_html(classes='gloves')],
                           titles=[data.columns.values])


@app.route("/beanies", methods=("POST", "GET"))
def show_beanies_tables():
    data = final_dataframes.beanies
    return render_template('simple.html', tables=[data.to_html(classes='beanies')],
                           titles=[data.columns.values])


@app.route("/facemasks", methods=("POST", "GET"))
def show_facemasks_tables():
    data = final_dataframes.facemasks
    return render_template('simple.html', tables=[data.to_html(classes='facemasks')],
                           titles=[data.columns.values])


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
