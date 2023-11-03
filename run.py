from dotenv import load_dotenv

# from waitress import serve

# load_dotenv(".env")

from app.main import app
from app.main.extensions.flask_extensions import api

# from app.main.extensions.flask_extensions import db

if __name__ == "__main__":
    # db.init_app(app) ## No DB Operations as of 2023-07-10 16:48:00
    api.init_app(app)
    app.run(host="0.0.0.0", debug=True, load_dotenv=".env")
    # serve(app, host="0.0.0.0", port=5000)
