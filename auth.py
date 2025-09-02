import bcrypt
from db import SessionLocal, User

def create_user(username, password, is_admin=False):
    db = SessionLocal()
    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
    user = User(username=username, password_hash=hashed, is_admin=is_admin)
    db.add(user)
    db.commit()
    db.close()

def verify_user(username, password):
    db = SessionLocal()
    user = db.query(User).filter(User.username == username).first()
    db.close()
    if not user:
        return None
    if bcrypt.checkpw(password.encode(), user.password_hash.encode()):
        return user
    return None
