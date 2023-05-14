def main():
    
    x = input("შეიყვანეთ სია: ")


    x = list(map(int, x.split()))

    # ეძებს მაქსიმუმს და მინიმუმს
    max_num = max(x)
    min_num = min(x)

    
    print("მაქსიმალური:", max_num)
    print("მინიმალური:", min_num)

if __name__ == "__main__":
    main()