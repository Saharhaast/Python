i = 0
while i >= -4:
    print(i)
    i -= 1

for i in range(-1, -10, -3):
    print(i)    

Style Guide for Python Code คือ PEP หมายเลข 8
    
for i in range(1, 6):
    print(i)

โปรแกรมมี 3 บรรทัดด้านล่าง
x = 5
y = x
x = 7
เมื่อจบบรรทัดที่ 3 ตอนนี้ y มีค่าเท่าไร ตอบ 5

ถ้าต้องการข้ามการทำงานของโปรแกรมที่ยังเหลืออยู่ใน loop ปัจจุบัน แล้วให้ขึ้นกลับไปทำงานใน  loop ต่อไปได้เลย จะต้องใช้ statement ใด
continue

ถ้าต้องการออกจาก loop ก่อนที่เงื่อนไขการวน loop นั้นยังไม่ครบตามจำนวน (for loop) หรือเงื่อนไขใน while loop ยังเป็นจริงอยู่ จะต้องใช้ statement ใด 
break

ฟังก์ชั่นที่ไม่มีการคืนค่า ถูกเรียกว่าเป็นประเภท void function

ถ้าเขียน function x() ไว้ใน module x.py
และเขียน function y() ไว้ใน module y.py
ถ้า function y() ต้องการเรียกใช้ function x() ต้องทำใช้คำสั่งหรือพิมพ์ statement
import x
ไว้ใน file y.py

function ที่มีการคืนค่ากลับจะเรียกว่า fruitful function
โดยจะมี statement return ใน function นั้นเพื่อคืนค่าที่ต้องการกลับไป




 



