import inspect

import promotions
from strategy1 import (
    Customer,
    LineItem,
    Decimal,
    Order
)

# Another way to avoid code duplication
promos = [
    func for _, func in inspect.getmembers(promotions, inspect.isfunction)
]


def best_promo(order: Order) -> Decimal:
    """Compute the best discount available"""
    return max(promo(order) for promo in promos)


if __name__ == '__main__':
    joe = Customer('John Doe', 0)
    ann = Customer('Ann Smith', 1100)
    cart = (
        LineItem('banana', 4, Decimal('.5')),
        LineItem('apple', 10, Decimal('1.5')),
        LineItem('watermelon', 5, Decimal(5))
    )

    banana_cart = (
        LineItem('banana', 30, Decimal('.5')),
        LineItem('apple', 10, Decimal('1.5'))
    )
    long_cart = tuple(
        LineItem(str(sku), 1, Decimal(1)) for sku in range(10)
    )
    print(Order(joe, cart, best_promo))
    print(Order(ann, cart, best_promo))
    print(Order(joe, banana_cart, best_promo))
    print(Order(joe, long_cart, best_promo))