from flask.cli import FlaskGroup
from flask_migrate import Migrate

from apps import create_app

app, db = create_app()

migrate = Migrate()
migrate.init_app(app, db)

cli = FlaskGroup(app)

if __name__ == '__main__':
    cli()