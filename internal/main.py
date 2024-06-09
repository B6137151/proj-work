from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from .config.database import SessionLocal, Base, engine
from .models.user import User  # Ensure this import path is correct

# Create all database tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/users/")
def create_user(username: str, password: str, email: str, tel: str, db: Session = Depends(get_db)):
    db_user = User(username=username, password=password, email=email, tel=tel)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# Add more endpoints as needed
