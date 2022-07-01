"""Software yang kami buat bersifat open source"""

import os, time, sys, requests, re, webbrowser
os.system('clear')

print ("#----------------------------------------------------------------#")
print ("<|---------------------| Funny Cat Lite |-----------------------|>")
print (" | Author:             RX77E                                    |")
print (" | Spesial Thank's:    RX77E                                    |")
print (" | Github:             https://github.com/Sreetx                |")
print (" | Instagram:          https://www.instagram.com/memelucubikin  |")
print ("<|--------------------------------------------------------------|>")
print ("#----------------------------------------------------------------#")

try:
    url = sys.argv[1]
except IndexError:
    print (" [INFO] Ketikan "+sys.argv[0]+" https://www.namawebsite.com/ untuk mengunduh video menggunakan script ini\n")
    sys.exit()

try:
    print ("\n  [*] Mencari file video....")
    video = url.split('/')[-1]
    print('\n [*] Mengunduh video '+video+'.mp4....')
    fi = requests.get(url)
    with open(video+'.mp4' , 'wb') as vidio:
      vidio.write(fi.content)
    print ("\n  [*] Video berhasil di download...\n")
    print ("  [*] Video anda sudah disimpan dengan nama '"+video+".mp4'\n")
    tanya = input(" [*] Follow berbagai akun kami? [Y/n]")
    if tanya.lower() == 'y':
        webbrowser.open('https://github.com/Sreetx/')
        webbrowser.open('https://www.instagram.com/memelucubikin/')
        webbrowser.open('https://youtube.com/channel/UCscuxW-ZUViftGyJ9Z1cPbw/')
        webbrowser.open('https://progpem.blogspot.com/2022/04/hom.html/')
        print (" [*] Terima kasih atas perhatian kalian")
    else:
        sys.exit()
except Exception as e: print ("   [!] Video tidak ditemukan");sys.exit()
except KeyboardInterrupt: print ("\n   [*] Mematikan program....");time.sleep(3);sys.exit()