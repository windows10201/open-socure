
import random
from random import choice as rc



mail=[]

mix_m1=["Emran","Heron","Mursed","Sumon","Robiul","Khursed","Fahad","Mahir","Niloy","Salam","Ruhul","Sami","Asif","Monir","Jahid","Joshim","Rabbi","Ramim","Asraf","Forid","Mithun","Ashik","Sujon","Sobuj","Fahim","Tanim","Parvez","SamSik","Sami","Tanvir","Rakib","Rased","Abdullah","Raiyan","Rohan","Farabi","Jahangir","Faruk","Zaman","Nozrul","Alam","Anamul","Sabbir","Saimon","Minhaj","Mahadi","Mahamud","Sipon","Sakil","Srabon","Raj","Sifat","Hamza","Hamid","Jisan","Khalid","Suny","Joni","Hanna","Hasan","Habib","Mahin","Salman","Zubayer","Imtiyaz","Shohag","Tonmoy","Ariyan","Deluwar","Siraj"]
mix_m2=["Khan","Ahamed","Islam","Chowdhury","Molla","Talukdar","Roy","Hasan","Afridi","rahman","vau","Miya"]
mix_m3=["Roni","Rajib","Nil","Khawsar","Safin","Rakib","Mamun","Ontor","Biplob","Mustofa","Murad","Suvo","Nirob","Nahid","Farhan","Tarek","Selim","Utsho","Johir","Roton","Sohid","Rofik"]




def mix():
    global mail
    while True:
        F1=rc(mix_m1)
        F2=rc(mix_m2)
        ema1=f"{F1.lower()}{F2.lower()}{rc(range(1000))}@gmail.com"
        mail.append(ema1+"|"+F1+" "+F2)
        F1=rc(mix_m1)
        F2=rc(mix_m2)
        F3=rc(mix_m3)
        ema2=f"{F1.lower()}{F2.lower()}{F3.lower()}{rc(range(100))}@gmail.com"
        print(ema2)
        mail.append(ema2+"|"+F1+" "+F2+" "+F3)
        if len(mail) >10000:
            break
        else:
            continue


Angela=[]

fast_an=["Alex","Lx","Dx","Picchi","Mst","Pinik","Xaiko","Angel","Crash","Ewr"]
middle=["Xan","Bow","Pagli","Priya","Riya","Mahi","Priti","Fariya","Nipa","Juli","Sathi","Isha","Maisa","Tisa","Nusrat","Jannat","Mimi","Sumaiya","Zara","Chocolate","Pakhi","Moni","Misti","Rani","Pori","Nagin","Jerry","Ammu","Raisa","Arohi","Mariya","Nishi","PomPom","Nupur","Mayabi","Ruhi","Ritu","Mim","Lamiya","Bristy","Adrita","Soniya","Queen","Sweety","Adiba","Priyanka","Anamika","Toma"]

last=["Chowdhury","Xhowdhury","Moni","Queen"]



def papakipari():
    global Angela
    while True:
        f1=rc(fast_an)
        f2=rc(middle)
        f3=rc(last)
        email1=f"{f1.lower()}{f2.lower()}{f3.lower()}{rc(range(1000))}@gmail.com"
        Angela.append(email1+"|"+f1+" "+f2+" "+f3)
        
        
        f2x=rc(middle)
        f3x=rc(last)
        email2=f"{f2x.lower()}{f3x.lower()}{rc(range(1000))}@gmail.com"
        Angela.append(email2+"|"+f2x+" "+f3x)
        
        
        f1g=rc(fast_an)
        f2g=rc(middle)
        
        email3=f"{f1g.lower()}{f2g.lower()}{rc(range(1000))}@gmail.com"
        Angela.append(email3+"|"+f1g+" "+f2g)
        if len(Angela) > 1000:
            break
        else:continue 


papakipari()
mix()






























