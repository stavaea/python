
class Garen:
    camp='demacia'
    def __init__(self,nickname,life_value,aggresivity):
        self.nickname=nickname
        self.life_value=life_value
        self.aggresivity=aggresivity

    def attack(self,enemy):
        enemy.life_value-=self.aggresivity


class Riven:
    camp = 'Noxus'

    def __init__(self, nickname, life_value, aggresivity):
        self.nickname = nickname
        self.life_value = life_value
        self.aggresivity = aggresivity

    def attack(self, enemy):
        enemy.life_value -= self.aggresivity

    def fire(self,enemy):
        enemy.life_value-=100

g1=Garen('草丛猥琐男',1000,100)
r1=Riven('猛男雯雯',200,500)

print(r1.life_value)
g1.attack(r1)
print(r1.life_value)

