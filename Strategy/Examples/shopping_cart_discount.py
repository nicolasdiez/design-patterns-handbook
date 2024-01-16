from abc import ABC, abstractmethod

# Create the DiscountStrategy interface as the contract for the different discount strategies
class DiscountStrategy(ABC):

    @abstractmethod
    def apply_discount(self, total: float) -> float:
        pass

# Implement the 3 discount strategies (no discount / percentage discount / fixed amount discount)
class NoDiscount(DiscountStrategy):
    def apply_discount(self, total: float) -> float:
        return total
        
class PercentageDiscount(DiscountStrategy):
    def __init__(self, percentage: float) -> float:
        self.percentage = percentage
            
    def apply_discount(self, total: float) -> float:
        total = total * (1 - (self.percentage/100))
        return total

class FixedAmountDiscount(DiscountStrategy):
    def __init__(self, fixed_amount: float) -> float:
        self.fixed_amount = fixed_amount
        
    def apply_discount(self, total: float) -> float:
        total = total - self.fixed_amount
        return total

# Implement the shopping cart
class ShoppingCart:
    def __init__(self, discount_strategy: DiscountStrategy):
        # Initialize the shopping cart with the given discount strategy and an empty items dictionary (the shopping cart)
        self.discount_strategy = discount_strategy
        self.cart = {}

    def add_item(self, item: str, price: float):
        # Add the item with its price to the cart
        if item not in self.cart:
            self.cart[item] = price
        else:
            print(f'The {item} is already in the cart')

    def remove_item(self, item: str):
        # Remove the item from the cart
        item_removed = self.cart.pop(item)
        print(f'The item {item_removed} was removed from the cart')
        # del self.cart[item]

    def get_total(self) -> float:
        # Calculate and return the total price of the items in the cart
        total = 0.0
        for item in self.cart:
            total += self.cart[item]
            
        return total

    def get_total_after_discount(self) -> float:
        # Calculate and return the total price of the items in the cart after applying the discount
        total = self.get_total()
        
        total_after_discount = self.discount_strategy.apply_discount(total)
        
        return total_after_discount

# Test the implementation
if __name__ == "__main__":
    # Create a shopping cart with a discount strategy
    cart = ShoppingCart(PercentageDiscount(10))

    # Add a few items
    cart.add_item("Item 1", 10.0)
    cart.add_item("Item 2", 20.0)
    cart.add_item("Item 3", 30.0)

    # Calculate and print the total price before discount
    print("Total cart amount before discount:", cart.get_total())

    # Calculate and print the total price after applying the discount
    print("Total cart amount after discount:", cart.get_total_after_discount())
