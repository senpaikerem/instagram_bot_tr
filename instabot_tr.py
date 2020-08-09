from selenium import webdriver
from time import sleep


def spamat():
    url = input("Gönderi url: ")
    adet = int(input("Kaç adet spam atılsın: "))
    uyku = 1
    if adet > 10:
        uyku = 2
    elif adet > 25:
        uyku = 3
    print("Uyku: ",uyku)
    sleep(1)
    driver.get(url=url)
    for i in range(0,adet):
        i = i+1
        print(i)
        try:
            button_ucnokta = driver.find_element_by_css_selector("svg._8-yf5")
            button_ucnokta.click()
            sleep(uyku)
            print("üç nokta yıklama > OK")
            button_sikayet = driver.find_element_by_css_selector("button.aOOlW.-Cab_")
            button_sikayet.click()
            sleep(uyku)
            print("şikayet et tıklama > OK")
            button_spam = driver.find_element_by_css_selector("button.b5k4S")
            button_spam.click()
            sleep(uyku+1)
            print("spam tıklama > OK")
            button_ok = driver.find_element_by_css_selector("button.sqdOP.L3NKy.y3zKF")
            button_ok.click()
            sleep(uyku)
            print("pencereyi kapatma > OK")
        except:
            pass

def sifredegistir(yeni,yeni2,tester):
    if yeni == yeni2:
        sd(yeni,yeni2,test=tester)
    else:
        print("HATA: İki şifre aynı değil!")
        pass

def sd(y,y2,test):
    url = 'https://www.instagram.com/accounts/password/change/'
    driver.get(url=url)

    eskii1 = driver.find_element_by_name("cppOldPassword")
    eskii1.send_keys(password)
    print('Last Pass > OK')
    sleep(1)

    yenii1 = driver.find_element_by_name("cppNewPassword")
    yenii1.send_keys(y)
    print('New Pass > OK')
    sleep(1)

    yenii2 = driver.find_element_by_name("cppConfirmPassword")
    yenii2.send_keys(y2)
    print('New Pass 2 > OK')
    sleep(1)

    degistir_but = driver.find_element_by_css_selector("button.sqdOP.L3NKy.y3zKF")
    degistir_but.click()
    print('Click button > OK')
    sleep(3)
    driver.close()

    if test == True:
        browser = webdriver.Chrome()
        urlb = "https://www.instagram.com/accounts/login/?source=auth_switcher"
        browser.get(url=urlb)
        sleep(2)
        usernamer = username
        passwordr = y2


        usernameee = browser.find_element_by_name("username")
        usernameee.send_keys(usernamer)
        print('Username > OK')
        sleep(1)

        passworddd = browser.find_element_by_name("password")
        passworddd.send_keys(passwordr + "\n")
        print('Password > OK')
        print('Please Check !')
        sleep(5)
        browser.close()
    else:
        print('Please Check !')


print("""
Instabot 'a hoşgeldiniz
@senpaikerem
""")

secenekler="""
[2]-Elle takip et
[3]-Elle takipten çık
[4]-Otomatik DM aç
[5]-Otomatik spam (gönderi)
[6]-Otomatik spam (hesap)
[7]-Otomatik sifre degistir
[8]-Otomatik DM v2
[e]-Çıkış
"""

print(secenekler)
secim= input("Seçim: ")


botuser = " "
botpass = " "


options = webdriver.ChromeOptions()
options.add_argument('--headless')

driver  = webdriver.Chrome(options=options)

driver.get(url='https://www.instagram.com/accounts/login/?source=auth_switcher')
sleep(2)
username = input("Kullanıcı Adınız: ")
password = input("Sifreniz: ")




if username=="":
    usernamee = driver.find_element_by_name("username")
    usernamee.send_keys(botuser)
    print('UsernameBot > OK')
    sleep(1)

    passwordd = driver.find_element_by_name("password")
    passwordd.send_keys(botpass + "\n")
    print('PasswordBot > OK')
    sleep(2)
else:
    usernamee = driver.find_element_by_name("username")
    usernamee.send_keys(username)
    print('Username > OK')
    sleep(1)

    passwordd = driver.find_element_by_name("password")
    passwordd.send_keys(password + "\n")
    print('Password > OK')
    sleep(2)

print("----------------Aşama 2-------------------------")
if secim =="2":
    kisi = str(input("Hesap(karşı taraf): "))
    url = 'https://www.instagram.com/'+str(kisi)
    driver.get(url=url)
    sleep(1)
    print("URL > OK")

    button = driver.find_element_by_css_selector("button.sqdOP.L3NKy.y3zKF")
    button.click()
    print('Pressed Follow Button')
    print('Successful !')
    driver.close()

elif secim=="3":
    kisi = str(input("Hesap(karşı taraf): "))
    url = 'https://www.instagram.com/'+str(kisi)
    driver.get(url=url)

    button = driver.find_element_by_css_selector("span.glyphsSpriteFriend_Follow.u-__7")
    button.click()
    sleep(1)
    button2 = driver.find_element_by_css_selector("button.aOOlW.-Cab_")
    button2.click()
    print('Pressed Unfollow Button')
    print('Successful !')
    driver.close()

elif secim=="4":
    sleep(1)
    url = "https://www.instagram.com/direct/inbox/"
    driver.get(url=url)
    try:
        sleep(1)
        button3= driver.find_element_by_css_selector("button.aOOlW.HoLwm")
        button3.click()
        sleep(1)
    except:
        pass
    sleep(1)


elif secim == "5":
    spamat()
    driver.close()

elif secim  =="6":
    kisi = str(input("Hesap(karşı taraf): "))
    adet = int(input("Kaç adet spam atılsın: "))
    uyku = 1
    url = 'https://www.instagram.com/'+str(kisi)
    driver.get(url=url)
    sleep(1)
    print("URL > OK")
    if adet > 10:
        uyku = 3
    elif adet > 25:
        uyku = 4
    else:
        uyku = uyku + 1
    for i in range(0,adet):
        i = i+1
        print(i)
        try:
            button_ucnokta = driver.find_element_by_css_selector("svg._8-yf5")
            button_ucnokta.click()
            sleep(uyku)
            print("üç nokta yıklama > OK")
            button_sikayet = driver.find_element_by_xpath(xpath="/html/body/div[4]/div/div/div/div/button[3]")
            button_sikayet.click()
            sleep(uyku)
            print("şikayet et tıklama > OK")
            button_spam = driver.find_element_by_css_selector("button.b5k4S")
            button_spam.click()
            sleep(uyku+1)
            print("spam tıklama > OK")
            button_ok = driver.find_element_by_xpath(xpath="/html/body/div[4]/div/div/div/div/div/div/div[2]/button")
            button_ok.click()
            sleep(uyku)
            print("pencereyi kapatma > OK")
        except:
            pass
    print("Sekme kapatılıyor...")
    driver.close()

elif secim =="7":
    new = input("Yeni şifre: ")
    new2 = input("Yeni şifre tekrar: ")
    t = input("Oto test edelim mi (yes or no): ")
    if t == 1 or "yes" or "evet":
        ts = True
    else:
        ts = False
    sifredegistir(new,new2,tester=ts)
    print("İşlem yapıldı lütfen kontrol edilmediyse kontrol ediniz..")
    sleep(5)
    driver.close()
elif secim =="8":
    sleep(2)
    url = "https://www.instagram.com/direct/inbox/"
    driver.get(url=url)
    sleep(4)
    bildirimkapa =  driver.find_element_by_xpath(xpath="/html/body/div[4]/div/div/div/div[3]/button[2]")
    bildirimkapa.click()
    sleep(1)

    a = int(input("Mesaj atılacak sıra: "))
    yol = '//*[@id="react-root"]/section/div/div[2]/div/div/div[1]/div[2]/div/div/div/div/div[{0}]/a'.format(a)
    dm = driver.find_element_by_xpath(xpath=yol)
    dm.click()

else:
    print("Çıkış Yapılıyor...")