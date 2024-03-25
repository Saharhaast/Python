initial_amount = 100  # เงินเริ่มต้น 100 บาท
monthly_interest_rate = 0.05  # อัตราดอกเบี้ยร้อยละ 5

for month in range(1, 49):  # คำนวณเป็นระยะเวลา 12 เดือน
    interest = initial_amount * monthly_interest_rate  # คำนวณดอกเบี้ย
    initial_amount += interest  # เพิ่มเงินที่ได้รับเข้ากับเงินเริ่มต้น
    
    print(f"เดือนที่ {month}: ยอดเงิน = {initial_amount:.2f} บาท")

