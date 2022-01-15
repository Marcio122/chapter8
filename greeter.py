def greet_user(username):
    """Display a simple message"""
    print(f"Hello, {username.title()}!")
greet_user('marcio')
#message
def message():
    print(f"I'm learning how to define functions")

message()

#favorite book
def favorite_book(title):
    print(f"One of my favorite books is {title.title()}!")
favorite_book('Alice in Wonderland')

#using a function with a while loop
def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()
while True:
    print(f"\nPlease tell me your name")
    print((f"Enter quit to break the program"))
    
    f_name = input("First name: ")
    if f_name == 'quit':
        break
    else:
        print(f_name)
    l_name = input("Last name: ")
    if l_name == 'quit':
        break
    else:
        print(l_name)
    
    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}!")

