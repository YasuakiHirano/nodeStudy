import charcter

monster_name = ['スライム', 'ゴブリン', 'スパイダー', 'ゾンビ']
monster_hp = [5,15,10,20]
monster_mp = [0,0,0,0]
monster_atk = [2,3,3,5]
monster_dfn = [0,2,1,5]
monster_exp = [3,6,9,15]
monster_list = []

i = 0
for name in monster_name:
    hp = monster_hp[i]
    mp = monster_mp[i]
    atk = monster_atk[i]
    dfn = monster_dfn[i]
    exp = monster_exp[i]

    mon = charcter.Charcter()
    mon.name = name
    mon.hp = hp
    mon.mp = mp
    mon.now_hp = hp
    mon.now_mp = mp
    mon.attack = atk
    mon.defense = dfn
    mon.exp = exp
    monster_list.append(mon)
    i += 1

