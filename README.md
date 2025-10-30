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

criar requirements.txt
--- venv/bin/pip3 freeze > requirements.txt

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

-- pip install SQLAlchemy


## model (conexão e comunicação com banco )

### settings
  - conexão com banco de dados neste caso como estamos com sqlalchemy por uma string

### entities
  - entidades que espelham o banco de dados 

### repositories
  - ações no banco

### tests https://docs.pytest.org/en/stable/getting-started.html

 - pip3 install -U pytest