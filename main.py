"""Simple math function"""

import double_it    # first awy to import
# from double_it import double_it


def prod_integers(
        num1: int,
        num2: int
        ) -> int:
    """_summary_

    Args:
        num1 (dict[str, int]): _description_
        num2 (list[int]): _description_

    Returns:
        int: _description_
    """

    x: int = num1 + num2

    result = double_it.double_int(x)

    return result


if __name__ == "__main__":
    print("inside main.py Dunder")
    print(prod_integers(1, 2))
