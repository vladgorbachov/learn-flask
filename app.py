from flask import Flask
from flask import jsonify, request

app = Flask(__name__)

# use Python Dict as DB
storage = dict()
# structure of storage: key - username, value - dict(default empty) in future will contain info about current user


# put some default users into db
storage.update(
    {
        "username1": {},
        "username2": {},
        "username3": {},
        "username4": {}
    }
)


@app.route('/')
def hello_world():
    return jsonify({'msg': 'Hello, World!'})


@app.route('/users/list/')
def user_list():
    return jsonify(storage)


@app.route('/users/delete/<username>')
def delete_user(username):
    old_users = storage.copy()
    storage.pop(username, False)
    if username in old_users:
        return f'User {username} was deleted'
    else:
        return 'User doesn`t exist or already deleted'


@app.route('/users/add/', methods=["POST"])
def add_user_list():
    data = request.get_json()
    try:
        username = data['username']
    except Exception as exp:
        response = {'msg': f'The field {exp} is required'}
        username = False



if __name__ == '__main__':
    app.run(debug=True)
