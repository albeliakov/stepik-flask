from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route("/")
def render_main():
    # return render_template("main.html")
    return render_template("zad.html", role=admin)


@app.route("/results/")
def render_results():
    # for i in range(1000000000): i / 2
    my_dict = {
        1: {"cap": 2000, "ka_cnt": 1, "pos": [("У2", "У4")]},
        2: {"cap": 1500, "ka_cnt": 2, "pos": [("У2", "У4"), ("У6", "ТП3")]}
        }
    dict_json = json.dumps(my_dict)
    return render_template("results.html")
    # return render_template("index.html")



app.run()