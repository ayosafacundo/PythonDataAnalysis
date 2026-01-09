import sys
letters = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZabcdefghijklmnñopqrstuvwxyz"
symbols = " ,.-"
def decypher(st):
    for let in range(len(st)):
        if (not st[let] in letters and st[let] in symbols):
            print(st[let], end="")
            continue
        if (st[let] == "z" or st[let] == "Z"):
            print("a", end="")
            continue
        print(chr(ord(st[let])+1), end="")

def cypher(st):
    for let in range(len(st)):
        if (not st[let] in letters and st[let] in symbols):
            print(st[let], end="")
            continue
        if (st[let] == "a" or st[let] == "A"):
            print("z", end="")
            continue
        if (st[let] == " "):
            print(" ", end="")
            continue
        print(chr(ord(st[let])-1), end="")

if __name__ == "__main__":
    if (len(sys.argv[1:]) > 1):
        if (sys.argv[1][:2] == "en"):
            cypher(" ".join(sys.argv[2:]))
        elif (sys.argv[1][:2] == "de"):
            decypher(" ".join(sys.argv[2:]))
        else:
            raise ValueError("First parameter should be either encrypt or decrypt")
    else:
        raise ValueError("First parameter should be either encrypt or decrypt")