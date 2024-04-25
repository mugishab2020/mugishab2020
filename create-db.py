from users import db

def init_db():
    # Create all database tables
    db.create_all()

if __name__ == '__main__':
    # When the script is executed, call the init_db function
    init_db()
