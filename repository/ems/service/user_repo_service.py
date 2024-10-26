from repository.ems.model.ems import User
from sqlalchemy.orm import Session


class UserRepoService:
    def save(user : User, db : Session):
        db.add(user)
        db.commit()
    
    def update(user : User, db : Session):
        db.query(User).filter(User.id == user.id).update({User.firstname : user.firstname,
                                      User.lastname : user.lastname, 
                                      User.email : user.email, User.password : user.password})
        db.commit()

    def getByEmail(email : str, db : Session):
        return db.query(User).filter(User.email == email).first()
    
    def getById(id : int, db : Session):
        return db.query(User).filter(User.id == id).first()
    
    def deleteById(id: int, db : Session):
        db.query(User).filter(User.id == id).delete()
        db.commit()
    
    def getAll(db : Session):
        return db.query(User).all()