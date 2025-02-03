"""
Meaningful names to variables, functions, modules, and classes;
Styling blocks of code;
Commenting where necessary;
Keeping code neat and elegant.
"""


def calculate_discount(price, discount):
    """
    Calculate the valur of the discount
    prise - the total price of product in EUR
    discount - the weight of the discount (30% -> 0.3)
    :return: the discount price in EUR
    """
    discount_price = price * discount
    return discount_price
