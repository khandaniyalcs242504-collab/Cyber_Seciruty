def encrypt(text, key):
    result = ""

    for char in text:
        if char.isalpha():
            shift = key % 26

            if char.isupper():
                result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        else:
            result += char

    return result


def decrypt(text, key):
    result = ""

    for char in text:
        if char.isalpha():
            shift = key % 26

            if char.isupper():
                result += chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            else:
                result += chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
        else:
            result += char

    return result


while True:
    print("\n===== Caesar Cipher =====")
    print("1. Encrypt")
    print("2. Decrypt")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        text = input("Enter Plain Text: ")
        key = int(input("Enter Key: "))
        print("Encrypted Text:", encrypt(text, key))

    elif choice == '2':
        text = input("Enter Cipher Text: ")
        key = int(input("Enter Key: "))
        print("Decrypted Text:", decrypt(text, key))

    elif choice == '3':
        break

    else:
        print("Invalid Choice")
