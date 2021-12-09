a = int(input('Enter first side: '))
b = int(input('Enter second side: '))
c = int(input('Enter third side: '))

if (a + b > c and b + c > a and c + a > b):
    if (a == b and a != c) or (b == c and b != a) or (c == a and c != b):
        print('Равнобедренный треугольник')
    elif a == b == c:
        print('Равносторонний треугольник')
    else:
        print('Разносторонний треугольник')
else:
    print('Из этих отрезков невозможно составить треугольник')
