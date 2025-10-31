from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class DBConnectionHandler:
    def __init__(self)-> None:
        self.__connection_string: str = "sqlite:///database.db"
        self.__engine = None
        self.session = None

    def connection_to_db(self):
        if self.__engine is None:
            self.__engine = create_engine(self.__connection_string)

    def get_engine(self):
        return self.__engine

    def __enter__(self):
        session_maker = sessionmaker()
        self.session = session_maker(bind=self.__engine)
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if self.session:
            self.session.close()

db_connection_handler = DBConnectionHandler()

## ex com postgris
# class DBConnectionSettings:
#     def __init__(self, host: str, port: int, username: str, password: str, database: str):
#         self.host = host
#         self.port = port
#         self.username = username
#         self.password = password
#         self.database = database

#     def get_connection_string(self) -> str:
#         return f"postgresql://{self.username}:{self.password}@{self.host}:{self.port}/{self.database}"
