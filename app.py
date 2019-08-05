from flask import Flask, jsonify, request

app = Flask(__name__)

stores = [
    {
        'name': 'First',
        'items': [
            {
                'name': 'An item',
                'price': 15.99
            }
        ]
    }
]

# Hello World
# @app.route('/')
# def home():
#     return 'Hello World!'

# POST /store data: {name:}
@app.route('/store', methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {
        'name': request_data['name'],
        'items': []
    }
    stores.append(new_store)
    resp = jsonify(success=True)
    return resp


# GET /store/<string:name>
@app.route('/store/<string:name>')
def get_store_by_name(name):
    store_found = list(filter(lambda store: store['name'] == name, stores))
    if bool(len(store_found)):
        return jsonify(store_found[0])
    else:
        return jsonify({'message': 'Store not found'})

# GET /store
@app.route('/store')
def get_stores():
    return jsonify(stores)

# POST /store/<string:name>/item {name:, price:}
@app.route('/store/<string:name>/item', methods=['POST'])
def create_store_item(name):
    store_found = list(filter(lambda store: store['name'] == name, stores))
    if bool(len(store_found)):
        store = store_found[0]
        request_data = request.get_json()
        new_item = {
            'name': request_data['name'],
            'price': request_data['price']
        }
        store['items'].append(new_item)
        return jsonify(store)
    else:
        return jsonify({'message': 'Store not found'})


# GET /store/<string:name>/item
@app.route('/store/<string:name>/item')
def get_store_items(name):
    store_found = list(filter(lambda store: store['name'] == name, stores))
    if bool(len(store_found)):
        return jsonify({'items': store_found[0]['items']})
    else:
        return jsonify({'message': 'Store not found'})


app.run(port=5000)
