### Working with API's --- JSON

from flask import Flask, jsonify, request

app = Flask(__name__)

## Initial data in my to do list

items = [
    {"id": 1, "name": "Item 1", "description": "This is item 1"},
    {"id": 2, "name": "Item 2", "description": "This is item 2"},
]

@app.route('/')
def home():
    return "Welcome to the To Do List App"

## GET : Retrieve all the items
@app.route('/items', methods=['GET'])
def getItems():
    return jsonify(items)

## GET : Retrive a specific item by id
@app.route('/items/<int:itemId>')
def getItem(itemId):
    item = next((item for item in items if item["id"]==itemId), None)
    if item is None:
        return jsonify({"error": "Item not found."})
    return jsonify(item)

## Post : Create a new task
@app.route('/items', methods=['POST'])
def createItem():
    if not request.json or not 'name' in request.json:
        return jsonify({"error": "item not found"})

    newItem = {
        "id": items[-1]["id"]+1,
        "name": request.json["name"],
        "description": request.json["description"]
    }

    items.append(newItem)
    return jsonify(newItem)

## PUT : Update existing task
@app.route('/items/<int:itemId>', methods=['PUT'])
def update_item(itemId):
    item = next((item for item in items if item["id"]==itemId), None)
    if item is None:
        return jsonify({"error": "Item not found"})
    item['name'] = request.json.get('name', item['name'])
    item['description'] = request.json.get('description', item['description'])
    return jsonify(item)

## Delete : Delete an item
app.route('/items/<int:itemId', methods=['DELETE'])
def deleteItem(itemId):
    global items
    items = [item for item in items if item['id']!= itemId]
    return jsonify(items)

if __name__ == '__main__':
    app.run(debug=True)
