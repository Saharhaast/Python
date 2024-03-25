f = open('myfile.txt', 'a') # แบบที่ 1
f = open('myfile.txt', 'r') # แบบที่ 2
f = open('myfile.txt', 'w') # แบบที่ 3
f = open('myfile.txt', 'x') # แบบที่ 4
#หากต้องการเปิดไฟล์ myfile.txt แต่ว่าไม่มีไฟล์ดังกล่าวอยู่ตั้งแต่แรก การรันคำสั่งแบบใดจะเกิด error ขึ้น
= แบบที่ 2


#กำหนดให้มีไฟล์ 2 ไฟล์ดังนี้
my_module.py
""" This is my_module.py """
if __name__ == '__main__':
    print(__name__)
my_main.py
""" This is my_main.py """
import my_module
#ข้อใดต่อไปนี้คือผลลัพธ์จากการ run my_main.py
=ไม่มี Output


#จงเติม Code ด้านล่างให้สมบูรณ์หากต้องการปิด File ที่เปิดค้างไว้ด้วยภาษา Python
f = open('file.txt', 'r')
=f.close()


#จงเติม Code ภาษา Python ต่อไปนี้ให้สมบูรณ์หากต้องการแสดงข้อมูลทั้งหมดที่อยู่ใน myfile.txt
f = open('myfile.txt', 'r')
print(f.read())


#กำหนดให้มีไฟล์ 2 ไฟล์ดังนี้
#จงเติม Code ใน my_main.py ให้สมบูรณ์หากต้องการ import my_module.py มาใช้งาน
my_module.py
""" This is my_module.py """
print(__name__)
my_main.py
""" This is my_main.py """
=import my_module <----Answer


#กำหนดให้มีไฟล์ 2 ไฟล์ดังนี้
my_module.py
""" This is my_module.py """
print(__name__) __name__ print ชื่อ เป็นคำสั่ง
my_main.py
""" This is my_main.py """
import my_module
#ข้อใดต่อไปนี้คือผลลัพธ์จากการ run my_main.py
='my_module'


#จงเติม Code ด้านล่างให้สมบูรณ์หากต้องการทราบว่า Directory ที่อยู่ปัจจุบันคืออะไรด้วยภาษา Python
import os
print(os.getcwd())


#จงเติม Code ด้านล่างให้สมบูรณ์หากต้องการเขียนข้อความว่า `I'm editing this file !` ด้วยภาษา Python
f = open('file.txt', 'w')
f.write("I'm editing this file !")
f.close()


my_module.py
""" This is my_module.py """
print(__name__)
#หากทำการ run my_module.py จะได้ output คือ '__main__'


#จงเติม Parameter ที่เหมาะสมหากต้องการเปิด File ชื่อ myfile.txt ด้วยภาษา Python
f = open('myfile.txt', 'r') # ต้องการอ่านไฟล์เพียงอย่างเดียว
f = open('myfile.txt', 'a') # ต้องการเขียนไฟล์โดยเพิ่มข้อมูลเข้าไปในไฟล์ต่อจากข้อมูลเดิมที่มีอยู่
f = open('myfile.txt', 'w') # ต้องการเขียนไฟล์โดยไม่สนใจข้อมูลที่อยู่ในไฟล์ตั้งแต่แรก
f = open('myfile.txt', 'x') # ต้องการเขียนไฟล์โดยไม่สนใจข้อมูลที่อยู่ในไฟล์ตั้งแต่แรก (แต่ต้องเป็นไฟล์ที่ไม่เคยมีอยู่แล้วเท่านั้น)