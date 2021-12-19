
import Object_Classes as Objects

def generateNFTs(numberToCreate, layers, traits):
	
	NFTs = []

	#ensure layers are sorted by priorities
	layers.sortByLayer()
	k = 1
	while k <= numberToCreate:
		NFTtraits = Objects.Traits()
		for i in layers.contents:
			layer = i.name
			
			trait = traits.SelectRandTrait(layer)
			NFTtraits.add(trait)
			

		nft = Objects.NFT(k,NFTtraits)
		NFTs.append(nft)
		k += 1

	return NFTs