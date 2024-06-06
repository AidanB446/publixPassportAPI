from publix import User

user = User("username", "password")

schedule = user.getSchedule()

payStatementHistory = user.payStatementHistory()

user.close()

