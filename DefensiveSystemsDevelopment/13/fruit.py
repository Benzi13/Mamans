class AppleBasket:
    def __init__(self, apple_color: str, apple_quantity: int) -> None:
        self.apple_color = apple_color
        self.apple_quantity = apple_quantity

    def increase(self) -> None:
        self.apple_quantity += 1

    def __str__(self) -> str:
        return f"A basket of {self.apple_quantity} {self.apple_color} apples."

class GreenAppleBasket(AppleBasket):
    def __init__(self, apple_quantity) -> None:
        super().__init__("Green", apple_quantity)

def main():
    basket1 = AppleBasket("red", 4)
    basket2 = AppleBasket("blue", 50)
    green_basket = GreenAppleBasket(25)

    print(basket1)
    print(basket2)
    print(green_basket)

    basket1.increase()
    basket2.increase()
    green_basket.increase()

    print(basket1)
    print(basket2)
    print(green_basket)


if __name__ == "__main__":
    main()
