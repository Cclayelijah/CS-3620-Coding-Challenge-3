from part4 import Computer
from part4 import Laptop
from part4 import Desktop


# Elijah Cannon

def studentDiscount(x):
    return x - x / 10

def regularBuyerDiscount(x):
    return x - x / 5

# Part 1
print("Part 1:")
price = 30
result = regularBuyerDiscount(studentDiscount(price))
print(result)

# Part 2
print("Part 2:")
result = (lambda x: x * (x+5) ** 2)(5)
print(result)

# Part 3
print("Part 3:")
prices = [32, 43, 13, 14, 84, 27, 54, 35, 64]
result = list(map(lambda x: x - x / 10, prices))
print(result)

# Part 4
print("Part 4:")
server = Computer()
laptop = Laptop()
pc = Desktop()

server.getspecs(4300, 64)
server.displayspecs()

laptop.getspecs(1700, 16, 44)
laptop.displayspecs()

pc.getspecs(2500, 32, 8)
pc.displayspecs()

# Part 5
class Number:
    def __init__(self, x):
        self.x = x
    def __mul__(self, other):
        x = self.x + other
        return x

print("Part 5:")
num = Number(5)
result = num * 5
print ("5 * 5 = " + str(result))