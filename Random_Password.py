import random
import string

def generate_pass():
    length = int(input("Enter Password length: ").strip())
    include_upper = input("Include Uppercase? (yes/no): ").strip().lower()
    include_special = input("Include Special? (yes/no): ").strip().lower()
    include_digits = input("Include Digits? (yes/no): ").strip().lower()

    if length < 4:
        print("Password length must be 4 characters.")
        return
    
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase if include_upper == "yes" else ""
    special = string.punctuation if include_special == "yes" else ""
    digits = string.digits if include_digits == "yes" else ""
    all = lower + upper + special + digits

    choice_character = []
    if include_upper == "yes":
        choice_character.append(random.choice(upper))
    if include_special == "yes":
        choice_character.append(random.choice(special))
    if include_digits == "yes":
        choice_character.append(random.choice(digits)) 

    choice_length = length - len(choice_character)
    password = choice_character

    for _ in range(choice_length):
        character = random.choice(all)
        password.append(character)

    random.shuffle(password)
    str_password = "".join(password)
    return str_password

password = generate_pass()
print(password)
