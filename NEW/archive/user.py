""" Class that contain information about user """
class User:
	
	
	def __init__(self, name, age, weight, height, gender, actv):
		self.name = name
		self.age = age
		self.weight = weight
		self.height = height
		self.gender = gender
		self.actv = actv
		
	@property
	def name(self):
		return self._name
	
	@property
	def age(self):
		return self._age
		
	@property
	def weight(self):
		return self._weight
	
	@property
	def height(self):
		return self._height
		
	@property
	def gender(self):
		return self._gender
	
	@property
	def actv(self):
		return self._actv
		
	@name.setter
	def name(self, name):
		self._name = name
		
	@age.setter
	def age(self, age):
		if age > 0 and age < 150:
			self._age = age
		else:
			raise Exception("Wrong age!")
			
	@weight.setter
	def weight(self, weight):
		if weight > 1 and weight < 550:
			self._weight = weight
		else:
			raise Exception("Wrong weight!")
			
	@height.setter
	def height(self, height):
		if height > 50 and height < 300:
			self._height = height
		else:
			raise Exception("Wrong weight!")
			
	@gender.setter
	def gender(self, gender):
		if gender == "male" or gender == "female":
			self._gender = gender
		else:
			raise Exception("Wrong gender!")
			
	@height.setter
	def actv(self, actv):
		if actv in [1.2, 1.375, 1.55, 1.7, 1.9]:
			self._actv = actv
		else:
			raise Exception("Wrong actv!")