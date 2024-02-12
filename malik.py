import requests
import sys
from termcolor import colored as cl

class malik():
    def __init__(self, xx, aa):
        self.xx = xx
        self.aa = aa
        
    def logo():
        print(cl("\nSIMPLE REVERSE IP LOOKUP\n       by CukiD\n","magenta"))

    def main(self):
        ip = {"q":self.xx}
        pwn = requests.request("GET", self.aa, params=ip)
        return print(pwn.text)

if __name__ == "__main__":
    api = "http://api.hackertarget.com/reverseiplookup/"
    if len(sys.argv) < 2:
        malik.logo()
        print("Untuk bantuan:\n  python reverseIP.py -h/--help\n")
    elif str(sys.argv[1]) == "-h" or str(sys.argv[1]) == "--help":
        malik.logo()
        print("python reverseIP.py [target]\npython reverseIP.py [target] -o/--output [output.txt]\n")
    elif str(sys.argv[1]) != "-h" or str(sys.argv[1]) != "--help":
        x = str(sys.argv[1])
        malik.logo()
        mulai = malik(x, api)
        mulai.main()
        print("")
    elif len(sys.argv) < 3:
        if str(sys.argv[2]) == "-o" or str(sys.argv[2]) == "--output":
            x = str(sys.argv[1])
            mulai = malik(x, api)
            malik.logo()
            haha = mulai.main()
            file = open(str(sys.argv[3]),'w')
            for anjay in haha:
                file.write(str(anjay)+"\n")
            file.close()
            print(f"Output berhasil disimpan dengan mana {str(sys.argv[3])}\n")
        else:
            pass
    else:
        pass