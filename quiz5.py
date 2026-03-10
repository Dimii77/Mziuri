#1
class Ticket:
    def __init__(self, movie_name, price, quantity, language= "Geo"):
        self.movie_name = movie_name
        self.price = price
        self.quantity = quantity
        self.language = language

    def __str__(self):
        return f"Film: {self.movie_name} Price: {self.price} Quantity: {self.quantity} Language: {self.language}"

class User:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def __str__(self):
        return f"User: {self.name} Balance: {self.balance}"

    def deposit(self, amount):
        self.balance += amount
        print(f"{self.name} deposited {amount}")

    def __gt__(self, other):
        if isinstance(other, Ticket):
            return self.quantity > other.quantity
        elif isinstance(other, int, float):
            return self.quantity > other
        return NotImplemented

class User:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def buy_ticket(self, ticket , amount):
        total_price = ticket.price * amount
        if ticket.quantity > amount:
            print("Not enough tickets")
        elif self.balance < total.price:
            print("Not enough money")
        else:
            self.balance -= total_price
            ticket.quantity -= amount
            print("You bought {amount} tickets")
    def deposit(self, amount):
        self.balance += amount
        print(f"{self.name} deposited {amount}")


ticket1 = Ticket("Scream7", 15, 20)
ticket2 = Ticket("Avatar", 13, 8)
user1 = User("Benjamin Netanyahu", 100)

user1.deposit(20)
user1.buy_ticket(ticket1, 3)

print(user1)
print(ticket1)
print(ticket2)





