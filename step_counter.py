class NegativeValueError(Exception):
    pass


def steps_to_miles(steps):
    if not isinstance(steps, int):
        raise ValueError("Exception: Non-Numeric Value Entered.")
    if steps < 0:
        raise NegativeValueError("Exception: Negative Step Count Entered.")
    miles = steps / 2000
    print(f"{miles:.2f} miles")


def main():
    while True:
        try:
            steps = int(input("Enter # of Steps:> "))
            steps_to_miles(steps)
        except ValueError:
            print("Exception: Non-Numeric Value Entered.")
        except NegativeValueError as e:
            print(e)


if __name__ == "__main__":
    main()
