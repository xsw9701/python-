from flask_caching import Cache
from flask_mail import Mail
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_debugtoolbar import DebugToolbarExtension


db = SQLAlchemy()
migrate = Migrate()
mail = Mail()
cache = Cache(
    config={
        "CACHE_TIME": "redis",
        "CACHE_TYPE": "simple"
    }
)


def init_ext(app):
    db.init_app(app)
    migrate.init_app(app, db)
    DebugToolbarExtension(app)
    mail.init_app(app)
    cache.init_app(app)
