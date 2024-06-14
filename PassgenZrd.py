import random  
import string  
import pyfiglet
import colorama
from colorama import Fore

# Initialize colorama for colored output
colorama.init(autoreset=True)

def display_name():
    """
    Display the name "PassgenZrd" using figlet.
    """
    # Generating  ASCII art of "PassgenZrd" using the figlet library
    path1 = "figlet-fonts/Graffiti"
    path2 = "figlet-fonts/wideterm"

    ascii_art1 = pyfiglet.figlet_format("PassgenZrd", font=path1, justify = "center")
    ascii_art2 = pyfiglet.figlet_format("Ethical WiZzzrd", font=path2, justify="center")
    # Printing the ASCII art in blue color for better visibility
    print(Fore.YELLOW + ascii_art1)
    print(ascii_art2)

def generate_password(length=12, use_uppercase=True, use_lowercase=True, use_digits=True, use_special=True):
    # Function to generate a random password
    # Default length is 12
    # By default, includes uppercase, lowercase, digits, and special characters

    if not (use_uppercase or use_lowercase or use_digits or use_special):
        # If no character sets are selected, raise an error
        raise ValueError("At least one character set must be enabled")

    character_pool = ""  # Initialize an empty string to hold the pool of characters

    if use_uppercase:
        character_pool += string.ascii_uppercase  # Add uppercase letters to the pool
    if use_lowercase:
        character_pool += string.ascii_lowercase  # Add lowercase letters to the pool
    if use_digits:
        character_pool += string.digits  # Add digits to the pool
    if use_special:
        character_pool += string.punctuation  # Add special characters to the pool

    # Generate a random password by choosing 'length' characters from the character pool
    password = ''.join(random.choice(character_pool) for _ in range(length))
    return password  # Return the generated password


def main():

    "display name of the tool"
    display_name();
    print("Welcome to the Password Generator Tool!")  # Welcome message

    print(Fore.RED + "[Note: Make sure the input are given as per asked form]\n\n")
    # Get user inputs for password criteria
    length = int(input("Enter the desired length of the password [integer]: "))  # Input for password length
    use_uppercase = input("Include uppercase letters? (y/n): ").strip().lower() == 'y'  # Include uppercase letters?
    use_lowercase = input("Include lowercase letters? (y/n): ").strip().lower() == 'y'  # Include lowercase letters?
    use_digits = input("Include digits? (y/n): ").strip().lower() == 'y'  # Include digits?
    use_special = input("Include special characters? (y/n): ").strip().lower() == 'y'  # Include special characters?
    
    # Generate the password based on user inputs
    password = generate_password(length, use_uppercase, use_lowercase, use_digits, use_special)
    print(f"Generated password: {password}")  # Output the generated password

if __name__ == "__main__":
    main()  

