import os
import time
import strings
import charcter
import random
import monster

mychar = charcter.Charcter() 
mychar.level = 1
mychar.hp = 10
mychar.now_hp = 10
mychar.mp = 10
mychar.now_mp = 10
mychar.attack = 3
mychar.defense = 3

def main_menu():
    print(strings.STR_TITLE)
    print(strings.STR_MENU_START)
    print(strings.STR_MENU_END)

def game_menu():
    print(strings.G_MENU_DUNG)
    print(strings.G_MENU_SLEEP)
    print(strings.G_MENU_END)

# 初期画面
def main():
    while 1:
        os.system('tput clear')
        main_menu()
        input_m = input(strings.STR_MENU_SELECT)

        if input_m == strings.SEL_NUM_END:
           break 
            
        if input_m == strings.SEL_NUM_START:
           game()

        time.sleep(1)
# ゲームスタート
def game():
    os.system('tput clear')
    mychar.name = input(strings.STR_NAME_SELECT)

    while 1:
        os.system('tput clear')
        mychar.show_status()
        game_menu()
        input_m = input(strings.STR_MENU_SELECT)

        if input_m == strings.SEL_DUNGEON:
            dungeon()

        elif input_m == strings.SEL_SLEEP:
            print(strings.G_SLEEPING)
            time.sleep(1)
            mychar.now_hp = mychar.hp
            mychar.now_mp = mychar.mp

        elif input_m == strings.SEL_END:
            break

        time.sleep(1)

# ダンジョンへ
def dungeon():
    os.system('tput clear')
    input_m = ''
    show_dung_menu(2)

    while 1:
        if input_m == strings.SEL_GO:
            randval = random.randint(1, 10)   

            if randval == 1 or randval == 2  or  randval == 3 or  randval == 4:
                show_monster()
                show_dung_menu(2)
            else:
                print('なにもみつからなかった') 
                show_dung_menu(2)

        if input_m == strings.SEL_RETURN:
            break
        
        mychar.show_status()
        input_m = input(strings.STR_MENU_SELECT)
        os.system('tput clear')
        time.sleep(1)

def show_monster():

    randval = random.randint(0, 3)   
    one_monster = monster.monster_list[randval]

    while 1:
        show_title = 'モンスター [%1]があらわれた！\n'
        show_title = show_title.replace('%1', one_monster.name)
        print(show_title) 
        one_monster.show_status_mob()
        show_dung_menu(1)

        mychar.show_status()
        input_m = input(strings.STR_MENU_SELECT)

        if input_m == '1': 
            os.system('tput clear')
            print(mychar.name + 'の攻撃...')
            time.sleep(1)
            one_monster.now_hp = one_monster.now_hp - mychar.attack 

            print(one_monster.name + 'に' + str(mychar.attack) + 'のダメージ！')
            time.sleep(1)

            if one_monster.now_hp <= 0:
                print(one_monster.name + 'を倒した！！！') 
                time.sleep(1)
                mychar.exp = one_monster.exp
                print(mychar.name + 'は' + str(one_monster.exp) + 'の経験値を得た。') 
                time.sleep(1)
                break


            print(one_monster.name + 'の攻撃...')
            mychar.now_hp = mychar.now_hp - one_monster.attack 
            time.sleep(1)

            print(mychar.name + 'に' + str(one_monster.attack) + 'のダメージ...')
            time.sleep(1)

            if mychar.now_hp <= 0:
               deth_end()
               break


        if input_m == '2': 
            print('まだ魔法を覚えていない')
        if input_m == '3': 
            break

        os.system('tput clear')
        time.sleep(1)

def deth_end():
    print(mychar.name + 'は死んでしまった...') 
    time.sleep(1)
    print('どこからとも無く、声が聞こえる....') 
    time.sleep(1)
    print('聞こえますか..あなたの心に問いかけています...') 
    time.sleep(1)
    print('光の石を手に入れて王国を救ってください...\n') 
    time.sleep(1)
    print('復活しますか？？') 
    print('1:復活する') 
    print('2:世界から消える') 
    input_m = input(strings.STR_MENU_SELECT)

    if input_m ==  '1':
        mychar.now_hp = mychar.hp
        mychar.now_mp = mychar.mp
        game()
    elif input_m ==  '2':
        print('GAME OVER') 
        sys.exit 

 


def show_dung_menu(flg):
    if flg == 1:
        print('1. 攻撃')
        print('2. 魔法')
        print('3. 逃げる')
        print('')

    elif flg == 2:
        print('1. 進む')
        print('2. 戻る')
        print('')

if __name__ == '__main__':
    main()
