from flask import Flask, jsonify, request

app = Flask(__name__)

user = {
        "name":"Amit Kumar",
        "city":"Ranchi" 
      }

# for getting request
@app.route('/data/<key>', methods=['GET'])
def get_data(key):
    if key in user:
        return jsonify(user)
    else:
        return jsonify({'error': 'Key not found'})


# for post request
@app.route('/data/<key>', methods=['POST'])
def add_data(key):
    new_data = request.get_json()
    user[new_data[key]] = new_data[key]
    return jsonify({'message': 'Data added successfully'})

#for update request
@app.route('/data/<key>', methods=['PUT'])
def update_data(key):
    if key in user:
        updated_data = request.get_json()
        user[key] = updated_data['value']
        return jsonify({'message': 'Data updated successfully'})
    else:
        return jsonify({'error': 'Key not found'})

#for delete request
@app.route('/data/<key>', methods=['DELETE'])
def delete_data(key):
    if key in user:
        del user[key]
        return jsonify({'message': 'Data deleted successfully'})
    else:
        return jsonify({'error': 'Key not found'})


if __name__ == '__main__':
    app.run()