# # # # -*- coding: utf-8 -*-
# # # """
# # # Created on Fri Dec 15 14:15:51 2023

# # # @author: rasul
# # # """

# # # """
# # # 27/11/2020
# # # Dasturlash asoslari
# # # #12-dars: Xatolar
# # # Muallif: Anvar Narzullaev
# # # Web sahifa: https://python.sariq.dev
# # # """

# # # son = float(input("Juft son kiriting: ")
# # # if son%2==0:
# # #     print("Bu son juft emas.')
# # # else:
# # #     print("Rahmat!"))

# # # """
# # # 27/11/2020
# # # Dasturlash asoslari
# # # #12-dars: Xatolar
# # # Muallif: Anvar Narzullaev
# # # Web sahifa: https://python.sariq.dev
# # # """

# # # yosh = (input("Yoshingiz nechida?"))

# # # if yosh<=4 or yosh>=60:
# # #     narh = '0'
# # # elif yosh < 18:
# # #     narh = '10000'
# # # else:       
# # #     narh = '20000'
# #     # print(f"Chipta {narh} so'm")

# # # """
# # # # 27/11/2020
# # # # Dasturlash asoslari
# # # #12-dars: Xatolar
# # # Muallif: Anvar Narzullaev
# # # Web sahifa: https://python.sariq.dev
# # # """

# # # x = float(input("Birinchi sonni kiriting: "))
# # # y = float(input("Ikkinchi sonni kiriting: "))
# # # if x==y:
# # #     print(f"{x}={y}")
# # # elif x<y:
# # #     print(f"{x}<{y}")
# # # else:
# # #     print(f"{x}>{y}")




        
    



# # # a = f"Savatga {n+1}-mahsulotni qo'shing: "
# # # print(f"Do'konimizda {mahsulot} bor")
# # # print(f"Do'konimizda {mahsulot} yo'q")
# # # print("Savatingiz bo'sh")            



# # # """
# # # 27/11/2020
# # # Dasturlash asoslari!

# # """
# # 27/11/2020
# # Dasturlash asoslari
# # #12-dars: Xatolar
# # Muallif: Anvar Narzullaev
# # Web sahifa: https://python.sariq.dev
# # """

# # users = ['alisher1983','aziza','yasina' 'umar']

# # login = input("Yangi login tanlang:" )

# # if login in users:
# #     print('Login band, yangi login tanlang!')
# # else:
# #     print("Xush kelibsiz!")

# """
# 27/11/2020
# Dasturlash asoslari
# #12-dars: Xatolar
# Muallif: Anvar Narzullaev
# Web sahifa: https://python.sariq.dev
# """

# # son = float(input("Juft son kiriting: "))
# # if son%2==0:
# #     print("Rahmat!")
# # else:
# #     print("Bu son juft emas.")


# user = ['alisher1983', 'aziza', 'yasina']
# users = ['alisher1983','aziza','yasina' ,'umar']

# login = input("Yangi login tanlang:" )

# if login in users:
#     print('Login band, yangi login tanalng!')
# else:
#     print("Xush kelibsiz!")


"""
27/11/2020
Dasturlash asoslari
#12-dars: Xatolar
Muallif: Anvar Narzullaev
Web sahifa: https://python.sariq.dev
"""

# yosh = int(input("Yoshingiz nechida?"))

# if yosh<=4 or yosh>=60:
#     narh = 0
# elif yosh < 18:
#     narh = 10000
# else:
#     narh = 20000
#     print(f"Chipta {narh} so'm")

# """
# 27/11/2020
# Dasturlash asoslari
# #12-dars: Xatolar
# Muallif: Anvar Narzullaev
# Web sahifa: https://python.sariq.dev
# """

# x = float(input("Birinchi sonni kiriting: "))
# y = float(input("Ikkinchi sonni kiriting: "))
# if x==y and 0:
#     print(f"{x}={y}")
# elif x<y:
#     print(f"(x]<{y}")
# else:
#     print(f"{x}>(y)")

"""
27/11/2020
Dasturlash asoslari
#12-dars: Xatolar
Muallif: Anvar Narzullaev
Web sahifa: https://python.sariq.dev
"""

mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz',
               'kartoshka', 'olma', 'banan', 'uzum', 'qovun']


savat = []
for n in range(5):
    savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))

bor_mahsulotlar = []
mavjud_emas = []
for mahsulot in savat:
    if mahsulot in mahsulotlar:
        bor_mahsulotlar.append(mahsulot)
    else:
        mavjud_emas.append(mahsulot)

if mavjud_emas:
  print("Do'konimizda quyidagi mahsulotlar yo'q:")
  for mahsulot in mavjud_emas:
      print(mahsulot)
else:
  print("Siz so'ragan barcha mahsulotlar do'konimizda bor")
    































