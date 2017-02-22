class Charcter:
    hp = 0
    mp = 0
    attack = 0
    defense = 0
    name = ''
    level = 0
    exp = 0
    money = 0

    now_hp = 0
    now_mp = 0

    def show_status(self):
        print('---------------------')
        print(' Lv:' + str(self.level) + ' $:' + str(self.money))
        print(' NAME:' + str(self.name))
        print('')
        print(' HP:'+ str(self.now_hp) + '/' + str(self.hp) + ' MP:' + str(self.now_mp) + '/' + str(self.mp))
        print(' ATK:' + str(self.attack) + ' DEF:' + str(self.defense))
        print(' EXP:' + str(self.exp))
        print('---------------------')

    def show_status_mob(self):
        print('---------------------')
        print(' NAME:' + str(self.name))
        print(' HP:'+ str(self.now_hp) + '/' + str(self.hp) + ' MP:' + str(self.now_mp) + '/' + str(self.mp))
        print('---------------------')
