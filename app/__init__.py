from flask import Flask 
from flask_pymongo import PyMongo 


mongo = PyMongo()


def create_app():
    app = Flask(__name__)

    app.config["MONGO_URI"] = "mongodb://mkrs:Ojolali123@46.250.229.129:27017/educareer_tenant_ugm?authSource=admin"
    mongo.init_app(app)

    print(app.config, end="\n")

    try:
        mongo.cx.server_info()
        print("MongoDB connection successfully")
    except Exception as e:
        print(f"MongoDB connection failed: {e}")

    from .routes import main_bp
    app.register_blueprint(main_bp)

    return app
