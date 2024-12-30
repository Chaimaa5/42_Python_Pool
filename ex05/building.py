import sys
import string
def calculate_character_sums(input_string):
    """
    Calculate the sums of ASCII values for different character categories in a string.

    Args:
        input_string (str): The string to process.

    Returns:
        dict: A dictionary with the sums of upper-case, lower-case, punctuation,
              digits, and spaces.
    """
    upper_count = sum(1 for char in input_string if char.isupper())
    lower_count = sum(1 for char in input_string if char.islower())
    digit_count = sum(1 for char in input_string if char.isdigit())
    punctuation_count = sum(1 for char in input_string if char in string.punctuation)
    space_count = sum(1 for char in input_string if char.isspace())

    print(f"The text contains {len(input_string)} characters:")
    print(f"{upper_count} upper letters")
    print(f"{lower_count} lower letters")
    print(f"{punctuation_count} punctuation marks")
    print(f"{space_count} spaces")
    print(f"{digit_count} digits")

def main():
    """
    Main function to handle input validation and prompt the user if necessary.
    Raises:
        AssertionError: If more than one argument is provided.
    """
    try:
        if len(sys.argv) > 2:
            raise AssertionError("More than one argument is provided")
        elif len(sys.argv) == 2:
            input_string = sys.argv[1]
        else:
            input_string = input("What is the text to count?\n")


        calculate_character_sums(input_string)

    except AssertionError as e:
        print(f"AssertionError: {e}")


if __name__ == "__main__":
    main()