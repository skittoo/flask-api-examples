from flask import Flask, jsonify

app = Flask(__name__)

stores = [
    {
        "name": "My Store",
        "items": [
            {
                "name": "Chair",
                "Price": 15.99
             },
            {
                "name": "Table",
                "Price": 15.99
             },
        ]
    }
]

@app.get("/store")
def get_store():
    return { "stores":  stores}
