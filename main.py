import time
from publix import User


user = User("username", "password")


schedule = user.getSchedule()

print(schedule)

user.close()

