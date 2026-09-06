from flask import Flask, render_template

app = Flask(__name__)

data = [
    {"name": "สินค้า A", "price": 100},
    {"name": "สินค้า B", "price": 250},
    {"name": "สินค้า C", "price": 75},
]

@app.route("/")
def home():
    return render_template("index.html", items=data)

if __name__ == "__main__":
    app.run(debug=True)