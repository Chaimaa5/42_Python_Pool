import sys
from ft_filter import ft_filter
def main():
    """
    Main function to handle input validation and prompt the user if necessary.
    Raises:
        AssertionError: In case of error.
    """
    try:
        if len(sys.argv) == 3:

            try:
                Number = int(sys.argv[2])
            except ValueError:
                raise AssertionError("the arguments are bad")

            try:
                String = sys.argv[1]
                if not isinstance(String, str):
                    raise AssertionError("the arguments are bad")
            except ValueError:
                raise AssertionError("the arguments are bad")

            dict = String.split()
            filtered = ft_filter(lambda word: len(word) > Number, dict)
            filtered_words = list(filtered)
            print(filtered_words)


        else:
            raise AssertionError("the arguments are bad!")

    
    except AssertionError as e:
        print(f"AssertionError: {e}")


if __name__ == "__main__":
    main()