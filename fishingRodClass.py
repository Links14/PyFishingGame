# Trevor Loth
# 7/8/24


class FishingRod:
    def __init__(self, stren = 1, dur = 10, rarity = "common"):
        self._rarity = rarity
        self._strength = stren
        self._durability = dur

    def get_rarity(self):
        return self._rarity

    def get_strength(self):
        return self._strength

    def get_durability(self):
        return self._durability
    
    
class Fish:
    def __init__(self, stren, rarity, catchF):
        self._rarity = rarity
        self._strength = stren
        self._catchFactor = catchF
        
    def get_rarity(self):
        return self._rarity

    def get_strength(self):
        return self._strength

    def get_durability(self):
        return self._catchFactor        



rods = {"goldenrod" : {"strength":100, "durability":100, "rarity":"epic"}}
print(rods["goldenrod"]["strength"])

goldenrod = FishingRod(100, 100, "epic")
print(goldenrod.get_strength())




rarityDict = {"common":0, "uncommon":1, "rare":2, "epic":3, "legendary":4, "mythical":5}


