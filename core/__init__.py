from flask import Flask, render_template, Blueprint, request, jsonify, g, session, redirect
from flask_jwt import JWT, jwt_required, current_identity
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_migrate import Migrate
from config import config
from flask_caching import Cache
# from flask_jwt_extended import (
#     JWTManager, jwt_required, create_access_token,
#     get_jwt_identity, decode_token
# )
from celery import Celery, shared_task



# dev_flag = 'production'
dev_flag = 'default' # Commnent this during deployment

app = Flask(__name__,
            template_folder = "index.html")


app.config.from_object(config[dev_flag])
cache = Cache(app, config=app.config['CACHE_TYPE'])
db = SQLAlchemy(app)
# jwt = JWTManager(app)
migrate = Migrate(app, db)
db.init_app(app)


celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
celery.config_from_object(app.config['CELERY_BEAT_SCHEDULE'], namespace='CELERY')
celery.conf.update(app.config)
CORS(app,resources={r"/api/*": {"origins": "*"}})


from .apis.views import api

# Register bleprints
app.register_blueprint(api, url_prefix='/api/v1/')


@app.route('/')
def home():
    return jsonify({"status": "success", "message": "App Working", "routes": ['%s' % rule for rule in app.url_map.iter_rules()]}), 200



# Error handlers
@app.errorhandler(404)
def page_not_found(e):
    return jsonify({"status": "error", "message": "url or page does not exist"}), 404

@app.errorhandler(400)
def bad_request(e):
    return jsonify({"status": "error", "message": "url does not exist"}), 400
    
@app.errorhandler(405)
def method_not_allowed(e):
    return render_template('index.html'), 405

@app.errorhandler(500)
def internal_server_error(e):
    return jsonify({"status": "error", "message": "We have a server error"}), 500


