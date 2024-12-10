from strategy1 import (
    Customer,
    Callable,
    LineItem,
    Decimal,
    Order
)

Promotion = Callable[[Order], Decimal]

promos: list[Promotion] = []

# Decorator register to avoid code repetition
def promotion(promo: Promotion) -> Promotion:
    promos.append(promo)
    return promo


def best_promo(order: Order) -> Decimal:
    """Compute the best discount available"""
    return max(promo(order) for promo in promos)


@promotion
def fidelity(order: Order) -> Decimal: 
    """5% discount for customers with 1000 or more fidelity points"""
    rate = Decimal('0.05')
    if order.customer.fidelity >= 20:
        return order.total() * rate
    return Decimal(0)


@promotion
def bulk_item(order: Order) -> Decimal:
    """10% discount for each LineItem with 20 or more units"""
    discount = Decimal(0)
    for item in order.cart:
        if item.quantity >= 20:
            discount += item.total() * Decimal('0.1')
    return discount


@promotion
def large_order(order: Order) -> Decimal:
    """7% discount for orders with 10 or more distinct items"""
    distinct_items = {item.product for item in order.cart}
    if len(distinct_items) >= 10:
        return order.total() * Decimal('0.07')
    return Decimal(0)


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