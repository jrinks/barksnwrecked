from app import create_store, db
from app.blueprints.auth.models import User

app = create_store()

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User}