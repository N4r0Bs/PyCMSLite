from pydantic import BaseSettings, PostgresDsn

from fastapi import FastAPI
from fastapi.templating import Jinja2Templates

from fastapi.staticfiles import StaticFiles

class PostgresDatabaseConfiguration(BaseSettings):
    DB_USER: str    
    DB_PASSWORD: str
    DB_NAME: str
    DB_SERVER: str
    DB_PORT: str

    @property
    def database_url(self) -> str:
        return PostgresDsn.build(
            scheme="postgresql",
            user=self.DB_USER,
            password=self.DB_PASSWORD,
            host=self.DB_SERVER,
            port=self.DB_PORT,
            path=f"/{self.DB_NAME}"
            )


    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'

postgresdb = PostgresDatabaseConfiguration()

DATABASE_URL = postgresdb.database_url

app = FastAPI()
app.mount("/static", StaticFiles(directory="app/views/static"), name="static")
templates = Jinja2Templates(directory="app/views/templates")