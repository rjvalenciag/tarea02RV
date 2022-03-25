from flask import Flask
from routes.main.site import site


app = Flask(__name__)


# register blueprints
app.register_blueprint(site)
