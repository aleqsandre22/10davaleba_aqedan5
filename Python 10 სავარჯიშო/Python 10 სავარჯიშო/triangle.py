def main():
    
    a, b, c = sorted(map(int, input("შეიყვანეთ სამი რიცხვი გამოტოვებით: ").split()))

    if a + b > c:
        print("სამკუთხედი აიგება.")
    else:
        print("სამკუთხედის აგება შეუძლებელია.")

if __name__ == "__main__":
    main()