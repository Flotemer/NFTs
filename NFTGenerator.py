
import Object_Classes as Objects

def generateNFTs(numberToCreate, layers, traits,failsAllowed = 100000):
	
	layers.update_occurances(traits)


	NFTs = {}

	#ensure layers are sorted by priorities
	layers.sortByLayer()
	k = 1

	#loop until max total combinations is reached OR number to create is reached
	while k <= numberToCreate and k <= layers.totalCombinations:
			
		NFTtraits = Objects.Traits()
		for i in layers.contents:
			layer = i.name
			
			trait = traits.SelectRandTrait(layer)
			NFTtraits.add(trait)
			

		nft = Objects.NFT(k,NFTtraits)
		
		if nft.hash not in NFTs:
			NFTs[nft.hash] = nft
			k += 1




	return NFTs

	