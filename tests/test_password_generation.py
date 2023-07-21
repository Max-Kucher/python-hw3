#!/usr/bin/python3
import unittest
# from random import randint
import string
from advanced.password_generation import PasswordGenerator


class PasswordGeneratorTests(unittest.TestCase):
    """Test case class for PasswordGenerator."""

    def test_contains_uppercase_letter_default(self):
        """
        Test if generated password contains at least one uppercase letter.
        """
        generator = PasswordGenerator(setdefault=True)
        password = generator.generate_password()
        self.assertTrue(any(
            char in string.ascii_uppercase for char in str(password)
        ))

    def test_contains_uppercase_if_set_true(self):
        """
        Test if generated password contains at least one uppercase letter.
        """
        generator = PasswordGenerator(
            is_set=True,
            setdefault=False,
            setlength=16,
            setinclude_uppercase=True,
            setinclude_lowercase=True,
            setinclude_digits=True,
            setinclude_special_chars=True,
            )
        password = generator.generate_password()
        self.assertTrue(any(
            char in string.ascii_uppercase for char in str(password)
        ))

    def test_contains_uppercase_if_set_not_true(self):
        """
        Test if generated password contains at least one uppercase letter.
        """
        generator = PasswordGenerator(
            is_set=True,
            setdefault=False,
            setlength=16,
            setinclude_uppercase=False,
            setinclude_lowercase=True,
            setinclude_digits=True,
            setinclude_special_chars=True,
            )
        password = generator.generate_password()
        self.assertFalse(any(
            char in string.ascii_uppercase for char in str(password)
        ))

    def test_contains_lowercase_letter_default(self):
        """
        Test if generated password contains at least one lowercase letter.
        """
        generator = PasswordGenerator(setdefault=True)
        password = generator.generate_password()
        self.assertTrue(any(
            char in string.ascii_lowercase for char in str(password)
        ))

    def test_contains_lowercase_if_set_true(self):
        """
        Test if generated password contains at least one lowercase letter.
        """
        generator = PasswordGenerator(
            is_set=True,
            setdefault=False,
            setlength=16,
            setinclude_uppercase=True,
            setinclude_lowercase=True,
            setinclude_digits=True,
            setinclude_special_chars=True,
            )
        password = generator.generate_password()
        self.assertTrue(any(
            char in string.ascii_lowercase for char in str(password)
        ))

    def test_contains_lowercase_if_set_not_true(self):
        """
        Test if generated password contains at least one lowercase letter.
        """
        generator = PasswordGenerator(
            is_set=True,
            setdefault=False,
            setlength=16,
            setinclude_uppercase=True,
            setinclude_lowercase=False,
            setinclude_digits=True,
            setinclude_special_chars=True,
            )
        password = generator.generate_password()
        self.assertFalse(any(
            char in string.ascii_lowercase for char in str(password)
        ))

    def test_contains_number_default(self):
        """
        Test if generated password contains at least one number.
        """
        generator = PasswordGenerator(setdefault=True)
        password = generator.generate_password()
        self.assertTrue(any(
            char in string.digits for char in str(password)
        ))

    def test_contains_number_if_set_true(self):
        """
        Test if generated password contains at least one number.
        """
        generator = PasswordGenerator(
            is_set=True,
            setdefault=False,
            setlength=16,
            setinclude_uppercase=True,
            setinclude_lowercase=True,
            setinclude_digits=True,
            setinclude_special_chars=True,
            )
        password = generator.generate_password()
        self.assertTrue(any(
            char in string.digits for char in str(password)
        ))

    def test_contains_number_if_set_not_true(self):
        """
        Test if generated password contains at least one number.
        """
        generator = PasswordGenerator(
            is_set=True,
            setdefault=False,
            setlength=16,
            setinclude_uppercase=True,
            setinclude_lowercase=True,
            setinclude_digits=False,
            setinclude_special_chars=True,
            )
        password = generator.generate_password()
        self.assertFalse(any(
            char in string.digits for char in str(password)
        ))

    def test_contains_special_character_default(self):
        """
        Test if generated password contains at least one special character.
        """
        generator = PasswordGenerator(setdefault=True)
        password = generator.generate_password()
        self.assertTrue(any(
            char in string.punctuation for char in str(password)
        ))

    def test_contains_special_character_if_set_true(self):
        """
        Test if generated password contains at least one special character.
        """
        generator = PasswordGenerator(
            is_set=True,
            setdefault=False,
            setlength=16,
            setinclude_uppercase=True,
            setinclude_lowercase=True,
            setinclude_digits=True,
            setinclude_special_chars=True,
            )
        password = generator.generate_password()
        self.assertTrue(any(
            char in string.punctuation for char in str(password)
        ))

    def test_contains_special_character_if_set_not_true(self):
        """
        Test if generated password contains at least one special character.
        """
        generator = PasswordGenerator(
            is_set=True,
            setdefault=False,
            setlength=16,
            setinclude_uppercase=True,
            setinclude_lowercase=True,
            setinclude_digits=True,
            setinclude_special_chars=False,
            )
        password = generator.generate_password()
        self.assertFalse(any(
            char in string.punctuation for char in str(password)
        ))

    def test_minimum_length(self):
        """
        Test if ValueError is raised for passwords with length less than 16.
        """
        generator = PasswordGenerator(
            is_set=True,
            setdefault=False,
            setlength=16,
            setinclude_uppercase=True,
            setinclude_lowercase=True,
            setinclude_digits=True,
            setinclude_special_chars=True,
        )
        with self.assertRaises(ValueError) as context:
            generator.set_length(15)
        self.assertEqual(
            str(context.exception),
            generator.get_var_length_error()
        )
        generator.generate_password()

    def test_negative_input_validation(self):
        """
        Test if ValueError is raised for negative password length.
        """
        generator = PasswordGenerator(
            is_set=True,
            setdefault=False,
            setlength=16,
            setinclude_uppercase=True,
            setinclude_lowercase=True,
            setinclude_digits=True,
            setinclude_special_chars=True,
        )
        with self.assertRaises(ValueError) as context:
            generator.set_length(-15)
        self.assertEqual(
            str(context.exception),
            generator.get_var_length_error()
        )
        generator.generate_password()

    def test_float_input_validation(self):
        """
        Test if TypeError is raised for float password length.
        """
        generator = PasswordGenerator(
            is_set=True,
            setdefault=False,
            setlength=16,
            setinclude_uppercase=True,
            setinclude_lowercase=True,
            setinclude_digits=True,
            setinclude_special_chars=True,
        )
        with self.assertRaises(TypeError) as context:
            generator.set_length(16.3)
        self.assertEqual(
            str(context.exception),
            generator.get_type_length_error()
        )
        generator.generate_password()

    def test_string_input_validation(self):
        """
        Test if TypeError is raised for string password length.
        """
        generator = PasswordGenerator(
            is_set=True,
            setdefault=False,
            setlength=16,
            setinclude_uppercase=True,
            setinclude_lowercase=True,
            setinclude_digits=True,
            setinclude_special_chars=True,
        )
        with self.assertRaises(TypeError) as context:
            generator.set_length("abc")
        self.assertEqual(
            str(context.exception),
            generator.get_type_length_error()
        )
        generator.generate_password()

    # def test_generated_password_length(self):
    #     generator = PasswordGenerator(
    #         is_set=True,
    #         setdefault=False,
    #         setlength=16,
    #         setinclude_uppercase=True,
    #         setinclude_lowercase=True,
    #         setinclude_digits=True,
    #         setinclude_special_chars=True,
    #     )
    #     generator.set_length(randint(16, 32))
    #     for _ in range(100):
    #         password = generator.generate_password()
    #         self.assertGreaterEqual(len(password), 16)

    def test_password_uniqueness(self):
        """
        Test if generated passwords are unique.
        """
        generator = PasswordGenerator(setdefault=True)
        generated_passwords = set()
        for _ in range(100):
            password = generator.generate_password()
            self.assertNotIn(password, generated_passwords)
            generated_passwords.add(password)
