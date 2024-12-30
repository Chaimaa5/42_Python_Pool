if __name__ == "__main__":
    import sys
    try:
        if(len(sys.argv) == 2):
            if(type(sys.argv[1]) == int or sys.argv[1].lstrip('-').isdigit()):
                if(int(sys.argv[1]) % 2 == 0):
                    print("I'm Even.")
                else:
                    print("I'm Odd.")
            else:
                print("AssertionError: argument is not an integer.")
        elif(len(sys.argv) > 2):
            print("AssertionError: more than one argument is provided.")
    except:
        print("AssertionError: argument is not an integer.")

