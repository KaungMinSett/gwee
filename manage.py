from getpass import getpass
import sys

from flask import current_app
from review_post import app, bcrypt
from review_post.models import Admin, db

def main():
    """Main entry point for script."""
    with app.app_context():
        db.metadata.create_all(db.engine)
        if Admin.query.all():
            print ('A user already exists! Create another? (y/n):',)
            create = input()
            if create == 'n':
                return

        print ('Enter Username: ',)
        username = input()
        password = getpass()
        assert password == getpass('Password (again):')

        admin = Admin(
            username= username , 
            password_hash=bcrypt.generate_password_hash(password).decode('utf-8'))
        db.session.add(admin)
        db.session.commit()
        print ('User added.')


if __name__ == '__main__':
    main()