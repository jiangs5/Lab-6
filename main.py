# Susan Jiang

def encode(str_num):
    encoded = ""
    for i in str_num:
        if int(i) < 7:
            encoded += str(int(i) + 3)
        else:
            encoded += str(int(i) - 7)
    return encoded

def main():
    pw = input("Enter a password to be encoded: ")
    print(encode(pw))

if __name__ == "__main__":
    main()
