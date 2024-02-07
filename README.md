### INSTALL
pyenv install 3.8
pyenv virtualenv 3.8 vemo-challenge
pyenv activate vemo-challenge

### REQ DEV
pip install -r requirements_dev.txt

### REQ
pip install -r requirements.txt

### RUN
python ./daemon.py

### TESTS
pytest

### TESTS COVERAGE
pytest --cov=services tests/

### DIRECTORIES
config              Config app values
controllers         Flask controllers 
data                Files with data
docs                Project doc
domain              Domain entities
gql                 GraphQL Entitites and Resolvers
repositories        Repositories implemented to access data files
services            Services with injected repositories to form responses

### DECISIONS
GraphQL add flexibility to client and simplify endpoints
Flask   have a simple integration to GraphQL
Pandas  powerfull data analisys specificaly to explore csv files