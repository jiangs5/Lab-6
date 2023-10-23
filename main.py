# Susan Jiang

def encode(str_num):
    encoded = ""
    for i in str_num:
        if int(i) < 7:
            encoded += str(int(i) + 3)
        else:
            encoded += str(int(i) - 7)
    return encoded


def decode(encoded_password):
    decoded_password = ""
    for num in encoded_password:
        old_num = (int(num) - 3) % 10
        decoded_password += str(old_num)
    return decoded_password


def main():
    while True:
        choice = menu()

        if choice == "1":
            pw = input("Please enter your password to encode: ")
            pw = encode(pw)
            print("Your password has been encoded and stored!")
        elif choice == "2":
            orig_pw = decode(pw)
            print(f'The encoded password is {pw}, and the original password is {orig_pw}.')
        elif choice == "3":
            quit()

def menu():
    print("Menu\n-------------")
    print("1. Encode\n2. Decode\n3. Quit")
    choice = input("Please enter an option: ")
    return choice

if __name__ == "__main__":
    main()
