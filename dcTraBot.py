import discord
from smtplib import SMTP
from random import *

prefix = "tr."

log = open("log.txt" , "a")

def pre(metin):
    metin2 = metin.lower()
    a = prefix + metin2
    return a
def mail_at(baslik, mesaj):
    try:
        subcjet = baslik
        message = mesaj
        content = "Subject: {0}\n\n{1}".format(subcjet, message)

        # Hesap Bilgileri
        myMailAdress = "keylogger.akb@gmail.com"
        password = "kerem2005"

        # Kime Gönderilecek Bilgisi
        sendTo = "kerembegicpython@gmail.com"

        mail = SMTP("smtp.gmail.com", 587)
        mail.ehlo()
        mail.starttls()
        mail.login(myMailAdress, password)
        mail.sendmail(myMailAdress, sendTo, content.encode("utf-8"))
    except Exception as e:
        pass
def kufur_etti(kufur,mesaj):
    mail_at("Küfür ettiler", "Birisi küfür yazdı :(\nMesaj: {0}\nBilgi: {1}".format(kufur,mesaj))



client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    random10 = randint(1, 7)
    random10 = str(random10)
    gelenmesaj = message.content
    liste = []
    if message.author == client.user:
        return

    elif message.content.startswith('sg'):
        await message.channel.send("Ettiğin küfürün ekran alıntısı alındı ve botun sahibine gönderildi. Lütfen bir daha etme. Yasal zorunluluk gereği ihbat etmek zorunda kalabilirim. Eğer yanlış anlaşılma olduysa bu mesajı görmezden gelebilirsin.")
        kufur_etti("sg",message)


    elif 'amk' in gelenmesaj:
        await message.channel.send("Ettiğin küfürün ekran alıntısı alındı ve botun sahibine gönderildi. Lütfen bir daha etme. Yasal zorunluluk gereği ihbat etmek zorunda kalabilirim. Eğer yanlış anlaşılma olduysa bu mesajı görmezden gelebilirsin.")
        kufur_etti("amk",message)

    elif message.content.startswith('amına koyarım'):
        await message.channel.send("Ettiğin küfürün ekran alıntısı alındı ve botun sahibine gönderildi. Lütfen bir daha etme. Yasal zorunluluk gereği ihbat etmek zorunda kalabilirim. Eğer yanlış anlaşılma olduysa bu mesajı görmezden gelebilirsin.")
        kufur_etti('amına koyarım',message)

    elif 'aq' in gelenmesaj:
        await message.channel.send("Ettiğin küfürün ekran alıntısı alındı ve botun sahibine gönderildi. Lütfen bir daha etme. Yasal zorunluluk gereği ihbat etmek zorunda kalabilirim. Eğer yanlış anlaşılma olduysa bu mesajı görmezden gelebilirsin.")
        kufur_etti('aq',message)

    elif 'siktir' in gelenmesaj:
        await message.channel.send("Ettiğin küfürün ekran alıntısı alındı ve botun sahibine gönderildi. Lütfen bir daha etme. Yasal zorunluluk gereği ihbat etmek zorunda kalabilirim. Eğer yanlış anlaşılma olduysa bu mesajı görmezden gelebilirsin.")
        kufur_etti('siktir',message)

    elif 'piç' in gelenmesaj:
        await message.channel.send("Ettiğin küfürün ekran alıntısı alındı ve botun sahibine gönderildi. Lütfen bir daha etme. Yasal zorunluluk gereği ihbat etmek zorunda kalabilirim. Eğer yanlış anlaşılma olduysa bu mesajı görmezden gelebilirsin.")
        kufur_etti('piç',message)

    elif 'pic' in gelenmesaj:
        await message.channel.send("Ettiğin küfürün ekran alıntısı alındı ve botun sahibine gönderildi. Lütfen bir daha etme. Yasal zorunluluk gereği ihbat etmek zorunda kalabilirim. Eğer yanlış anlaşılma olduysa bu mesajı görmezden gelebilirsin.")
        kufur_etti('pic',message)

    elif 'orospu' in gelenmesaj:
        await message.channel.send("Ettiğin küfürün ekran alıntısı alındı ve botun sahibine gönderildi. Lütfen bir daha etme. Yasal zorunluluk gereği ihbat etmek zorunda kalabilirim. Eğer yanlış anlaşılma olduysa bu mesajı görmezden gelebilirsin.")
        kufur_etti('orospu çocuğu',message)

    elif message.content.startswith(pre("mesaj")):
        await message.channel.send("Bot sahibine hemen buraya bakması için mesaj gönderdim.")
        mail_at("Hemen discord'a bak.", "Birisi discordu kontrol etmeni istiyor !")

    elif message.content.startswith(pre('yardım')):
        await message.channel.send("Transfer Botu. Komutlar: ")
        await message.channel.send("""
        prefix = tr.
        yardım >> yardım menüsü
        transfer >> puan transfer talebi oluşturmak için kullanabilirsiniz. (Detay için: tr.y_transfer )
        mesaj >> yetkiliye mesaj gönderir
        """)

    elif message.content.startswith(pre('y_transfer')):
        await message.channel.send("""
    Kullanımı:
    tr.transfer @kişi miktar
    örnek:
    tr.transfer @Kerem 12
        """)

    elif message.content.startswith(pre('transfer')):
        await message.channel.send("Transfer Modu açık.")
        gelenmesaj_str = str(gelenmesaj)
        try:
            for i in gelenmesaj_str.split():
                liste.append(i)
            await message.channel.send(" {0} kullanıcısına, {1} puan gönderiliyor...".format(liste[1],liste[2]))
            try:
                log.write("{0} kullanıcısından, {1} kullanıcısına giden transfer: {2}\n".format(message.author,liste[1],liste[2]))
                mail_at("Puan Transfer Talebi","{0} kullanıcısından, {1} kullanıcısına giden transfer: {2}".format(message.author,liste[1],liste[2]))
                await message.channel.send("İşlem başarılı. Talebiniz alınmıştır. En kısa süre içinde onaylanacaktır. Teşekkürler @{}".format(message.author))
            except:
                await message.channel.send("Bir hata ile karşılaştım. Sahibim konu hakkında bilgilendiriliyor..")
                mail_at("HATA-Transfer botu","Devreye girme sebebi: log.write veya  mail_at kısmı. \nAdres:elif message.content.startswith(pre('transfer')): \n2. try metodu.\nkod satır numarası (farklı olabilir.): 112")
        except:
            await message.channel.send("Bir hata ile karşılaştım. Sahibim konu hakkında bilgilendiriliyor.. (Not: komutu yanlış kullanmanızdan kaynaklı bir sorun olabilir lütfen bakınız: tr.y_transfer )")
            mail_at("HATA-Transfer botu",
                    "Devreye girme sebebi: log.write veya  mail_at kısmı. \nAdres:elif message.content.startswith(pre('transfer')): \n1. try metodu.\nkod satır numarası (farklı olabilir.): 116")




client.run('NzU1NDk5ODU3MzMwMDQ1MDg4.X2EMEg.bT-Je9GzQFz8EBvuF1ydJWUIXCE')