import unittest
import random
from credit_card_validator import credit_card_validator


class TestCase(unittest.TestCase):

    def test_credit_card_validator(self):
        for num in range(400000):
            # Generate a random credit card number
            credit_card_number = generate_random_credit_card()
            # Pass the generated credit card number to the validator function
            credit_card_validator(credit_card_number)
        for num in range(50):
            credit_card_number = test_other_prefixes()


def test_other_prefixes():
    for prefix in range(1, 10):
        if str(prefix) not in ['4', '5', '34', '37']:
            for length in range(14, 18):
                remaining_digits = "".join(
                    [str(random.randint(0, 9)) for _ in range(length - 1)])
                credit_card_number = str(prefix) + remaining_digits
                credit_card_validator(credit_card_number)


def generate_random_credit_card():
    # Generate a random prefix based on the rules for different issuers
    prefix = random.choice(
        ["4", "5" + str(random.randint(1, 5)), random.choice(["34", "37"]), str(random.randint(2221, 2720))])

    if prefix == "4":
        remaining_digits = "".join(
            # Length for Visa is 16
            [str(random.randint(0, 9)) for _ in range(18)])
    elif prefix.startswith("5"):
        remaining_digits = "".join([str(random.randint(0, 9)) for _ in range(
            16 - len(prefix))])  # Length for MasterCard is 16
    elif prefix.startswith("2"):
        remaining_digits = "".join([str(random.randint(0, 9)) for _ in range(
            16 - len(prefix))])  # Length for MasterCard is 16
    else:
        # Length for American Express is 15
        remaining_digits = "".join(
            [str(random.randint(0, 9)) for _ in range(12)])

    # Generate the remaining digits based on the length requirement for each issuer
    if prefix == "4":
        remaining_digits = "".join(
            [str(random.randint(0, 9)) for _ in range(15)])
    elif prefix == "":
        return ""
    elif prefix.startswith("5"):
        remaining_digits = "".join(
            [str(random.randint(0, 9)) for _ in range(15 - len(prefix))])
    elif prefix in ["34", "37"]:
        remaining_digits = "".join(
            [str(random.randint(0, 9)) for _ in range(13)])  # Length 14
    elif prefix.startswith("5"):
        remaining_digits = "".join(
            [str(random.randint(0, 9)) for _ in range(14)])  # Length 15
    elif prefix in ["34", "37"]:
        remaining_digits = "".join(
            [str(random.randint(0, 9)) for _ in range(16)])  # Length 17
    else:
        remaining_digits = "".join(
            # Default to length 14
            [str(random.randint(0, 9)) for _ in range(14)])

    return prefix + remaining_digits


if __name__ == '__main__':
    unittest.main()
