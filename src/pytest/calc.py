import sys

def calcAdd(r_val1, r_val2):
    return r_val1 + r_val2

def calcSub(r_val1, r_val2):
    return r_val1 - r_val2

def calcMulti(r_val1, r_val2):
    return r_val1 * r_val2

def calcDivi(r_val1, r_val2):
    return r_val1 / r_val2

val1 = input('数値1を入力:')
val2 = input('数値2を入力:')

print("足し算:" + str(calcAdd(int(val1),int(val2))) )
print("引き算:" + str(calcSub(int(val1),int(val2))) )
print("かけ算:" + str(calcMulti(int(val1),int(val2))) )
print("割り算:" + str(calcDivi(int(val1),int(val2))) )

 
