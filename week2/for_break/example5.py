secret = 4

for i in range(5):
    x = int(input("Угадай число от 1 до 5: "))
    if x == secret:
        print("Молодец!")
        break
