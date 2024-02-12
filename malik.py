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
        return pwn.text

if __name__ == "__main__":
    api = "http://api.hackertarget.com/reverseiplookup/"
    if len(sys.argv) < 2:
        malik.logo()
        print("Untuk bantuan:\n  python malik.py -h/--help\n")
    elif str(sys.argv[1]) == "-h" or str(sys.argv[1]) == "--help":
        malik.logo()
        print("python malik.py [target]\npython malik.py [target] -o/--output [output.txt]\n")
    elif len(sys.argv) == 2:
        x = str(sys.argv[1])
        malik.logo()
        mulai = malik(x, api)
        uu = mulai.main()
        print(f"{uu}\n")
    elif len(sys.argv) == 4:
        if (str(sys.argv[2]) == "-o" or str(sys.argv[2]) == "--output") and '.txt' in str(sys.argv[3]).lower():
            x = str(sys.argv[1])
            f = sys.argv[3]
            mulai = malik(x, api)
            malik.logo()
            haha = mulai.main()
            file = open(str(f),'w')
            for an in haha:
                file.write(str(an)+"\n")
            file.close()
            print(f"Output berhasil disimpan dengan nama {str(sys.argv[3])}\n")
        else:
            pass
    else:
        print("\nUntuk bantuan:\n  python malik.py -h/--help\n")
