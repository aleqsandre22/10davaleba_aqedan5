AB = int(input("შეიყვანეთ გვერდის სიგრძე: "))
BC = int(input("შეიყვანეთ მეორე გვერდის სიგრძე: "))
AC = int(input("შეიყვანეთ მოსამე გვარდის სიგრძე: "))

if AB + BC > AC and AB + AC > BC and BC + AC > AB:
    print("შესაძლებელია აიგოს სამკუთხედი")
else:
    print("შეუძლებელია სამკუთხედის აგება")