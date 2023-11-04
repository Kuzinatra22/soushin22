# bukva = input("Введите букву")
# if bukva == "a" or bukva == "e" or bukva == "i" or bukva == "o":
#     print("Буква гласная")
# else:
#     print("Буква согласная")


# bukva = input("Введите букву")

# glasnye = ["a","e","i","o","y"]

# if bukva in glasnye:
#     print("Буква гласная")
# else:
#     print("Буква согласная")


coordinate = input("Введите координату ")
letter = coordinate[0]
number = int(coordinate[1]) 

if number % 2 == 0 and (letter == "b" or letter == "d" or letter == "f" or letter == "h") :
    print ("клетка чёрная")
elif: number % 2 == 0 and (letter == "a" or letter == "c" or letter == "e" or letter == "g") :
else:
    print("клетка чёрная")



num = 121
count = 0
for i in range(2,num):
    if (num % i == 0):
        count += 1
    if(count>0):
        print(f"Число {num} составное.\nОно делится на {i}")
    else:
         print(f"число простое")

  
       

