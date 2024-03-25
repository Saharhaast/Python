class	YES
assert	YES
with	YES
is	    YES
do	    NO
try	    YES
from	YES
pass	YES
where	NO
final	NO

pass

Chained  conditional
if x < y:
    print('x is less than y')
elif x > y:
    print('x is greater than y')
else:
    print('x and y are equal')

print(a)	4
print(b)	Error
print(c)	Error
print(x)	7

ผู้ใช้งาน function f สามารถเรียกใช้งาน function f ได้โดยการส่งค่าตัวเลข 2 จำนวน ไปให้ a และ b ซึ่งเป็น ตัวแปรรับค่าผ่านเข้ามาของ function f หรืออาจจะส่งเพียงตัวเลขเดียว ให้ไป b ก็ได้ (โดย a จะถูกกำหนดให้มีค่าเป็น 0) function นี้ ต้องการหาผลรวมระหว่าง a และ b และส่งค่ากลับมา
def f(a=0,b):
    return a+b
เมื่อทดลองใช้งาน function นี้ พบว่ามี Error
ให้เขียนบรรทัดนั้นใหม่ให้ถูกต้อง
def f(b, a=0):
    return a + b

encapsulation
generalization
refactoring

 

      
