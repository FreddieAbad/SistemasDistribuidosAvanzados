from flask import Flask, request, jsonify
import json

app = Flask(__name__)

shards_data = {
    "shard1": []
}

@app.route('/users', methods=['POST'])
def create_user():
    data = request.json
    shard_id = data.get('shard_id')
    user_data = data.get('user_data')
    shards_data[shard_id].append(user_data)
    return jsonify({"message": "User created successfully."}), 201

@app.route('/users/<shard_id>', methods=['GET'])
def get_users(shard_id):
    return jsonify(shards_data.get(shard_id, []))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

