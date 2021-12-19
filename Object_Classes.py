
import random


class Trait:
	
	priority = int
	filepath = str
	start_occurance = int
	end_occurance = int

	def __init__(self, name, layerName, occurances):
		self.name = name
		self.layerName = layerName
		self.occurances = occurances

	def setPriority(layerList):
		if type(layerList) == Layers:
			return layerList[self.layerName]

	def print(self):
		print(vars(self))



class Traits:
	
	def __init__(self):
		self.contents = []

	def add(self,trait):
		if type(trait) == Trait:
			self.contents.append(trait)
			
		else:
			print("error: not a trait")

	def printTraits(self):
		for trait in self.contents:
			trait.print()

	def sort(self):
		self.contents.sort(key=lambda x: (x.layerName, x.name))

	def updateBounds(self):
		self.sort()
		lastLayer = ""
		x = 1

		for i in self.contents:
			if lastLayer != i.layerName:
				x = 1
			
			i.start_occurance = x
			i.end_occurance = x + i.occurances - 1

			x = i.end_occurance + 1
			lastLayer = i.layerName

	def SelectRandTrait(self, layer):
		totalOccurances = 0

		for i in self.contents:
			if i.layerName == layer:
				totalOccurances += i.occurances 

		
		occurance = random.randint(1, totalOccurances)
			
		for k in self.contents:

			if (occurance >= k.start_occurance) and (occurance <= k.end_occurance) and (layer == k.layerName):
				return k




class Layer:

	def __init__(self,name,priority):
		self.name = name
		self.priority = priority

	def print(self):
		print(vars(self))

class Layers: 
	
	contents = []
	
	def __init__(self):
		pass
	
	def printLayers(self):
		for layer in self.contents:
			layer.print()

	def add(self,layer):
		if isinstance(layer.name, str):
			if isinstance(layer.priority, int):
				priorityExists = False
				for x in self.contents:
  					if x.priority == layer.priority:
  						priorityExists = True
				if priorityExists:
					print("error: attempted to add a priority that already exists")
				else:
					self.contents.append(layer)
			else:
				print("error: attempted to add a priority not of type 'int'")
			
		else:
			print("error: attempted to add a layer not of type 'string'")

	def sortByLayer(self):
		self.contents.sort(key=lambda x: (x.priority))


class NFT:

	def __init__(self, UID, traits = []):
		self.UID = UID
		self.traits = traits

	def show(self):
		pass

	def print(self):
		trait_list = "  Traits: "
		for i in self.traits.contents:
			trait_list += "(" + i.layerName + ":" +(i.name) + ")"
		
		print("UID: " + str(self.UID) + trait_list)
