from flask import Flask
from flask_smorest import Api
from flask_jwt_extended import JWTManager
from database import db
from config import Config

jwt = JWTManager()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    jwt.init_app(app)

    app.config['API_TITLE'] = 'Healthcare API'
    app.config['API_VERSION'] = 'v1'
    app.config['OPENAPI_VERSION'] = '3.0.3'
    app.config['OPENAPI_URL_PREFIX'] = '/'
    app.config['OPENAPI_SWAGGER_UI_PATH'] = '/swagger-ui'
    app.config['OPENAPI_SWAGGER_UI_URL'] = 'https://cdn.jsdelivr.net/npm/swagger-ui-dist/'

    with app.app_context():
        from resources import patient_blp, doctor_blp, appointment_blp
        api = Api(app)
        api.register_blueprint(patient_blp)
        api.register_blueprint(doctor_blp)
        api.register_blueprint(appointment_blp)
        db.create_all()

    return app


if __name__ == '__main__':
    flask_app = create_app(Config)
    flask_app.run(debug=True)