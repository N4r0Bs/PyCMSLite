from sqlmodel import create_engine
from core.config import DATABASE_URL

engine = create_engine(url=DATABASE_URL, echo=True)


    