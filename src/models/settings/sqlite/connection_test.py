import pytest
from sqlalchemy import Engine
from .connection import DBConnectionHandler

@pytest.mark.skip(reason="Teste de conexão com banco de dados SQLite desativado temporariamente")
def test_db_connection_handler():
    db_handler = DBConnectionHandler()  # Cria nova instância para isolar o teste
    
    assert db_handler.get_engine() is None # Verifica que engine inicia como None
  
    db_handler.connection_to_db()  # Conecta ao banco

    db_engine = db_handler.get_engine() 

    assert db_engine is not None # Verifica que engine foi criada
    
    assert str(db_engine.url) == "sqlite:///database.db" # BONUS: Verifica se é uma engine válida

    assert isinstance(db_engine, Engine) # Verifica se é uma instância de Engine do SQLAlchemy
