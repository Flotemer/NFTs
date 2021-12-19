
import random
import os
from PIL import Image

print(os.getcwd())
class Trait:
	

	start_occurance = int
	end_occurance = int

	def __init__(self, name, layerName, occurances, filePath):
		self.name = name
		self.layerName = layerName
		self.occurances = occurances
		self.filePath = filePath

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
		self.occurances = 0

	def print(self):
		print(vars(self))

	def update_occurances(self,traits):
		self.occurances = 0
		for trait in traits.contents:
			if trait.layerName == self.name:
				self.occurances += 1


class Layers: 
	
	contents = []
	totalCombinations = 1
	def __init__(self):
		pass
	
	def printLayers(self):
		for layer in self.contents:
			layer.print()

	def update_occurances(self,traits):
		self.totalCombinations = 1
		for layer in self.contents:
			layer.update_occurances(traits)
			self.totalCombinations *= layer.occurances

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
		self.hash = self.generate_hash()

	def generate_hash(self):
		string = ""
		for i in self.traits.contents:
			string += i.name
		#print(string)
		#print(hash(string))
		#print(hash(string))
		return hash(string)


	def show(self):
		pass

	def print(self):
		trait_list = "  Traits: "
		for i in self.traits.contents:
			trait_list += "(" + i.layerName + ":" +(i.name) + ")"
		
		print("UID: " + str(self.UID) + trait_list)

	def saveImage(self):
		nftImage = Image.new(mode = "RGBA", size = (600,600))
		for trait in self.traits.contents:
			filePath = trait.filePath
			nextLayerImage = Image.open(filePath).convert("RGBA")
			nftImage.alpha_composite(nextLayerImage)
		#nftImage.show()
		nftImage.save("/Users/harry/Documents/GitHub/NFTs/Output/" + str(self.UID) + ".png")
		print("NFT:"+ str(self.UID) + "---Saved")
