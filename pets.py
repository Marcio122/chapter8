def describe_pet(animal_type, pet_name = 'kaila'):
    """Display information about pet """
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}!")
    
describe_pet('Dog')
describe_pet(animal_type ='cat', pet_name = 'leila') #order matters in arguments