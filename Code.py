# Exercise 47
''' the main purpose of the ex is to create auto tests for it. 
They can be found in the 'test' folder and executed over
nosetests or nose2 '''

class Room:

	def __init__(self, name, description):
		self.name = name
		self.description = description
		self.paths = {}
		
	def go(self, direction):
		return self.paths.get(direction, None)
		
	def add_paths(self, paths):
		self.paths.update(paths)

#-*-coding: UTF-8-*-
# Exercise 43

from sys import exit
from random import randint

class Scene:

	def enter(self):
		print ("Not set. Create subclass and initialize enter()")
		exit(1)


class Engine:
	def __init__(self, scene_map):
		self.scene_map = scene_map
		
	def play(self):
		current_scene = self.scene_map.opening_scene()
		
		#while current_scene!= last_scene:
		next_scene_name = current_scene.enter()
		current_scene = self.scene_map.next_scene(next_scene_name)
			
		current_scene.enter()
		

class Death(Scene):
	quips = [
		"You're dead.",
		"You're like puppy. Moreover, dead",
		"GAMEOVER",
		]
		
	def enter(self):
		print (Death.quips[randint(0, len(self.quips) - 1)])
		exit(1)


		
class Lawn(Scene):

	def enter(self):
		print ("Arthur Dent is trying to shave at home in the morning")
		print ("Suddenly he sees the bulldozer in the mirror")
		print ("He rans out and lies down into the mud")
		print ("Mr Prosper asks: What are you doing?")
		
		print ("\n")
		
		print ("A. I'm just having a rest")
		print ("B. I'm going to kill you!")
		print ("C. That's my home, you are not going to destroy it!")
		
		action = input("> ")
		
		if action == "A" or "a" or "A." or "a.":
			
			print ("Mr Prosper thinks you're mad. He is calling police.")
			print ("The Earth is going to be destroyed soon.")
			print ("And you're along with it.")
			return 'death'
			
		elif action == "B" or "b" or "B." or "b.":
			print ("Mr Prosper decides to call police.")
			print ("They come to arrest you.")
			print ("The Earth is going to be destroyed soon.")
			print ("And you're along with it.")
			return 'death'
			
		elif action == "C" or "c" or "C." or "c.":
			print ("Mr Prosper is surprized.")
			print ("Didn't you see the notice two months ago?")
			print ("Ford Prefect appears and takes Arthur Dent to the close bar")
			return "bar"
			
		else:
			print ("You cannot do that!")
			return 'lawnbeforehouse'
			
class Bar(Scene):
	
	def enter(self):
		print ("Ford Prefect orders two pints of beer.")
		print ("""Barman wants to give a change, but Ford 
		says that the end of Earth is going to come in two minutes.""")
		print ("Arthur Dent wants to know how much time they've got.")
		
		time = "{}".format(randint(1, 13))
		quess = input("[keypad]> ")
		quesses = 0
		
		while guess != code and quesses < 10:
			if quesses == 9:
				print ("Just one more time!")
			print ("Zzzzzz... Wrong!")
			quesses+=1
			quess = input("[keypad]> ")
			
		if quess == code:
			print ("You're right.")
			print ("You should go outside and hitchhike an UFO.")
			return 'the_street'
			
		else:
			print ("You're wrong.")
			print ("While you've been trying to guess the time to live, the Earth is getting destroyed.")
			print ("Congrats.")
			return 'death'

class TheStreet(Scene):
	
	def enter(self):
		print ("Arthur Dent and Ford Prefect are chatting in the street.")
		print ("Suddenly, Arther sees his hous gets destroyed by bulldozer.")
		print ("He is going to stop it...")
		
		print ("\n")
		
		print ("Stop \ Allow")
		
		action = input("> ")
		
		if action == "Allow" or action == "allow":
			print ("Arthur Dent goes and safes his house but the planet gets destroyed.")
			return 'death'
			
		elif action == "Stop" or action == "stop":
			print ("Ford Prefect makes him to stop.")
			print ("He takes out a ... to hitchhike a UFO.")
			print ("It works out!..")
			return 'escape_pod'
			
		else:
			print ("You CAN'T do it!")
			return 'the_street'
			
class EscapePod(Scene):
	
	def enter(self):
		print ("Ford Prefect and Arthur Dent on the ship of aliens.")
		print ("But they're not welcome here...")
		print ("There are three doors. Which do you choose?")
		
		good_door = randint(1,4)
		quess = input("[door #]> ")
		
		if int(quess) != good_door:
			print ("You've come in and see an alien soldier.")
			print ("He takes you to the commander.")
			print ("The commander wants you to get off.")
			print ("The soldier opens the door to the space and kick you off")
			
			return 'death'
			
		else:
			print ("You're hidden somewhere in the pantry.")
			print ("You're safe so far")
			
			return 'finished'

class Finished(Scene):

	def enter(self):
		print ("You're alive. Good!")
		return 'finished'
	
			
class Map:
	
	scenes = {
		'death': Death(),
		'lawnbeforehouse': Lawn(),
		'bar': Bar(),
		'the_street': TheStreet(),
		'escape_pod': EscapePod(),
		'finished': Finished(),
		}
		
	def __init__(self, start_scene):
		self.start_scene = start_scene
		
	def next_scene(self, scene_name): 
		val = Map.scenes.get(scene_name)
		return val
		
	def opening_scene(self):
		return self.next_scene(self.start_scene)
		
		
a_map = Map('lawnbeforehouse')
a_game = Engine(a_map)
a_game.play()
		
			
#-*-coding: utf-8-*-
# Exercise 42

## Animal наследует object
class Animal(object):
	pass
	
## класс Dog наследует Animal
class Dog(Animal):
		# класс Dog комбинирует __init__ c параметрами self, name
		def __init__(self, name):
			# параметр name комбинирует атрибута класса
			self.name = name
			
## создается класс Cat, который наследует Animal
class Cat(Animal):
	# класс Cat комбинирует __init__ с параметрами self, name
	def __init__(self, name):
		# параметр name комбинирует атрибут класса
		self.name = name
		
## создается класс Person, наследующий ojbect

class Person(object):
	# класс Person комбинирует __init__ с параметрами self, name
	def __init__(self, name):
		# параметр name комбинирует атрибут класса
		self.name = name
	# Person - 	композиция животного некоторого вида
	self.pet = None
	
## создается класс Employee, который наследует Person
class Employee(Person):
		# класс Emlpoyee комбинирует метод __init__ с параметрами self, name, salary
		def __init__(self, name, salary):
			# композиция супер-класса от Employee
			super(Employee, self).__init__(name)
			# композиция атрибута класса
			# параметр salary комбинирует атрибут класса
			self.salary = salary
			
# класс Fish наследует object
class Fish(object):
	pass
	
# класс Salmon наследует класс Fish
class Salmno(Fish):
	pass
	
# класс Halibut наследует класс Fish	
class Halibut(Fish):
	pass
	
## rover наследует Dog
rover = Dog("Rover")

sat = Cat("sat")

## Мэри наследует Person
mary = Person("Mary")

# атрибут pet комбинирует экземпляр класса sat
mary.pet = sat

# создается frank как экземпляр класса Employee с параметрами "Frank", 120000
frank = Employess("Frank", 120000)

# из frank получается атрибут pet, а затем устанавливается равным rover
frank.pet = rover

# создается flipper как экземпляр класса Fish
flipper = Fish()

# создается crouse как экземпляр класса Salmon
crouse = Salmon()

# создается harry как экземпляр класса Halibut
harry = Halibut()


#-*-coding: utf-8-*-
# Exercise 39 (I & II)

# схема связей аббревиатур с названиями стран

countries = {
	u'Россия': 'RU',
	u'Германия': 'DE',
	u'Узбекистан': 'UZ',
	u'Зимбабве': 'ZW',
	u'Турция': 'TR'
	}
	
# создание базового набора стран и некоторых городов в них
cities = {
	'UZ': u'Газли',
	'TR': u'Сарыгерме',
	'DE': u'Мюнхен'
	}
	
# добавление некоторых городов
cities['ZW'] = u'Гверу'
cities['RU'] = u'Москва'

# вывод некоторых городов
print ('- ' * 10)
print (u'В стране ZW есть город: ', cities['ZW'])
print (u'В стране RU есть город: ', cities['RU'])

# вывод некоторых стран
print ('- ' * 10)
print (u'Аббревиатура Турции: ', countries[u'Турция'])
print (u'Аббревиатура Германии: ', countries[u'Германия'])

# выполняется с учетом страны и словаря городов
print ('- ' * 10)
print (u'В Турции есть город: ', cities[countries[u'Турция']])
print (u'В Германии есть город: ', cities[countries[u'Германия']])

# вывод аббревиатур всех стран
print ('- ' * 10)
for country, abbrev in countries.items():
	print (u'{} имеет аббревиатуру {}'.format(country, abbrev))
	
# вывод всех городов в странах
print('- ' * 10)
for abbrev, city in cities.items():
	print (u'В стране %s есть город %s' % (abbrev, city))
	
# а теперь сразу оба типа данных
print ("- " * 10)
for country, abbrev in countries.items():
	print (u'В стране %s используется аббревиатура %s и есть город %s' % (country, abbrev, cities[abbrev]))
	
print ("- " * 10)
# безопасное получение аббревиатуры страны, которая не представлена
country = countries.get(u'США', None)

if not country:
	print (u'Прошу прощения, США не обнаружено.')
	
# получение города со значением по умолчанию
city = cities.get('US', u'не существует')
print (u'В стране "US" есть город: %s' % city)

US_states = {
	'Alaska' : "Juneau",
	"Alabama" : "Montgomery", 
	"Arizona" : "Phoenix",
	"Arkanzas" : "Little Rock",
	"California" : "Sacramento",
	"Colorado" : "Denver", 
	"Connecticut" : "Hartford",
	"Delawere" : "Dover",
	"Florida" : "Tallahassee",
	"Georgia" : "Atlanta",
	"Hawaii" : "Honolulu",
	"Idaho" : "Boise",
	"Illinois" : "Springfield", 
	"Indiana" : "Indianapolis",
	"Iowa" : "Des Moines",
	"Kansas" : "Topeka", 
}

US_resol = {
	"AL": "Alabama",
	"AK": "Alaska",
	"AZ": "Arizona", 
}

US_abbrs = {
	'Alabama' : 'AL',
	'Alaska' : 'AK', 
	'Arizona' : 'AZ',
	'Arkanzas' : 'AR',
	'California' : 'CA',
	'Colorado' : 'CO',
	'Connecticut' : 'CT'
}

US_abbrs['Delawere'] = 'DE'
US_abbrs['Florida'] = 'FL'
US_abbrs['Georgia'] = 'GA'

print ("=" * 10+" "+"=" * 10)
print (f"{US_abbrs['Alabama']} capital is {US_states['Alabama']}")
print (f"{US_abbrs['Alaska']} capital is {US_states['Alaska']}")
print (f"{US_abbrs['Arizona']} capital is {US_states['Arizona']}")

print ("=" * 10+" "+"=" * 10 + "\n")
print (f"Attempt to find out the capital by abbreviation. The 'AL' implies {US_states[US_resol['AL']]}")
print (f"Attempt to find out the capital by abbreviation. The 'AK' implies {US_states[US_resol['AK']]}")
print (f"Attempt to find out the capital by abbreviation. The 'AK' implies {US_states[US_resol['AZ']]}")

print ("=" * 10+" "+"=" * 10 + "\n" )
for state, capital in US_states.items():
	print (f"{state} has capital named '{capital}'")
	
print ("\n" + "=" * 10+" "+"=" * 10 + "\n" )
for state, abbr in US_abbrs.items():
	print (f"{state} is shortened to '{abbr}'")
	
print ("\n" + "=" * 10+" "+"=" * 10 + "\n" )
for state, abbr in US_resol.items():
	print (f"Here again. The capital of {US_resol['AL']} is {US_states[US_resol['AL']]}")
	print (f"Here again. The capital of {US_resol['AK']} is {US_states[US_resol['AK']]}")
	print (f"Here again. The capital of {US_resol['AZ']} is {US_states[US_resol['AZ']]}")
	
print ("\n" + "- " * 10)
var = US_abbrs.get('NY', None)

if not var:
	print ('Sorry! The variable doesn\'t exist.')
	
State = US_states.get('NY', 'not exist')
print ('US has got the city: {}'.format(State))



# Exercise 38
#-*-coding: utf-8-*-

# создаем строковую переменную
ten_things = u'Apples Oranges Crows Telephone Light Sugar'

print (u"Погодите, тут меньше 10 объектов. Давайте исправим это.")

# разбиваем строковую переменную с помощью функции сплит на части с раздилителем ' ' (пробел)
stuff = ten_things.split(' ')

# создаем список литералом
more_stuff = ['Day', 'Night', 'Song', 'Frisbee', 'Corn', 'Banana', 'Girl', 'Boy']

# петля "пока не равно 10"
while len(stuff) != 10:
	# удаляем последнее значение из списка more_stuff присваем его переменной next_one
	next_one = more_stuff.pop()
	print (u'Добавляем: ', next_one)
	# добавляем переменную в список, объявленный ранее 
	stuff.append(next_one)
	print (u"Теперь у нас %d объектов." % len(stuff))
	
print (u"Итак: ", stuff)

print (u"Давайте кое-что сделаем с нашими объектами.")

print (stuff[1])
print (stuff[-1]) # хм! интересно
print (stuff.pop())
# снова из списка делаем строку
print (' '.join(stuff)) # что? круто!

#  с помощью функции join объединяем 3 и 4 кардинальные значения в списке stuff
print ("#".join(stuff[3:8])) # просто супер!

print (stuff)

# Excercise 36

from sys import exit

def gold_room():
	print ("A lot of gold. How much would you take?")

	next = input("> ")

	if 	next.isdigit():
		if int(next) < 50:
			print ("Awesome! You're not greedy, you won!")
			exit(0)
		else:
			print ("You're sneaky!")	
	else:
		print ("You should input a digit.")

def bear_room():
	print ('''Here is a bear.
	It has a pot with honey.
	It closes the exit. How to move?''')
	bear_moved = False

	while True:
		next = input("> ")

		if "take honey" in next:
			dead("First choice")
		elif "yell at it" in next and not bear_moved:
			print ("Try more")
			bear_moved = True
		elif "move it" in next and bear_moved:
			dead("Bear kills u")
		elif "open the door" in next and bear_moved:
			gold_room()
		else:
			print ("Don't have a clue")

def cthulhu_room():
	print ('''Ctulhu is lookgin' at you.
		Run away or just stay?''')

	next = input("> ")

	if "run" in next:
		start()
	elif "stay" in next:
		dead("Not a choice!")
	else:
		cthulhu_room()

def dead(why):
	print (why, "Excellent!")
	exit(0)

def start():
	print ('''You're in the dark room.
		There are two doors.
		Which do you choose?''')

	next = input("> ")

	if next == "left":
		bear_room()
	elif next == "right":
		cthulhu_room()
	else:
		dead("You have to choose, man. Or it's gonna done by default...")

start()		


#-*-coding: utf-8-*-
# Exercise 34

import codecs, sys
outf = codecs.getwriter('cp866')(sys.stdout, errors = 'replace')
sys.stdout = outf

from sys import exit

def gold_room():
	print (u"Здесь полно золота. Сколько кг ты унесешь?")

	next = input("> ").decode(sys.stdin.encoding or locale.getpreferredencoding(True))

	if "0" in next or "1" in next:
		how_much = int(next)
	else:
		dead(u"Эй, надо ввести число!")

	if how_much < 50:
		print (u"Шикарно! Ты не жадный, поэтому выигрываешь!")
		exit(0)
	else:
		dead(u"Ах ты жадина!")

def bear_room():
	print (u"Здесь сидит медведь.")
	print (u"У медведя бочка с медом.")
	print (u"Медведь закрыл собой дверь выхода.")
	print (u"Как переместить медведя? Отобрать мед или подразнить медведя?")
	bear_moved = False

	while True:
		next = input("> ")
		if next == u"отобрать мед":
			dead (u"Медведь посмотрел на тебя и ударил лапой по лицу.")
		elif next == u"подразнить медведя" and not bear_moved:
			print (u"Медведь отошел от двери. Вы можете войти в нее. Подразнить медведя и ваойти дверь?")
			bear_moved = True
		elif next == u"подразнить медведя" and bear_moved:
			dead (u"Медведь разозлился и откусил тебе ногу.")
		elif next == u"войти в дверь" and bear_moved:
			gold_room()
		else:
			print (u"Понятия не имею, что происходит.")


def cthulhu_room():
	print (u"На вас смотрит великий и ужасный Ктулху.")
	print (u"Он смотрит на тебя, и ты начинаешь сходить с ума.")
	print (u"Убежать или съесть свою голову?")

	next = input("> ").decode(sys.stdin.encoding or locale.getpreferredencoding(True))

	if u"убежать" in next:
		start()
	elif u"съесть свою голову" in next:
		dead(u"Хм, а это даже и вкусно!")
	else:
		cthulhu_room

def dead(why):
	print (why, u"Великолепно!")
	exit(0)

def start():
	print (u"Ты в темной комнате.")
	print (u"Отсюда ведут две двери, налево и направо.")
	print (u"Куда ты повернешь?")

	next = input("> ").decode(sys.stdin.encoding or locale.getpreferredencoding(True))

	if next == u"налево":
		bear_room
	elif next == "направо":
		cthulhu_room
	else:
		dead(u"Ты ходишь из комнаты в комнату, пока не умираешь с голоду.")


start()	

#-*-coding: utf-8-*-
# Exercise 33

'''
i = 0
number = []

while i < 6:
    print (u"Вверху значение i равно %d" % i)
    number.append(i)

    i +=1
    print (u"Текущие значения: ", number)
    print (u"Внизу значение i равно %d" % i)

print (u'Значения: ')

for num in number:
	print (num)

# part II 

def number(a, b):
	i = 0
	list_=[]
	while i < a:
		print (u"Вверху значение i равно %d" % i)
		list_.append(i)

		i+=b
		print (u"Текущие значения: ", list_)
		print (u"Внизу значение i равно %d" % i)

	print (u"Значения: ")

	for num in list_:
		print (num)

print (u"Введите число")
a = input("> ")

print (u"Введите шаг")
b = input("> ")

number (int(a), int(b))

# part III

'''
def number(a, b):
	list_=[]
	for i in range (0, a, b):
		print (u"Вверху значение i равно %d" % i)
		list_.append(i)
		print (u"Текущие значения: ", list_)
		print (u"Внизу значение i равно %d" % i)

	print (u"Значения: ")

	for num in list_:
		print (num)

print (u"Введите число")
a = input("> ")

print (u"Введите шаг")
b = input("> ")

number (int(a), int(b))

#-*-coding: utf-8-*-
# Exercise 32

the_count = [1, 2, 3, 4, 5,]
fruits = [u'яблоко', u'апельсин', u'персик', u'абрикос']
change = [1, '25', 2, '50', 3, '75']

# цикл for первого типа обрабатывает список
for number in the_count:
    print (u'Счетчик %d' % number)

# то же, что и выше
for fruit in fruits:
    print (u'Фрукт: %s' % fruit)

# также можно обрабатывать смешанные списки
# обратите внимание, что используется оператор %r, так как неизвестен тип значения
for i in change:
	print (u"Я получил %r" % i)

# также мы можем создавать списки, начнем с пустого
elements = []

# затем используетсяd функция range для ограничения диапазона
for i in range(0, 6):
	print (u"Добавление %d в список." % i)

	# append - функция для добавления элементов в список
	elements.append(i)


# теперь мы их выводим
for i in elements:
	print (u'Номер элемента: %d' % i)
