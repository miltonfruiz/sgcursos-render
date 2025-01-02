from flask import Flask
from flask_cors import CORS
from cursos_app.config import Config
from cursos_app.models import db
from cursos_app.routes import routes
from flask_migrate import Migrate
import os

app = Flask(
    __name__,
    template_folder=os.path.join(os.getcwd(), 'cursos_app/templates'),
    static_folder=os.path.join(os.getcwd(), 'cursos_app/static')
)

app.config.from_object(Config)
CORS(app, resources={r"/api/*": {"origins": "*"}}, supports_credentials=True)

db.init_app(app)
migrate = Migrate(app, db)

app.register_blueprint(routes)

@app.errorhandler(Exception)
def handle_exception(e):
    app.logger.error(f"Error no controlado: {e}")
    return {"mensaje": "Error interno del servidor", "tipo": "error"}, 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
