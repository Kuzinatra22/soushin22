import random
hp = 100
speed = 0
distance = 400
yetti = 1
tree = 2
rock = 3

while True:
    print()

    chanceEnemy = random.randint(0,10)
    if chanceEnemy == rock:
        print('Вы столкнулись с камнем')
        hp -=5
        print(f"У вас осталось {hp} жизней")
    elif chanceEnemy == yetti:
        print('Вас пожрал Йети')
        hp -=10
        print(f"У вас осталось {hp} жизней")
    elif chanceEnemy == tree:
        print('Вы врезались в дерево')
        hp -=8
        print(f"У вас осталось {hp} жизней")


    speed += 1
    distance -= speed
    print(F"\nВы летите со скорость {speed} км/с")
    print(F"\n Осталось проехать {speed} км/с")
    print(F"Осталось проехать {distance} километров")
    if (distance <= 0):
        print("ура")
        break
    if (hp<=0):
      print("Вас сожрали")
      break


    #сделать,чтобы игрок мог выбирать сторону,куда повернуть