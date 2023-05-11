x = int(input("შეიყვანეთ პირველი რიცხვი: "))
y = int(input("შეიყვანეთ მეორე რიცხვი: "))

if x > y:
    print(x, "უფრო მეტია", y)
elif y > x:
    print(y, "უფრო მეტია", x)
else:
    print("ტოლია")