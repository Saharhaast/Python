def kaprekar_steps(n):
    # กำหนดค่าคงที่ Kaprekar's constant
    kaprekar_constant = 6174
    steps = 0
    
    # วนลูปเรื่อยๆ จนกว่าจะได้ผลลัพธ์เป็น Kaprekar's constant
    while n != kaprekar_constant:
        # แปลงตัวเลข n เป็นสตริง 4 หลัก
        n_str = str(n)
        
        # กรณีที่ n มีน้อยกว่า 4 หลัก ให้เติมศูนย์ไปด้านหน้า
        while len(n_str) < 4:
            n_str = '0' + n_str
        
        # เรียงเลขจากมากไปน้อยและน้อยไปมาก
        max_num = int(''.join(sorted(n_str, reverse=True)))
        min_num = int(''.join(sorted(n_str)))
        
        # คำนวณผลลัพธ์ใหม่
        n = max_num - min_num
        
        # เพิ่มจำนวนครั้งที่ใช้
        steps += 1
    
    return steps

# อ่านข้อมูลจากข้อมูลนำเข้า
n = int(input())

# คำนวณและแสดงผลลัพธ์
result = kaprekar_steps(n)
print(result)
