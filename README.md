# ark_py

code --install-extension esbenp.prettier-vscode
code --install-extension dbaeumer.vscode-eslint
code --install-extension PKief.material-icon-theme
code --install-extension dracula-theme.theme-dracula
code --install-extension usernamehw.errorlens
code --install-extension eamodio.gitlens
code --install-extension rangav.vscode-thunder-client
code --install-extension wix.vscode-import-cost

code --install-extension esbenp.prettier-vscode
code --install-extension dbaeumer.vscode-eslint
code --install-extension dracula-theme.theme-dracula
code --install-extension PKief.material-icon-theme

code --install-extension ms-python.python
code --install-extension ms-python.vscode-pylance

code --install-extension eamodio.gitlens
code --install-extension usernamehw.errorlens

### INSTALL E AMBIENTE VIRTUAL

-- pip install virtualenv
---- python3 -m venv venv
------ . venv/bin/activate
--------- > SELECT INTERPRETADOR

-- pip install pylint
---- pylint --generate-rcfile > .pylintrc

extensão vscode Pylint

criar requirements.txt --- venv/bin/pip3 freeze > requirements.txt

criar requirements.txt


--- pip3 install -r requirements.txt


### vali rodar o lint antes de commitar

-- pip3 install pre-commit
---- pre-commit --version
----- pre-commit install

### banco sqlite

-- No terminal:
1- python3

> > > 2- import sqlite3
> > > 3- sqlite3.connect('database.db')

<sqlite3.Connection object at 0x7ea8941c0400>

### orm

-- pip3 install SQLAlchemy


## model (conexão e comunicação com banco )

### settings
  - conexão com banco de dados neste caso como estamos com sqlalchemy por uma string

### entities
  - entidades que espelham o banco de dados 

### repositories
  - ações no banco

### tests https://docs.pytest.org/en/stable/getting-started.html

 - pip3 install -U pytest


## with

````
class AlgumaCoisa:
    def __enter__(self):
        print("Estou entrando")

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Estou saindo")


with AlgumaCoisa as O_que_vai_no_meio:
    print("meio")

exc_type: O tipo exceção que ocorreu, se houver.
    Se não ocorreu nenhuma exceção, este parâmetro será None

exc_val: O valor da exceção que ocorreu, se houver.
    Se não ocorreu nenhuma exceção, este parâmetro será None

exc_tb: O traceback (rastreamento de pilha) associado à exceção que ocorreu,
se houver.
    Se não ocorreu nenhuma exceção, este parâmetro será None

````

## criar mock para teste uni 

-- pip install mock-alchemy

basico: criamos basicamente um teste com dados staticos ou immemory

primeiro criamos uma representação da connection

````
class MockConnection:
    def __init__(self)->None:
-->session  self.session = UnifiedAlchemyMagicMock( -> 
            data=[
                (
--> query que espero [mock.call.query(PetsTable)], #query
                    [
-> result              PetsTable(name="dog", type="dog"),
                        PetsTable(name="cat", type="cat"),
                    ],  # resultado
                )
            ]
        )

    def __enter__(self): -> enter 
        return self

    def __exit__(self, exc_type, exc_val, exc_tb): -> exit
        pass

````


## pip3 install pytest-mock


## FLASK 

-- pip3 install Flask

-- pip3 install Flask-Cors