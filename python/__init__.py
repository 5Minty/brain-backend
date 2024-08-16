from flask import Flask
from flask_cors import CORS
from flask_socketio import SocketIO
from python.config import FE_ADDRESS

python = Flask(__name__)

# TODO: remove 'hello world'
@python.route("/")
def hello_world():
    # TODO: FE_ADDRESS is /python not localhost of FE
    return f"<p>Hello, {FE_ADDRESS}!</p>"

CORS(python, resources={r"/api/*": {"origins": FE_ADDRESS}})
socketio = SocketIO(python, cors_allowed_origins=FE_ADDRESS)

from python import routes  # import routes to register with the app
