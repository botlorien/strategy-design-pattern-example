from best_strategy3 import promotion, promos, best_promo
from strategy1 import (
    Customer,
    Callable,
    LineItem,
    Decimal,
    Order
)

@promotion
def general(order: Order) -> Decimal:
    """20% discount for total order"""
    return order.total() * Decimal('0.06')


if __name__ == '__main__':
    print(promos)
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