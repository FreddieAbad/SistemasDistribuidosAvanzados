import requests

# Servidor central
SERVER_URL = 'http://3.87.24.34:5000'  

def create_user(shard_id, user_data):
    url = f'{SERVER_URL}/users'
    data = {'shard_id': shard_id, 'user_data': user_data}
    response = requests.post(url, json=data)
    return response.json()

def get_users(shard_id):
    url = f'{SERVER_URL}/users/{shard_id}'
    response = requests.get(url)
    return response.json()

if __name__ == '__main__':
    create_user('shard1', {'username': 'user1', 'email': 'user1@example.com'})
    users = get_users('shard1')
    print(users)
