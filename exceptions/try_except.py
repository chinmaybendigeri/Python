def ask_for_int():
    while True:
        try:
            result = int(input("Enter a number: "))
        except:
            print("That is not a number! Please Try Again.")
            continue
        else:
            print("Its is number: {}".format(result))
            break
        finally:
            print("All done")


if __name__ == '__main__':
    ask_for_int()
