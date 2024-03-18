def hash_function(password):
    hash_value = 0
    for char, index in zip(password, range(len(password))):
         hash_value += ord(char) * index
    return hash_value % 10**9
class Account:
    def __init__(self, login, password):
        self._login = login
        self._password = password

    @property
    def login(self):
        return self._login

    @property
    def password(self):
        return hash_function(self._password)
    @login.setter
    def login(self,login):
        raise AttributeError('Изменение логина невозможно')
    @password.setter
    def password(self, password):
        self._password = password

account = Account('hannymad', 'cakeisalie')

print(account.login)
print(account.password)