class SpiderMan:
    def attack(self) -> str:
        return print("Web Shooter!")
    
    def defend(self) -> str:
        return print("Spider Sense!")

class BlackWidow:
    def attack(self) -> str:
        return print("Widow's Bite!")
    def defend(self) -> str:
        return print("Acrobatic Dodge!")    


def battle_sequence(spider)->None:
    spider.attack()
    spider.defend()




# Don't modify the code below
spider_man = SpiderMan()
black_widow = BlackWidow()

battle_sequence(spider_man)
battle_sequence(black_widow)
