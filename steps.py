#THIS IS MY NEW SUBMISSION: I RENAMED MY "steps_convert" FUNCTION TO "feet_to_steps"
def feet_to_steps(feet):
    steps = feet / 2.5
    steps = int(steps)
    return steps


def main():
    feet = float(input("Please enter the distance travelled in feet: "))
    steps = feet_to_steps(feet)
    print(f"{steps} steps")


if __name__ == "__main__":
    main()
