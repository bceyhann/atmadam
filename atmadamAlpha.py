import sqlite3
from os import system
from time import sleep
import sys

db = sqlite3.connect("accounts.db") 
im = db.cursor()

def clear():  # For cleaning console.
    _ = system('cls')

def isitint(a):  # Checking input's type. If it is int function will return True value.
    b = True
    while True:
        try:
            a = int(a)
            b = True
            break
        except ValueError:
            b = False
            break
    return b

class bankamatik():  # Main class
    def __init__(self):
        self.login()
        self.accountno = self.data[0]
        self.accountpass = self.data[1]
        self.accountbalance = self.data[2]
        self.accountname = self.data[3]

        self.accountno = int(self.accountno) 
        self.accountpass = int(self.accountpass)
        self.accountbalance = int(self.accountbalance)

        self.menu()

    def login(self):  # Checking inputs matching an account.
        while True:
            while True:
                clear()
                print("ATMADAM BANKASINA HOŞGELDİNİZ\n-----------------------------\n")
                account = input("Hesap Numaranızı Giriniz: ")
                print("")
                if isitint(account)is True:
                    break
                else:
                    clear()
                    print("Lütfen sayısal bir değer giriniz...")
                    sleep(2)
                    continue
            while True:
                clear()
                print("ATMADAM BANKASINA HOŞGELDİNİZ\n-----------------------------\n")
                password = input("Şifrenizi Giriniz: ")
                print("")
                if isitint(password) is True:
                    break
                else:
                    clear()
                    print("Lütfen sayısal bir değer giriniz...")
                    sleep(2)
                    continue
            im.execute("""SELECT * FROM ac WHERE
            acno = '%s' AND acpass = '%s'"""%(account, password))
            self.data = im.fetchone()
            if not self.data:
                clear()
                print("Böyle bir hesap yok.\nLütfen tekrar deneyiniz...")
                sleep(2)
                continue
            else:
                return self.data

    def menu(self):  # After login menu.
        while True:
            clear()
            print("ATM ADAM BANK")
            print("------------------------------------\n")
            print("Hoşgeldiniz sayın,",self.accountname,"\n\nHesabınızdaki bakiye:",self.accountbalance,"""\n\n[1]Para Çekme
[2]Para Yatırma
[3]Faiz Yatırımı
[4]Çıkış
""")
            while True:
                choose = int(input("Yapacağınız işlemi seçiniz: "))  # Simulating switch case.
                if isitint(choose) is True:
                    break
                else:
                    clear()
                    print("Lütfen geçerli bir değer giriniz...")
                    sleep(2)
                    continue
            if(choose == 1):
                self.withdraw()
            elif(choose == 2):
                self.deposit()
            elif(choose == 3):
                self.invest()
            elif(choose == 4):
                self.quit()
            else:
                clear()
                print("Lütfen geçerli bir değer giriniz...")
                sleep(2)
                continue

    def withdraw(self):  # Withdraw money from account.
        while True:
            clear()
            value = input("Çekmek istediğiniz miktarı giriniz: ")
            if isitint(value) is True:
                break
            else:
                clear()
                print("Lütfen sayısal değer giriniz.")
                sleep(2)
                continue
        value = int(value)
        self.accountbalance -= value
        im.execute("UPDATE ac SET acbalance = ? WHERE acno = ?", (str(self.accountbalance), str(self.accountno))) # Updating account's balance.
        db.commit()
        clear()
        print("\nÇektiğiniz Miktar:",value,"\nKalan Paranız:",self.accountbalance)
        sleep(2)

    def deposit(self):  # Deposit money to account.
        while True:
            clear()
            value = input("Yatırmak istediğiniz miktarı giriniz:")
            if isitint(value) is True:
                break
            else:
                clear()
                print("Lütfen sayısal değer giriniz.")
                sleep(2)
                continue
        value = int(value)
        self.accountbalance += value
        im.execute("UPDATE ac SET acbalance = ? WHERE acno = ?", (str(self.accountbalance), str(self.accountno)))  # Updating account's balance.
        db.commit()
        clear()
        print("\nYatırdığınız Miktar:",value,"\nYeni Paranız:",self.accountbalance)
        sleep(2)

    def invest(self):  # For investing money in your account.
        while True:
            clear()
            print("Yatıracağınız Paranın miktarını ve Yatırılacak Gün Sayısını yazınız.\nYıllık faiz oranı 0.19'dur\n")
            sleep(2)
            while True:
                value = int(input("Yatıracağınız Miktar:"))
                if isitint(value) is True:
                    a = True
                    break
                else:
                    clear()
                    print("Lütfen sayısal değer giriniz.")
                    sleep(2)
                    continue
            while True:
                monthcount = int(input("\nAy Sayısı:"))
                if isitint(monthcount) is True:
                    b = True
                    break
                else:
                    clear()
                    print("Lütfen sayısal değer giriniz.")
                    sleep(2)
                    continue
            if a == True and b == True:
                break
            else:
                continue

        self.accountbalance -= value
        monthcount = monthcount / 12
        invest = value * (1+0.19*monthcount)  # Investing formula.
        self.accountbalance = self.accountbalance + invest
        im.execute("UPDATE ac SET acbalance = ? WHERE acno = ?", (str(self.accountbalance), str(self.accountno)))  # Updating account's balance.
        db.commit()
        clear()
        print("Yatırdığınız para: ",value,"\nNet Kazancınız: ",invest - value,"\nFaiz Sonucundaki paranız: ",self.accountbalance)
        sleep(5)

    def quit(self):     # For close the program. (Remember it's a simulation :)) )
        clear()
        print("ATM ADAM BANKASI İYİ GÜNLER DİLER...")
        sleep(2)
        sys.exit()


start = bankamatik()    # Calling class.
