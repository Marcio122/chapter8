#Passing a list to a function
def greet_user(names):
    """Print a simple greeting to each user in  the list"""
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)
usernames = ['hannah', 'ty', 'margot']
greet_user(usernames)
#second example
def saudar(marcios):
    """Mostrar o nome dos usuários"""
    for marcio in marcios:
        sms = f"Olá, {marcio.title()}!"
        print(sms)
lista_usuarios = ['marcio', 'kailany']
saudar(lista_usuarios)