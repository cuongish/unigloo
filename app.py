from flask import Flask
from flask import render_template
from flask_cors import CORS
from flask_cors import cross_origin

from handler import Handler
from handler import tabulate_availability
from handler import tabulate_products
from handler import get_complete_inventory_data
from handler import select_distinct_manufacturers

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

product_results = tabulate_products()
manufacturers = select_distinct_manufacturers(product_results)
complete_inventory_data = get_complete_inventory_data(manufacturers)
inventory_df = tabulate_availability(complete_inventory_data)
final_dataframes = Handler()
final_dataframes.export_final_df(product_results, inventory_df)


@app.route('/')
@cross_origin()
def index():
    return render_template('index.html')


@app.route('/gloves', methods=("POST", "GET"))
@cross_origin()
def show_gloves_tables():
    data = final_dataframes.gloves
    return render_template('simple.html', tables=[data.to_html(classes='gloves')],
                           titles=[data.columns.values])


@app.route("/beanies", methods=("POST", "GET"))
@cross_origin()
def show_beanies_tables():
    data = final_dataframes.beanies
    return render_template('simple.html', tables=[data.to_html(classes='beanies')],
                           titles=[data.columns.values])


@app.route("/facemasks", methods=("POST", "GET"))
@cross_origin()
def show_facemasks_tables():
    data = final_dataframes.facemasks
    return render_template('simple.html', tables=[data.to_html(classes='facemasks')],
                           titles=[data.columns.values])


if __name__ == '__main__':
    app.run()
