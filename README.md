# Publix PassPort API
API to interact with publix passport. Still under development, features are still being added.

# WARNING
Publix requires mutlifactor authentification on login. Currently the API will prompt you for the factors sent to you via SMS in the terminal.

I recomend editing the __init__() function in 'publix.py' file to fit your needs.


# Installation

It will be shipped as a PIP package soon.
For now clone and refer to as shown in example below and in 'main.py' file.

```python
pip install -r requirements.txt

```

# Usage

```python

from publix import User

user = User('username', 'password')

schedule = user.getSchedule() # returns hashmap
payStatements = user.payStatementHistory() # returns list



```


