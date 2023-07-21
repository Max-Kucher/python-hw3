#!/usr/bin/python3
'''
## Task: Password change for Linux User

### Intro
user_password_changer.py:   Class object which changing user password with
                            secure options
author:                     Nakonechnyi Mikhail
date:                       04.07.23
version:                    1.1 (with OOP)
description of homework:


### Description

Your task is to develop a Python script that implements the Linux chpasswd
simulation

### Requirements:

    The program should prompt the user to enter a username.
    The program should check if user exist in system.
    The program should ask the user to input a password or generate a new one
        if not provided.
    The program should check the password against specified requirements
        minimum length
        presence of different character types (uppercase, lowercase, digits,
            special characters)
        any other criteria you specify.
    Change password for user
    The program should print the results, including the username, the original
        or generated password, and whether the password meets the requirements.

### Useful Links:
* https://www.maketecheasier.com/how-linux-stores-manages-user-passwords/
* https://www.section.io/
    engineering-education/how-to-execute-linux-commands-in-python/
* https://unix.stackexchange.com/
    questions/238180/execute-shell-commands-in-python


### Versions:
* 1.0 OOP realization
* 1.1 Fix for task algorithm
      -  https://github.com/DevOps01-ua/python01/blob/main/homeworks/img.png

'''
import getpass
import crypt
import subprocess
from sys import exit as ex

from src.password_generation import PasswordGenerator


class UserPasswordChanger:
    """_summary_
    """
    def __init__(self):
        """_summary_
        """
        self.minimal_default_length = 16
        self.description = """User password changer"""
        self.password_generator = PasswordGenerator(setdefault=False)

    def hello(self):
        """_summary_
        """
        return self.description

    def get_input(self) -> tuple:
        """
        Prompt the user to enter a username and a new password or generate one.

        Returns:
            tuple: Username and Password entered by the user.
        """
        try:
            while True:
                username = input("Enter the username: ")
                if not self.check_user_exist(username):
                    print(f"User '{username}' does not exist.")
                    continue

                password = getpass.getpass(
                    "Enter the new password (leave blank to generate one): "
                )

                if not password:
                    password = self.generate_password()
                elif len(password) < 16:
                    print("Password is too short. Must be at least 16.")
                    continue
                elif password != '' and \
                        not self.check_password_requirements(password):
                    print("The password does not meet the requirements.")
                    continue
                elif len(password) > 16:
                    self.password_generator.set_length(len(password))
                    self.password_generator.set_include_uppercase(True)
                    self.password_generator.set_include_lowercase(True)
                    self.password_generator.set_include_digits(True)
                    self.password_generator.set_include_special_chars(True)
                    if not self.check_password_requirements(password):
                        continue
                return username, password
        except KeyboardInterrupt:
            print("\nUser interrupted. Exiting...")
            ex()

    def check_user_exist(self, username):
        """
        Check if the user exists in the system.

        Args:
            username (str): Username to check.

        Returns:
            bool: True if the user exists, False otherwise.
        """
        try:
            subprocess.check_output(["id", username])
            return True
        except subprocess.CalledProcessError:
            return False

    def check_password_requirements(self, password):
        """
        Check if the password meets the specified requirements.
        """
        return self.password_generator.check_password_requirements(password)

    def generate_password(self):
        """
        Generate a random password using the PasswordGenerator class.

        Args:
            length (int): Length of the password. Defaults to 16.

        Returns:
            str: Generated password.
        """
        return self.password_generator.generate_password()

    def change_password(self, username=None, password=None):
        """
        Change the password for the specified username.

        Args:
            username (str): Username to change the password for.
            password (str, optional): New password. Defaults to None.
                If None, a random password will be generated.

        Returns:
            bool:
                True if the password is successfully changed, False otherwise.
        """
        username, password = self.get_input()

        password_hash = crypt.crypt(
            str(password),
            crypt.mksalt(crypt.METHOD_SHA512)
        )
        try:
            subprocess.check_call(
                ["sudo", "usermod", "-p", password_hash, str(username)]
            )
            print(f"Password {password} changed for user '{username}'.")
            return True
        except subprocess.CalledProcessError:
            print("Failed to change the password.")
            return False
