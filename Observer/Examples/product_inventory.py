from abc import ABC, abstractmethod


# Observer = Consumer
class Observer(ABC):
    @abstractmethod
    def update(self, product_name: str, new_stock: int) -> None:
        pass

# Subject = Producer
class Subject(ABC):
    @abstractmethod
    def attach(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def detach(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def notify(self) -> None:
        pass


class StoreManager(Observer):
    def __init__(self, name: str):
        self._name = name

    def update(self, product_name: str, new_stock: int) -> None:
        # method to display a message indicating the stock level update
        print(f'{self._name} - New stock for {product_name}: {new_stock}')


class Inventory(Subject):
    def __init__(self):
        self._observers = []
        self._products = {}

    def attach(self, observer: Observer) -> None:
        # method to add an observer
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        # method to remove an observer
        self._observers.remove(observer)

    def notify(self, product_name: str, new_stock: int) -> None:
        # method to notify all observers
        for observer in self._observers:
            observer.update(product_name, new_stock)

    def update_stock(self, product_name: str, new_stock: int) -> None:
        # method to update the stock level and call notify if necessary (only when stock decreases)
        if (new_stock != self._products[product_name]):
            if (new_stock < self._products[product_name]):
                self.notify(product_name, new_stock)
            
            self._products[product_name] = new_stock


if __name__ == "__main__":
    inventory = Inventory()
    
    # Adding products to inventory
    inventory._products = {
        "Apples": 10,
        "Oranges": 25,
        "Bananas": 50,
    }
    
    manager1 = StoreManager("Alice")
    manager2 = StoreManager("Bob")
    
    # Attaching store managers
    inventory.attach(manager1)
    inventory.attach(manager2)
    
    # Updating stock levels and checking notifications
    print("Stock level update 1:")
    inventory.update_stock("Apples", 5)  # Should notify both managers
    print("\nStock level update 2:")
    inventory.update_stock("Bananas", 60)  # Should not notify as stock level increased
    
    # Detaching manager1
    inventory.detach(manager1)
    
    # Updating stock levels again
    print("\nStock level update 3:")
    inventory.update_stock("Oranges", 20)  # Should notify only manager2
