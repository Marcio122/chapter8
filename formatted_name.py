#def get_formatted_name(first_name, last_name):
 #   """Return a full name neatly formatted """
  #  full_name = f"{first_name} {last_name}"
   # return full_name.title()
#musicians = get_formatted_name('marcio', 'jeovety')
#print(musicians)

# making an argument optional
def get_formatted_name(first_name, last_name, middle_name = ''):
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"

    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()
musicians = get_formatted_name('Alexandre', 'geoveti')
print(musicians)

musicians = get_formatted_name('Alexandre', 'pedro', 'geoveti')
print(musicians)