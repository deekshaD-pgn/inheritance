import json


class Person:

	def __init__(self, name, age=None):
		self.name = name
		self.age = age
		self.children = []


	def summary(self, depth=0):
		if self:
			child_text = "I have the following children:"
		else:
			child_text = "I have no children."	

		print(f"{' '*depth*4}My name is {self.name}, and my age is {self.age}, {child_text}")	
		for child in self.children:
			child.summary(depth=depth+1)

	def get_dict(self):
		return {
			'name': self.name,
			'age': self.age,
			'children': [child.get_dict() for child in self.children],
		}		


	def add_child(self, child):
		self.children.append(child)	


	def save(self, filename):
		with open(filename, 'w') as f:
			f.write(json.dumps(simon.get_dict()))

	@classmethod
	def load_data(cls, data):	
		person = cls(data['name'], age=data['age'])
		for child_data in data['children']:
			child = cls.load_data(child_data)
			person.add_child(child)
		return person	

	@classmethod
	def load(cls, filename):
		with open(filename, 'r') as f:
			data = json.loads(f.read())
		return cls.load_data(data)	


	def __bool__(self):
		return len(self.children) > 0


	def __str__(self):
		return f"Person called {self.name}"	




# simon = Person("simon")

# deeksha = Person("Deeksha")
# mushika = Person("mushika")
# yodan = Person("yodan")

# simon.add_child(deeksha)
# simon.add_child(mushika)
# simon.add_child(yodan)


# #mushika
# dunno = Person("Dunno")
# kushtav = Person("Kushtav")

# mushika.add_child(dunno)
# mushika.add_child(kushtav)

# #deeksha
# sanvi = Person("Sanvi")
# arnav = Person("Arnav")

# deeksha.add_child(sanvi)
# deeksha.add_child(arnav)

# #yodan
# ahana = Person("Ahana")
# veer = Person("Veer")

# yodan.add_child(ahana)
# yodan.add_child(veer)

p = Person.load('./family.json')

p.summary()

print(p.__class__.__name__)

	


