def encrypt(text, key):
    rail = ['' for _ in range(key)]
    direction = 1
    row = 0

    for ch in text:
        rail[row] += ch

        if row == 0:
            direction = 1
        elif row == key - 1:
            direction = -1

        row += direction

    return ''.join(rail)


def decrypt(cipher, key):
    pattern = [['' for _ in cipher] for _ in range(key)]

    row = 0
    direction = 1

    for col in range(len(cipher)):
        pattern[row][col] = '*'

        if row == 0:
            direction = 1
        elif row == key - 1:
            direction = -1

        row += direction

    index = 0
    for i in range(key):
        for j in range(len(cipher)):
            if pattern[i][j] == '*' and index < len(cipher):
                pattern[i][j] = cipher[index]
                index += 1

    result = ""
    row = 0
    direction = 1

    for col in range(len(cipher)):
        result += pattern[row][col]

        if row == 0:
            direction = 1
        elif row == key - 1:
            direction = -1

        row += direction

    return result


while True:
    print("\n===== Rail Fence Cipher =====")
    print("1. Encrypt")
    print("2. Decrypt")
    print("3. Exit")

    choice = input("Enter Choice: ")

    if choice == '1':
        text = input("Enter Plain Text: ")
        key = int(input("Enter Number of Rails: "))
        print("Encrypted:", encrypt(text, key))

    elif choice == '2':
        text = input("Enter Cipher Text: ")
        key = int(input("Enter Number of Rails: "))
        print("Decrypted:", decrypt(text, key))

    elif choice == '3':
        break

    else:
        print("Invalid Choice")
