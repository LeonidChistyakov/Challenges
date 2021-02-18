prices = {
    "Strawberries": "$1.50",
    "Banana": "$0.50",
    "Mango": "$2.50",
    "Blueberries": "$1.00",
    "Raspberries": "$1.00",
    "Apple": "$1.75",
    "Pineapple": "$3.50",
}

class Smoothie:
    def __init__(self, ingridients):
        self.ingridients = ingridients
    def get_cost(self):
        cost = 0.0
        for fruit in self.ingridients:
            cost += float(prices[fruit].strip("$"))
        return "$%.2f" % cost
    def get_price(self):
        price = float(self.get_cost().strip("$")) * 2.5
        return "$%.2f" % price
    def get_name(self):
        name = str()
        self.ingridients.sort()
        for x in self.ingridients:
            if x.endswith("berries"):
                name += x.replace("berries", "berry") + " "
            else:
                name += x + " "
        if len(self.ingridients) > 1:
            name += "Fusion"
        else:
            name += "Smoothie"
        return name

s1 = Smoothie(["Banana", "Strawberries", "Apple", "Mango"])
print(s1.ingridients)
print(s1.get_cost())
print(s1.get_price())
print(s1.get_name())

s2 = Smoothie(["Pineapple"])
print(s2.ingridients)
print(s2.get_cost())
print(s2.get_price())
print(s2.get_name())
