# 3- Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и 
# выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

# *Пример:*

# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

x = int(input("Значение х - "))
y = int(input("Введите y - "))

if x > 0 and y > 0:
    print(f"При х = {x} и y = {y} -> I")
elif x < 0 and y > 0:
    print(f"При х = {x} и y = {y} -> II")
elif x < 0 and y < 0:
    print(f"При х = {x} и y = {y} -> III")
elif x > 0 and y < 0:
    print(f"При х = {x} и y = {y} -> IV")
else:
    print("Указана нулевая координата")