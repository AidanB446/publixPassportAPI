# Publix PassPort API
API to interact with publix passport. Still under development, features are still being added.

# WARNING
Publix requires mutlifactor authentification on login. Currently the API will prompt you for the factors sent to you via SMS in the terminal.

I recomend editing the __init__() function in 'publix.py' file to fit your needs.


# Installation

## with pip
```python
pip install publixPassportAPI==0.0.3

```
## with git clone
```bash
git clone https://github.com/AidanB446/publixPassportAPI

pip install -r requirements.txt


```

# Usage

```python

from publixPassportAPI.publix import User

user = User('username', 'password')

schedule = user.getSchedule() # returns hashmap
payStatements = user.payStatementHistory() # returns list



```


