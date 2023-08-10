from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'akjsdfafa'
    
    from .views import views

    app.register_blueprint(views, url_prefix='/')
    # app.register_blueprint(results, url_prefix='/results')

    return app