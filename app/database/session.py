from sqlmodel import Session, SQLModel

from database.engine import engine


async def get_db():
    with Session(engine) as session:
        yield session


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)
    
