from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_login import LoginManager

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///rentify.db'
db = SQLAlchemy(app)
CORS(app)

# Import routes after app and db are created to avoid circular imports
from routes import *

# Initialize Flask-Login
login_manager = LoginManager(app)
login_manager.login_view = 'login'

from models import User

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Create an application context
with app.app_context():
    # Create all database tables
    db.create_all()

# Now you can run your application
if __name__ == '__main__':
    app.run(debug=True)
