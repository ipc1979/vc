from flask import Flask
from controllers.graphql import register_graphql_controllers
from config import config

app = Flask(__name__)
register_graphql_controllers(app)
app.run(port=config.port)