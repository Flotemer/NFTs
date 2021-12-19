from PIL import Image

import numpy as np
import os

import Object_Classes as OCS

import pandas as pd
import csv 

import NFTGenerator as Gen

#---------------------------------------------------------------------------
#1. create objects that will hold our Layers and Traits
#---------------------------------------------------------------------------
layers = OCS.Layers()
traits = OCS.Traits()


#---------------------------------------------------------------------------
#2. create dfs and import information about layer and traits from setup file
#---------------------------------------------------------------------------
layers_df = pd.read_excel('NFTSetup.xlsx', sheet_name="Layers")
traits_df = pd.read_excel('NFTSetup.xlsx', sheet_name="Traits")


#---------------------------------------------------------------------------
#3. load layers from dataframes into layers list object
#---------------------------------------------------------------------------
for row in layers_df.iterrows():
	layer = OCS.Layer(row[1][0], row[1][1])
	layers.add(layer)


#---------------------------------------------------------------------------
#4. generate list of traits
#---------------------------------------------------------------------------
for row in traits_df.iterrows():

	trait = OCS.Trait(row[1][0], row[1][1],row[1][3])
	traits.add(trait)	
	#trait.print()
traits.updateBounds()

#---------------------------------------------------------------------------
#5. generate list of nfts with traits
#---------------------------------------------------------------------------


nfts = Gen.generateNFTs(29,layers,traits)
for nft in nfts:
	nft.print()









background = Image.open("testingbackground.png")
foreground = Image.open("Overlay.png")


class Sale_Receipts:
	def __init__(self, path = "", contents = []):
		self.source_folder = source_folder
		self.contents = contents

	def print_files(self):
		os.listdir(path=path)

a = Sales_Receipts(path = '')

final1 = Image.new(mode = "RGBA", size = background.size, color = (100,100,0,50))
#(mode = "RGB", size = (200, 200), color = (153, 153, 255))
final1.show()
final1.paste(background, (0,0), background)
final1.paste(foreground, (0,0), foreground)


