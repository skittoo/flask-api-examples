from flask import Flask, request

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
def get_stores():
    return { "stores":  stores}


@app.post("/store")
def create_store():
    request_data = request.get_json()
    new_store = {"name": request_data["name"], "items": []}
    stores.append(new_store)

    return new_store, 201 # 201 means: okay, i have acepted the new data.


@app.post("/store/<string:name>/item")
def create_item(name= None):
    request_data = request.get_json()
    for store in stores:
        if store["name"] == name:
            new_item = {"name": request_data["name"], "price": request_data["price"]}
            store["items"].append(new_item)
            return new_item, 201
    return {"message": "Store not found"}, 404

@app.get("/store/<string:name>")
def get_store(name= None):
    for store in stores:
        if store["name"] == name:
            return store, 200
    return {"message": "store not found"}, 404

@app.get("/store/<string:name>/item")
def get_items(name= None):
    for store in stores:
        if store["name"] == name:
            return {"items": store["items"]}, 200
    return {"message": "store not found"}, 404
    