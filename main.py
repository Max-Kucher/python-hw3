#!/usr/bin/python3
import argparse
import unittest
from src.password_generation import PasswordGenerator
from src.user_password_changer import UserPasswordChanger

from tests.test_password_generation import PasswordGeneratorTests
from tests.test_user_password_changer import UserPasswordChangerTests


def main():
    """
    _summary_

    Run script:
        python main.py --generate-password
        python main.py --change-user-pass

        python main.py --run-tests
        python main.py --generate-password --run-tests
    """
    parser = argparse.ArgumentParser(description="Password generator and changer")

    parser.add_argument(
        "--generate-password",
        required=False,
        dest="generate_password",
        action="store_true",
        help="Generate a random password",
    )
    parser.add_argument(
        "--run-tests",
        required=False,
        dest="run_tests",
        action="store_true",
        help="Run the all tests",
    )
    parser.add_argument(
        "--change-user-pass",
        required=False,
        dest="change_user_pass",
        action="store_true",
        help="Run the user password changing",
    )
    args = parser.parse_args()

    if args.generate_password:
        generator = PasswordGenerator()
        print(generator.hello())
        password = generator.generate_password()
        print("Generated password:", password)

    if args.change_user_pass:
        password_changer = UserPasswordChanger()
        print(password_changer.hello())
        password_changer.change_password()

    if args.run_tests:
        print(f'Running: {PasswordGeneratorTests.__doc__}')
        unittest.TextTestRunner().run(
            unittest.TestLoader().loadTestsFromTestCase(PasswordGeneratorTests)
        )
        print(f'Running: {UserPasswordChangerTests.__doc__}')
        unittest.TextTestRunner().run(
            unittest.TestLoader().loadTestsFromTestCase(
                UserPasswordChangerTests
            )
        )


if __name__ == "__main__":
    main()
