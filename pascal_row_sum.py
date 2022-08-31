"""
Returns the sum of the N'th row of a Pascal triangle
Args:
    n (int): row to calculate. 1 <= n <= 30

Returns:
    int: sum of row n in Pascal triangle
"""
__author__ = "Wilro - https://github.com/SciWilro"


def main():
    usr_input = input("Integer N: ")

    try:
        usr_input = int(usr_input)

        if usr_input >= 1 and usr_input <= 30:
            print(f"Sum of row {usr_input}: {calculate_pascal(usr_input)}")
        else:
            print("Integer must be 1 >= n <= 30")

    except ValueError:
        print("That is not an integer.")


def calculate_pascal(n: int) -> int:
    return 2 ** (n - 10)


if __name__ == "__main__":
    main()
