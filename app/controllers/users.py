from sqlmodel import Session, select

from models.users import User, UserModel

async def create_user(usermodel: UserModel, db: Session):
    
    existsting_user = db.exec(select(User).where(User.email == usermodel.email)).first()
    if not existsting_user:
        print("no user exists")
    user = User.from_orm(usermodel)
    db.add(user)
    db.commit()
    db.refresh(user)
    return {"success": f"User mit ID {user.id} erstellt"}
   
async def get_user(user_id: int, db: Session):
    query_user = db.exec(select(User).where(User.id == user_id)).first()

    if not query_user:
        return {"error": "User not found"}


    return {"success": f"User with ID {query_user.id} found"}


def testfunction():
    print("du SPahahahahst")
    
def vondertaufe():
    print("HUDN")