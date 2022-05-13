from core import app
from core.models import db
from flask_migrate import upgrade, migrate, stamp

app.app_context().push()

stamp()
migrate()
upgrade()