from app import app, db

print("Database URI:", app.config['SQLALCHEMY_DATABASE_URI'])

try:
    with app.app_context():
        db.create_all()
        print("Database tables created successfully.")
except Exception as e:
    print("Error creating database tables:", e)