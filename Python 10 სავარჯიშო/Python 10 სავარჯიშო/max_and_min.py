def main():
   
    x, y = map(int, input("შეიყვანეთ ორი რიცხვი, რომლებიც გამოყოფილია ინტერვალით: ").split())

    print(x, "არის უფრო მეტი", y) if x > y else print(y, "უფრო მეტია", x)

if __name__ == "__main__":
    main()