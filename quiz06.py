string1 = 'Helloworld'
print(string1[-2:2:-1])
= lrowol

จงเติมคำตอบ ตอบเป็นตัวเลข หรือ ValueError
>>> hello = "Hello, World"
>>> hello.index("o")
=4
>>> hello.index("o", 10)
=ValueError
>>> hello.index("o", 5)
=8

mystring = 'This PSIT exam is very easy.'
x = mystring.index('a')
print(x)
=12

จงเติมคำสั่งที่ง่ายที่สุดที่จะทำให้แสดงผลออกมาว่า FALLO โดยต้องสร้างมาจาก ax และ bx เท่านั้น ให้ใช้ string slice; ห้ามใช้ค่าใหม่; ห้ามเรียก character ออกมาทีละตัว
ax = "FAIL"
bx = "HELLO"
print(ax[:2] + bx[2:])

อยากรู้ว่า String มี method อะไรให้ใช้บ้าง ให้พิมพ์ 
>>> help(str)
ลองอ่านดูว่า method index กับ method find เหมือนและต่างกันอย่างไร
จงเติมโค้ดในช่องว่างเพื่อให้แสดงผลตามที่กำหนดให้

>>> string = "abcDEF"
>>> string2 = 
string.upper()
>>> print(string2)
'ABCDEF'
>>> string3 = 
string.lower()
>>> print(string3)
'abcdef'

String ใน Python เป็นข้อมูลชนิด immutable กล่าวคือ ไม่สามารถเปลี่ยนแปลงแก้ไข string ปัจจุบันได้

จงเติมคำตอบ
>>> "Lo" in "Hello"
false
>>> "LO" in "Hello"
false
>>> "lo" in "Hello"
true

>>> "tomato" > "potato"
=true
>>> "Tomato" > "tomato"
=false
>>> "Pineapple" > "Potato"
=false
>>> "Pineapple" > "Apple"
=true

>>>'ca'.isupper()
False

>>>'CA'.isupper()
True
