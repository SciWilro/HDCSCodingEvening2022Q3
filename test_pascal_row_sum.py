from pascal_row_sum import calculate_pascal


def main():
    test_calculate_pascal()


def test_calculate_pascal():
    assert calculate_pascal(5) == 16
    assert calculate_pascal(8) == 128
    assert calculate_pascal(30) == 536870912


if __name__ == "__main__":
    main()
