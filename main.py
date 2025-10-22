def greet_user():
    
    name = input("Please enter your name: ")
    
    if name.strip():
        formatted_name = name.strip().capitalize()
        
        print(f"\nHello, {formatted_name}! Welcome to the Python world.")
    else:
        print("\nHello there! It seems you didn't enter a name.")


if __name__ == "__main__":
    greet_user()