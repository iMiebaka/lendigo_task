from core import app
from core.models import db
from flask_migrate import upgrade, migrate, init, stamp

app.app_context().push()
# db.drop_all()
# db.create_all()

# init()
stamp()
migrate()
upgrade()