import pytest
from products import Product, NonStockedProduct, LimitedProduct
from promotion import PercentDiscount, SecondHalfPrice, ThirdOneFree

#test creating a normal product
def test_create_product():
    product = Product("MacBook Air M2", price=1450, quantity=100)
    assert product._name == "MacBook Air M2"
    assert product.price == 1450
    assert product.quantity == 100


#Test: Creating a product with an empty name should raise an exception
def test_empty_name():
    with pytest.raises(ValueError):
        Product("MacBook Air M2", price=-10, quantity=100)


#Test:Test: When a product reaches 0 quantity, it becomes inactive
def test_product_inactive():
    product = Product("Bose QuietComfort Earbuds", price=250, quantity=1)
    product.buy(1)
    assert not product.is_active()

#Test: Buying a product updates quantity correctly
def test_buy_product():
    product = Product("Google Pixel 7", price=500, quantity=10)
    cost = product.buy(3)
    assert product.quantity == 7
    assert cost == 1500


#Test: Buying more than available quantity should raise an exception
def test_buy_more_than_available():
    product = Product("MacBook Air M2", price=1450, quantity=2)
    with pytest.raises(ValueError):
        product.buy(5)

def test_zero_quantity_with_promotion():
    product = Product("Monitor", price=200, quantity=5)
    promo = PercentDiscount("10% Off", percent=10)
    product.set_promotion(promo)

    with pytest.raises(ValueError):
        product.buy(0)


def test_third_one_free_promotion():
    product = Product("macbook_air2", price=10,quantity=10)
    promo = ThirdOneFree("buy 2 get 3rd free")
    product.set_promotion(promo)


def test_second_half_price_promotion():
    product = Product("macbook_air2",price=50,quantity=10)
    promo = SecondHalfPrice("Buy 1 Get 2nd Half Price")
    product.set_promotion(promo)


def test_percent_discount_promotion():
    product = Product("Google Pixel 7",price=100,quantity=5)
    promo = PercentDiscount("20% off", percent=20)
    product.set_promotion(promo)
        











