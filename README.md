# PassgenZrd

PassgenZrd is a simple yet powerful password generation tool developed to create secure passwords tailored to your specifications.

## Overview

This Python script utilizes randomization and user input to generate complex passwords. Let's explore its functionality:

### Importing Libraries

The script imports essential libraries such as `random`, `string`, `pyfiglet` for ASCII art, and `colorama` for colored output.

### Displaying Name

The `display_name()` function generates ASCII art for the names "PassgenZrd" and "Ethical WiZzzrd" using the pyfiglet library, providing an aesthetic introduction.

### Password Generation Function

The `generate_password()` function generates random passwords based on user-defined criteria:
- **Length**: Specifies the desired password length.
- **Character Sets**: Users can include uppercase letters, lowercase letters, digits, and special characters based on their needs.

### Main Function

The main functionality is encapsulated in a user-friendly menu system:
- Users are prompted to specify password criteria such as length and character types.
- The script then generates and displays a password that meets the specified criteria.

### Execution

To run the tool:
1. Clone the repository:
   ```
   git clone https://github.com/your-username/PassgenZrd
   ```

2. Navigate to the project directory:
   ```
   cd PassgenZrd
   ```

3. Run the script:
   ```
   python PassgenZrd.py
   ```


