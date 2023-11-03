from flask_restx import Api


from app.main.utils import constants

## Define Api object with Basic App Information
api = Api(
    title=constants.APP_TITLE,
    version=constants.APP_VERSION,
    description=constants.APP_DESC,
    prefix=constants.API_VERSION,
    doc=constants.API_DOCS_URL,
    contact_email="shaikmalikbasha@example.com",
)
