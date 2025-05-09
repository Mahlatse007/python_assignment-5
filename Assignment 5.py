#Activity 1
class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def get_title(self):
        return self.title

    def get_pages(self):
        return self.pages

book1 = Book('Welcome to the World', '23')
print(book1.get_title())

#Activity 2
class Animals:
    def __init__(self, animals):
        self.animals = animals

    def move(self):
        return self.animals


class Vehicles:
    def __init__(self, vehicles):
        self.vehicles = vehicles

    def move(self):
        return self.vehicles

Car = Vehicles('Driving')
Plane = Animals('Flying')

# print(f"{Car.move()}")
print(f"{Plane.move()}")