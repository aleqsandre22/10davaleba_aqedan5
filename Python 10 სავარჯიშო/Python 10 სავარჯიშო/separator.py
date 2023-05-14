import math

def main():
    
    num1 = int(input("შეიყვანეთ რიცხვი: "))
    num2 = int(input("შეიყვანეთ მეორე რიცხვი: "))

    gcd = math.gcd(num1, num2)

    # ეკრანზე უდიდესი საერთო გამყოფის დაბეჭდვა
    print("უსჯ არის:", gcd)

# გამოიძახეთ მთავარი ფუნქცია
if __name__ == "__main__":
    main()