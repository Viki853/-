a=int(input(" ведите сторону a: "))
b=int(input(" ведите сторону b: "))
c=int(input(" ведите сторону c: "))

if a + c > b and a + b > c and b + c > a:
    if a==b==c:
        print("Треугольник равностороний")

    elif a==b or b==c or c==a:
        print("Треугольник равнобедренный")

    else:
        print("Треугольник разностороний")
else:
    print("Такого треугольника нет")