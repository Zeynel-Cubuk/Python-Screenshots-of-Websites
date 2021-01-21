import screenshooter
import time


# COLORS
W = '\033[0m'  # beyaz
R = '\033[31m'  # kirmizi
G = '\033[1;32m'  # koyu yesil
O = '\033[33m'  # turuncu
B = '\033[34m'  # mavi
P = '\033[35m'  # mor
C = '\033[36m'  # sari
GR = '\033[37m'  # gri
RED = "\033[1;31m"
BLUE = "\033[1;34m"
CYAN = "\033[1;36m"
GREEN = "\033[0;32m"

def banner():
    print(O+" __ _ _       __                                    ")
    print("/ _(_) |_ ___/ _\ ___ _ __ ___  ___ _ __   ___ _ __ ")
    print("\ \| | __/ _ \ \ / __| '__/ _ \/ _ \ '_ \ / _ \ '__|")
    print("_\ \ | ||  __/\ \ (__| | |  __/  __/ | | |  __/ |   ")
    print("\__/_|\__\___\__/\___|_|  \___|\___|_| |_|\___|_|   ")

    print(GR + "# Author      :" + "KIZILYILDIZ✮")
    print(GR + "# Instagram   :" + "instagram.com/kiziilyildiz")
    print(GR + "# GitHub      :" + "github.com/Zeynel-Cubuk")
    print(GR + "# Title       :" + "site_screener.py")
    print(GR + "# Date        :" + "21/1/2021")
    print(GR + "# Version     :" + "2.1")

if __name__ == "__main__":
    banner()
    print("#"*52)
    time.sleep(1)
    url = input(GREEN+"\n[*] URL: ")
    #http://www.taanilinna.com/
    #img_name = url.split(".")[1]
    img_name = input(CYAN+"[!] Kayıt Adı: ")
    time.sleep(1)
    print(GREEN+"[!] Veri Alınıyor...")
    sc = screenshooter.Screen()
    image = sc.get_image(url)
    image.save(img_name+".png")
    print(GREEN+"[!] Kayıt Başarılı!")
