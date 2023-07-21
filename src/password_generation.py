#!/usr/bin/python3
'''
## *Task Advanced:* Create a Password Generator for Linux Users

### Intro
password_generation.py:     Class object which generating secure password
author:                     Nakonechnyi Mikhail
date:                       04.07.23
version:                    2.1 (with OOP)
description of homework:


### Description

Your task is to create a password generator program using Python specifically
designed for Linux users. The program should generate strong and secure
passwords that can be used for user accounts on Linux systems.

### *Requirements:*

Prompt the user to enter the desired length for the password. Generate a
random password consisting of a combination of uppercase letters, lowercase
letters, numbers, and special characters. Ensure that the generated password
meets the following criteria:

    Contains at least one uppercase letter
    Contains at least one lowercase letter
    Contains at least one number
    Contains at least one special character (e.g., !, @, #, $, %, etc.)
    Display the generated password to the user.

### *Example Output:*

Welcome to the Linux User Password Generator!

Please enter the desired password length: 12

Generated password: 3@5uJ9#p1L$w

### *Note:*

You can utilize the random module in Python to generate random characters and
build the password. Consider using the string module in Python to access sets
of characters (uppercase, lowercase, numbers, and special characters). Make
sure to include clear instructions and error handling for invalid input.

## NEW REQUIREMENTS: HW3

### Objective: Implement a password generator program using basic
    object-oriented programming principles in Python.

### Instructions:

    Create a Python class called PasswordGenerator that will generate random
    passwords based on certain criteria.

    The PasswordGenerator class should have the following attributes:

    length: an integer representing the length of the password (default: 8)
    include_uppercase: a boolean indicating whether to include uppercase
        letters in the password (default: True)
    include_lowercase: a boolean indicating whether to include lowercase
        letters in the password (default: True)
    include_digits: a boolean indicating whether to include digits in the
        password (default: True)
    include_special_chars: a boolean indicating whether to include special
        characters in the password (default: True)

    Implement the following_ methods in the PasswordGenerator class:

    __init__(self): Initializes the attributes of the class.
    generate_password(self): Generates and returns a random password based on
        the specified criteria. The password should be a string of characters
        randomly chosen from the available character sets (uppercase letters,
        lowercase letters, digits, and special characters).

    Write a separate Python script (outside the class) that utilizes the
        PasswordGenerator class.

    Create an instance of the PasswordGenerator class.
    Prompt the user to input the desired password length and criteria (whether
        to include uppercase letters, lowercase letters, digits, and special
        characters).
    Use the instance of the class to generate a password based on the user's
        input.
    Display the generated password to the user.

    Test your program with different inputs and ensure it generates passwords
        that satisfy the user's criteria.

### ** Submission Guidelines**:

    Submit the Python script file containing the implementation of the
        PasswordGenerator class and the separate script that utilizes the
        class.
    Include comments in your code to explain the purpose and functionality of
        each section.
    Add any additional features or enhancements to the program if you desire,
        as long as the basic requirements are met.

### ** Note **: You may use any built-in Python libraries or functions related
        to random number generation or string manipulation to complete this
        assignment.

### Versions:
* 1.0 function realization
* 2.0 OOP realization
* 2.1 Fix Error Exception
* 2.2 Change Logic with new requirements (HW 3)

TODO: fix logic to access getter as default case in setters methor or defaults
'''

from sys import exit as ex
import random
import string


class PasswordGenerator:
    """Class to generate secure passwords."""
    value_err = "Password length must be a positive integer at least 16."
    type_length_err = "Password length must be a positive integer."

    def __init__(self, *args, **kwargs):
        """
        Initialize a PasswordGenerator object.

        Args:
            length (int, optional): Length of the password. Defaults to None.
            include_uppercase (bool, optional): Whether to include uppercase
                letters. Defaults to True.
            include_lowercase (bool, optional): Whether to include lowercase
                letters. Defaults to True.
            include_digits (bool, optional): Whether to include digits.
                Defaults to True.
            include_special_chars (bool, optional): Whether to include special
                characters. Defaults to True.
        """
        self.description = """Welcome to the Linux User Password Generator!"""
        self.is_set = kwargs.get('is_set', None)
        self.setdefault = kwargs.get('setdefault', False)
        self.setlength = kwargs.get('setlength', 16)
        self.setinclude_uppercase = kwargs.get('setinclude_uppercase', True)
        self.setinclude_lowercase = kwargs.get('setinclude_lowercase', True)
        self.setinclude_digits = kwargs.get('setinclude_digits', True)
        self.setinclude_special_chars = kwargs.get(
            'setinclude_special_chars', True)
        self.length = None
        self.include_uppercase = None
        self.include_lowercase = None
        self.include_digits = None
        self.include_special_chars = None
        self.password = ''

    # def __del__(self):
    #     print("PasswordGenerator object deleted.")

    def hello(self) -> str:
        """_summary_
        """
        return self.description

    def get_var_length_error(self):
        """_summary_
        """
        return self.value_err

    def get_type_length_error(self):
        """_summary_
        """
        return self.type_length_err

    def set_length(self, new_length=None) -> None:
        """_summary_

        Args:
            new_length (None): _description_
        """
        if new_length is not None:
            # try:
            # length_input = \
            #     abs(int(round(float(self.length))))
            # Check correct length
            if not isinstance(new_length, int):
                raise TypeError(self.type_length_err)
            if new_length < 0 or new_length < 16:
                raise ValueError(self.value_err)
            self.length = new_length
            # except (TypeError, ValueError, Exception) as err:
            #     print(f"Error: {str(err)}")
        # check if user set length value in constructor
        elif self.is_set is True and not self.setdefault:
            if not isinstance(self.setlength, int):
                raise TypeError(self.type_length_err)
            if self.setlength < 0 or self.setlength < 16:
                raise ValueError(self.value_err)
            self.length = self.setlength
        # check if set default=False and user was not set length
        # then get user input
        elif not self.setdefault and self.length is None:
            # Input validation from user
            length_input = 0
            while True:
                try:
                    length_input = \
                        int(input(
                            "Please enter the desired password length: "
                        ))
                    # Check correct length
                    if not isinstance(length_input, int):
                        raise TypeError(self.type_length_err)
                    if length_input < 0 or length_input < 16:
                        raise ValueError(self.value_err)
                    self.length = length_input
                    break
                except (TypeError, ValueError, Exception) as err:
                    print(f"Error: {str(err)}")
                except KeyboardInterrupt:
                    print("\nUser interrupted. Exiting...")
                    ex()
        elif self.setdefault:
            self.length = self.setlength

    def get_length(self) -> int:
        """_summary_

        if length is not set yet, can get minimal of default length

        Returns:
            int: _description_
        """
        if self.length is not None:
            return int(self.length)
        else:
            return 16

    def set_include_uppercase(self, include_uppercase=None) -> None:
        """_summary_

        Args:
            include_uppercase (_type_): _description_

        Raises:
            ValueError: _description_
        """
        if include_uppercase is not None:
            try:
                # Check correct include_uppercase
                if not isinstance(include_uppercase, bool):
                    raise ValueError("Include uppercase must be a boolean.")
                self.include_uppercase = bool(include_uppercase)
            except (TypeError, ValueError, Exception) as err:
                print(f"Error: {str(err)}")
        # check if user set include_uppercase value in constructor
        elif self.is_set is True and not self.setdefault:
            # Check correct include_uppercase
            if not isinstance(self.setinclude_uppercase, bool):
                raise ValueError("Include uppercase must be a boolean.")
            self.include_uppercase = self.setinclude_uppercase
        # check if set default=False and user was not set include_uppercase
        # then get user input
        elif not self.setdefault and self.include_uppercase is None:
            # Input validation from user
            while True:
                try:
                    inc_uppercase = input(
                        "Include uppercase letters? (Default: [y]): "
                        ).lower()
                    if inc_uppercase == 'y' or not inc_uppercase:
                        inc_uppercase = True
                    elif inc_uppercase != 'y':
                        inc_uppercase = False
                    self.include_uppercase = inc_uppercase
                    break
                except KeyboardInterrupt:
                    print("\nUser interrupted. Exiting...")
                    ex()
        # set default value
        elif self.setdefault:
            self.include_uppercase = self.setinclude_uppercase

    def get_include_uppercase(self) -> bool:
        """_summary_

        Returns:
            _type_: _description_
        """
        if self.include_uppercase is not None:
            return bool(self.include_uppercase)
        else:
            return True

    def set_include_lowercase(self, include_lowercase=None) -> None:
        """_summary_

        Args:
            include_lowercase (_type_): _description_

        Raises:
            ValueError: _description_
        """
        if include_lowercase is not None:
            try:
                # Check correct include_lowercase
                if not isinstance(include_lowercase, bool):
                    raise ValueError("Include lowercase must be a boolean.")
                self.include_lowercase = bool(include_lowercase)
            except (TypeError, ValueError, Exception) as err:
                print(f"Error: {str(err)}")
        # check if user set include_lowercase value in constructor
        elif self.is_set is True and not self.setdefault:
            # Check correct include_lowercase
            if not isinstance(self.setinclude_lowercase, bool):
                raise ValueError("Include lowercase must be a boolean.")
            self.include_lowercase = self.setinclude_lowercase
        # check if set default=False and user was not set include_lowercase
        # then get user input
        elif not self.setdefault and self.include_lowercase is None:
            # Input validation from user
            while True:
                try:
                    inc_lowercase = input(
                        "Include lowercase letters? (Default: [y]): "
                        ).lower()
                    if inc_lowercase == 'y' or not inc_lowercase:
                        inc_lowercase = True
                    elif inc_lowercase != 'y':
                        inc_lowercase = False
                    # Check correct include_lowercase
                    if not isinstance(inc_lowercase, bool):
                        raise \
                            ValueError("Include lowercase must be a boolean.")
                    self.include_lowercase = inc_lowercase
                    break
                except ValueError as valerr:
                    print(f"Invalid input. {str(valerr)}")
                except Exception as exc:
                    print(f"Error: {str(exc)}")
                except KeyboardInterrupt:
                    print("\nUser interrupted. Exiting...")
                    ex()
        # set default value
        elif self.setdefault:
            self.include_lowercase = self.setinclude_lowercase

    def get_include_lowercase(self) -> bool:
        """_summary_

        Returns:
            _type_: _description_
        """
        if self.include_lowercase is not None:
            return bool(self.include_lowercase)
        else:
            return True

    def set_include_digits(self, include_digits=None) -> None:
        """_summary_

        Args:
            include_digits (_type_): _description_

        Raises:
            ValueError: _description_
        """

        if include_digits is not None:
            try:
                # Check correct include_digits
                if not isinstance(include_digits, bool):
                    raise ValueError("Include digits must be a boolean.")
                self.include_digits = bool(include_digits)
            except (TypeError, ValueError, Exception) as err:
                print(f"Error: {str(err)}")
        # check if user set include_digits value in constructor
        elif self.is_set is True and not self.setdefault:
            # Check correct include_digits
            if not isinstance(self.setinclude_digits, bool):
                raise ValueError("Include lowercase must be a boolean.")
            self.include_digits = self.setinclude_digits
        # check if set default=False and user was not set include_digits
        # then get user input
        elif not self.setdefault and self.include_digits is None:
            # Input validation from user
            while True:
                try:
                    inc_digits = input(
                        "Include digits? (Default: [y]): "
                        ).lower()
                    if inc_digits == 'y' or not inc_digits:
                        inc_digits = True
                    elif inc_digits != 'y':
                        inc_digits = False
                    # Check correct include_digits
                    if not isinstance(inc_digits, bool):
                        raise \
                            ValueError("Include digits must be a boolean.")
                    self.include_digits = inc_digits
                    break
                except ValueError as valerr:
                    print(f"Invalid input. {str(valerr)}")
                except Exception as exc:
                    print(f"Error: {str(exc)}")
                except KeyboardInterrupt:
                    print("\nUser interrupted. Exiting...")
                    ex()
        # set default value
        elif self.setdefault:
            self.include_digits = self.setinclude_digits

    def get_include_digits(self) -> bool:
        """_summary_

        Returns:
            _type_: _description_
        """
        if self.include_digits is not None:
            return bool(self.include_digits)
        else:
            return True

    def set_include_special_chars(self, include_special_chars=None) -> None:
        """_summary_

        Args:
            include_special_chars (_type_): _description_

        Raises:
            ValueError: _description_
        """
        if include_special_chars is not None:
            try:
                # Check correct include_special_chars
                if not isinstance(include_special_chars, bool):
                    raise ValueError(
                        "Include special_chars must be a boolean.")
                self.include_special_chars = include_special_chars
            except (TypeError, ValueError, Exception) as err:
                print(f"Error: {str(err)}")
        # check if user set include_special_chars value in constructor
        elif self.is_set is True and not self.setdefault:
            # Check correct include_special_chars
            if not isinstance(self.setinclude_special_chars, bool):
                raise \
                    ValueError("Include special_chars must be a boolean.")
            self.include_special_chars = self.setinclude_special_chars
        # check if set default=False and user was not set
        # include_special_chars then get user input
        elif not self.setdefault and self.include_special_chars is None:
            # Input validation from user
            while True:
                try:
                    inc_special_chars = input(
                        "Include special_chars? (Default: [y]): "
                        ).lower()
                    if inc_special_chars == 'y' or not inc_special_chars:
                        inc_special_chars = True
                    elif inc_special_chars != 'y':
                        inc_special_chars = False
                    # Check correct include_special_chars
                    if not isinstance(inc_special_chars, bool):
                        raise \
                            ValueError(
                                "Include special_chars must be a boolean.")
                    self.include_special_chars = inc_special_chars
                    break
                except ValueError as valerr:
                    print(f"Invalid input. {str(valerr)}")
                except Exception as exc:
                    print(f"Error: {str(exc)}")
                except KeyboardInterrupt:
                    print("\nUser interrupted. Exiting...")
                    ex()
        # set default value
        elif self.setdefault:
            self.include_special_chars = self.setinclude_special_chars

    def get_include_special_chars(self) -> bool:
        """_summary_

        Returns:
            _type_: _description_
        """
        if self.include_special_chars is not None:
            return self.include_special_chars
        else:
            return True

    def prompt_password_criteria(self) -> None:
        """_summary_
        """
        self.set_length()
        self.set_include_uppercase()
        self.set_include_lowercase()
        self.set_include_digits()
        self.set_include_special_chars()

    def default_password_generation(self) -> str:
        """_summary_

        Returns:
            _type_: _description_
        """
        try:
            # Define character sets
            lowercase_letters = string.ascii_lowercase
            uppercase_letters = string.ascii_uppercase
            numbers = string.digits
            special_characters = string.punctuation

            # Ensure the password has at least one character from each set
            password = []
            password.append(random.choice(lowercase_letters))
            password.append(random.choice(uppercase_letters))
            password.append(random.choice(numbers))
            password.append(random.choice(special_characters))

            # Fill the remaining password length with random characters
            remaining_length = int(self.setlength) - 4
            password.extend(random.choice(
                lowercase_letters + uppercase_letters +
                numbers + special_characters
            ) for _ in range(remaining_length))

            # Shuffle the password to make it random
            random.shuffle(password)

            # Convert the password list to a string
            password = str(''.join(password))
            return password
        except ValueError as exc:
            print("Error:", str(exc))
            return ""
        except Exception as exc:
            print("An error occurred:", str(exc))
            return ""

    def generate_password(self) -> str:
        """Generate a secure password.

        Returns:
            str: Generated password.
        """
        try:
            if self.setdefault:
                self.password = self.default_password_generation()
                if self.check_default_password_requirements(self.password):
                    return self.password
                else:
                    raise UserWarning("Check requirements is failed")
            else:
                self.prompt_password_criteria()

                if self.length is None or self.include_uppercase is None \
                        or self.include_lowercase is None \
                        or self.include_digits is None \
                        or self.include_special_chars is None:
                    raise ValueError("Password criteria is not set.")
                if self.length < 16:
                    raise ValueError(self.value_err)
                # print(f"""
                # length: \t\t\t {self.length}
                # include_uppercase: \t\t {self.include_uppercase}
                # include_lowercase: \t\t {self.include_lowercase}
                # include_digits: \t\t {self.include_digits}
                # include_special_chars: \t\t {self.include_special_chars}
                # """)

                character_sets = []
                if self.include_uppercase:
                    character_sets.append(string.ascii_uppercase)
                if self.include_lowercase:
                    character_sets.append(string.ascii_lowercase)
                if self.include_digits:
                    character_sets.append(string.digits)
                if self.include_special_chars:
                    character_sets.append(string.punctuation)

                if not character_sets:
                    raise \
                        ValueError(
                            "At least one character set must be included.")

                password = []
                while len(password) < self.length:
                    character_set = random.choice(character_sets)
                    password.append(random.choice(character_set))

                random.shuffle(password)
                self.password = ''.join(password)
                if self.check_password_requirements(self.password):
                    return self.password
                else:
                    raise UserWarning("Check requirements is failed")
        except (ValueError, UserWarning, Exception) as err:
            print(f"Error: {err}")
            return ""

    def check_default_password_requirements(self, password):
        """
        Check if the password meets the specified requirements.

        Args:
            password (str): Password to check.

        Returns:
            bool: True if the password meets the requirements, False otherwise.
        """
        minimum_length = 16
        has_lowercase = any(char.islower() for char in str(password))
        has_uppercase = any(char.isupper() for char in str(password))
        has_digit = any(char.isdigit() for char in str(password))
        has_special_char = any(
            char in string.punctuation for char in str(password))

        return (
            len(password) >= minimum_length
            and has_lowercase
            and has_uppercase
            and has_digit
            and has_special_char
        )

    def check_password_requirements(self, password):
        """
        Check if the password meets the specified requirements.

        Args:
            password (str): Password to check.

        Returns:
            bool:   True if the password meets the requirements,
                    False otherwise.
        """
        if self.length is not None:
            minimum_length = self.length
        else:
            minimum_length = self.setlength
        # check requirements for including options
        # check include_lowercase is True
        if self.include_lowercase:
            has_lowercase = any(char.islower() for char in str(password))
        else:
            has_lowercase = True
        # check include_uppercase is True
        if self.include_uppercase:
            has_uppercase = any(char.isupper() for char in str(password))
        else:
            has_uppercase = True
        # check include_digits is True
        if self.include_digits:
            has_digit = any(char.isdigit() for char in str(password))
        else:
            has_digit = True
        # check include_special_chars is True
        if self.include_special_chars:
            has_special_char = any(
                char in string.punctuation for char in str(password))
        else:
            has_special_char = True

        return (
            len(password) >= minimum_length
            and has_lowercase
            and has_uppercase
            and has_digit
            and has_special_char
        )
