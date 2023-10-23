# Susan Jiang

def encode(str_num):
    temp_list = []
    temp_list[:] = str_num
    encoded = ""
    for i in temp_list:
        if int(i) < 7:
            encoded += str(int(i) + 3)
        else:
            encoded += str(int(i) - 7)
    return encoded

def main():
    print(encode("00009962"))

if __name__ == "__main__":
    main()
