
avtolar = ['audi','bmw','volvo','kia','hyundai']
for avto in avtolar:
    if avto == 'bmw':
        print(avto.upper())
    else:
     print(avto.title())
ism='Jaloliddin'
ism == 'Ali'
print(ism == ('jaloliddin').title())

ism = input("Ismingiz nima?\n")
if ism.lower() != 'ali':
    print(f"Uzr,{ism.title()} biz Alini kutyabmiz.")
else:
    print("Salom, Ali")

javob = float(input("12*6 nechchiga teng?"))
if javob != 72:
    print("Javob xato!")
else:
    print("Javobingi judaaa to'g'riiii ")

yosh = int(input("Yoshingiz nechchida?"))
if yosh >= 18:
    print("Xush kelibsiz!!!")
    
else:
    print("Kirishingiz mumkin emas!!!")
    
login = input("Yangi login kiriting:")
if len(login) <=5:
    print("Login 5 ta harfdan ko'p bo'lishi shart!")
else:
  print("Welcome!!!")
yil = int(input("Tug'ilgan yilingizni kiriting:"))
if 2023-yil<18:
    print(f"Yoshingiz {2023-yil}da ekan")
    print("Mumkin emas uzr.")
else:
    print("xush keldingiz")


yosh = int(input("Yoshingiz nechada?\n"))
if yosh > 65:
    print("Siz covid-19  guruhidan ekansiz ")
else:
    print("Siz sog'lomsiz birodar")


x,y = 40,10
print("x>y") if x>y else print("x<y")

cars= ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
for car in cars:
    if car != 'gm':
        print(car.upper())
#     else:
#         print(car.title())

login = input("Loginingizni kiriting!")
if login:
    print("Xush kelibsiz Admin")

son_1 = int(input("1-sonni kiriting:"))
son_2 = int(input("2-sonni kiriting:"))
if son_1 == son_2:
    print("Sonlar teng ekan!!!")
else:
    print('tengmas')


sonlar = int(input('Istalgan sonni kiriting:'))
if sonlar > 0:
    print('Musbat son')
else:
    print('Manfiy')
    
sonlar = int(input("Musbat son kiriting:"))
if sonlar > 0:
    print((sonlar)**0.5)
else:
    print("Musbat son kiriting:")



    


























































































