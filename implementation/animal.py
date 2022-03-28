class Animal:
	# set name and food as atrributes
	# let's say default inital food amount is 50
	def __init__(self, name):
		self.__name = name
		self.__food = 50

	# eat() method calls hidden method digest().
	def eat(self, food=0):
		print("ate food")
		self.__digest(food)

	# walk() method calls hidden method consume_food().
	def walk(self, distance=5):
		print("walked")

	# returns name
	def get_name(self):
		print("my name is", self.__name)
		return self.__name

	# digest() add food.
	# default food absortion rate is 1
	# default maximum food gauge is 100
	def __digest(self, food):
		if food > 99:
			print("I am full")
		else:
			self.food += food % 101
			print("food +"+str(food))

	# digest() substract food.
	# defualt food efficiency is 1
	def __consume_food(self, amount):
		if food-amount < 0:
			print("I am hungry")
		else:
			self.food -= amount
			print("food -"+str(amount))

# Dog inherits from Animal
class Dog(Animal):
	# new method woof
	# uses 10 food per each call
	def woof(self):
		print("woof woof")
		self.__consume_food(10)

	# overwrite digest()
	# dog's full absortion rate is 0.7
	def __diget(self, food):
		if food > 99:
			print("I am full")
		else:
			food *= 0.7
			self.food += food % 101
			print("food +"+str(food))

# Cat inherits from Animal
class Cat(Animal)
	# new method cat
	# uses

