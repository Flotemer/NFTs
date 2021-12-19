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

	trait = OCS.Trait(row[1][0], row[1][1],row[1][5],row[1][3])
	traits.add(trait)	
	#trait.print()
traits.updateBounds()



#---------------------------------------------------------------------------
#5. generate list of nfts with traits
#---------------------------------------------------------------------------


nfts = Gen.generateNFTs(100,layers,traits)




#---------------------------------------------------------------------------
#6. generate images from nft features
#---------------------------------------------------------------------------

for nft in nfts.values():
	nft.saveImage(pixelate = (10,10))



