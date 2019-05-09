from flask import Flask

app = Flask(__name__)

# Hello World
# @app.route('/')
# def home():
#     return 'Hello World!'

# POST /store data: {name:}
@app.route('/store', methods=['POST'])
def create_store():
    pass


# GET /store/<string:name>
@app.route('/store/<string:name>')
def get_store_by_name(name):
    pass

# GET /store
@app.route('/store')
def get_store():
    pass

# POST /store/<string:name>/item {name:, price:}
@app.route('/store/<string:name>/item', methods=['POST'])
def create_store_item(name):
    pass

# GET /store/<string:name>/item
@app.route('/store/<string:name>/item')
def get_store_item(name):
    pass


app.run(port=5000)
