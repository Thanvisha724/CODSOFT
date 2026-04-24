import random
import string

def get_password_length():
    """
    Get the desired password length from the user.
    Validates that it's a positive integer.
    """
    while True:
        try:
            length = int(input("Enter the password length (minimum 1): "))
            if length > 0:
                return length
            else:
                print("Length must be greater than 0.")
        except ValueError:
            print("Please enter a valid number.")

def get_character_options():
    """
    Ask the user for character type preferences.
    Ensures at least one type is selected.
    Returns a dictionary of options.
    """
    options = {}
    print("Include the following? (y/n)")
    options['uppercase'] = input("Uppercase letters (A-Z)? ").strip().lower() == 'y'
    options['lowercase'] = input("Lowercase letters (a-z)? ").strip().lower() == 'y'
    options['numbers'] = input("Numbers (0-9)? ").strip().lower() == 'y'
    options['special'] = input("Special characters (!@#$%^&*)? ").strip().lower() == 'y'

    if not any(options.values()):
        print("You must select at least one character type.")
        return get_character_options()
    return options

def generate_password(length, options):
    """
    Generate a random password based on length and options.
    Guarantees at least one character from each selected type.
    """
    # Define character sets
    chars = {
        'uppercase': string.ascii_uppercase,
        'lowercase': string.ascii_lowercase,
        'numbers': string.digits,
        'special': '!@#$%^&*'
    }

    # Collect all possible characters
    all_chars = ''
    guaranteed = []
    for key, include in options.items():
        if include:
            all_chars += chars[key]
            guaranteed.append(random.choice(chars[key]))

    # If guaranteed characters are more than length, adjust
    if len(guaranteed) > length:
        return ''.join(random.sample(guaranteed, length))

    # Fill the rest randomly
    remaining_length = length - len(guaranteed)
    password_list = guaranteed + random.choices(list(all_chars), k=remaining_length)

    # Shuffle to randomize order
    random.shuffle(password_list)
    return ''.join(password_list)

def assess_password_strength(password):
    """
    Assess the strength of the password based on length and character types.
    Returns 'Weak', 'Medium', or 'Strong'.
    """
    length = len(password)
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in '!@#$%^&*' for c in password)

    types_count = sum([has_upper, has_lower, has_digit, has_special])

    if length < 8 or types_count < 2:
        return "Weak"
    elif length < 12 or types_count < 3:
        return "Medium"
    else:
        return "Strong"

def main():
    """
    Main function to run the password generator.
    """
    print("Welcome to the Password Generator!")

    while True:
        # Get password length
        length = get_password_length()

        # Get character options
        options = get_character_options()

        # Generate password
        password = generate_password(length, options)

        # Display password and strength
        print(f"\nGenerated Password: {password}")
        strength = assess_password_strength(password)
        print(f"Password Strength: {strength}")

        # Ask to generate another
        again = input("\nGenerate another password? (y/n): ").strip().lower()
        if again not in ['y', 'yes']:
            print("Thank you for using the Password Generator!")
            break

# Run the main function
if __name__ == "__main__":
    main()