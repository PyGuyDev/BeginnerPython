# invest.py --> A program that tracks investment growth over a period of time


def invest(initial, apr, term):
    """This function takes three user inputed parameters to calculate the growth of an investment over a period of time."""  # noqa: E501
    n = 1
    while n <= term:
        invest_growth = float(initial) * float(apr)  # Calculates the grown amount  # noqa: E501
        new_principle = float(initial) + invest_growth  # Adds the grown amount back into the initial principle  # noqa: E501
        print(f"year {n}: ${new_principle:.2f}")
        initial = new_principle  # Resets the initial amount to the new amount
        n += 1  # Increases to the next year


invest(100, .05, 5)
