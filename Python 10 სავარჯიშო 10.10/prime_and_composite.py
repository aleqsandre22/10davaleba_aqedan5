import math

def main():

    num = int(input("შეიყვანეთ რიცხვი: "))

    # შეამოწმოს მარტივია თუ შედგენილი თუ არცერთი
    if num == 1:
        print(num, "არც შედგენილია და არც მარტივი")
    elif num == 2:
        print(num, "არის მარტივი")
    elif num % 2 == 0:
        print(num, "არის შედგენილი")
    else:
        is_prime = True
        for y in range(3, int(math.sqrt(num))+1, 2):
            if num % y == 0:
                is_prime = False
                break
        if is_prime:
            print(num, "არის მარტივი")
        else:
            print(num, "არის შედგენილი")

if __name__ == "__main__":
    main()
