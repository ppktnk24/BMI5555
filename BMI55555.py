@st.cache_data
def load_big_data():
    df = pd.read_csv("huge_file.csv")
    return df
# โปรแกรมคำนวณค่าดัชนีมวลกาย (BMI)

def calculate_bmi():
    print("=== โปรแกรมคำนวณ BMI ===")
    
    try:
        # รับค่าจากผู้ใช้
        weight = float(input("กรอกน้ำหนักของคุณ (กิโลกรัม): "))
        height_cm = float(input("กรอกส่วนสูงของคุณ (เซนติเมตร): "))
        
        # แปลงส่วนสูงจากเซนติเมตรเป็นเมตร
        height_m = height_cm / 100
        
        # คำนวณค่า BMI
        bmi = weight / (height_m ** 2)
        
        # แสดงผลลัพธ์ค่า BMI (ทศนิยม 2 ตำแหน่ง)
        print(f"\nค่า BMI ของคุณคือ: {bmi:.2f}")
        
        # แปลผลตามเกณฑ์มาตรฐาน
        if bmi < 18.5:
            result = "น้ำหนักน้อยกว่ามาตรฐาน (ผอม)"
        elif 18.5 <= bmi < 23:
            result = "น้ำหนักปกติ (สุขภาพดี)"
        elif 23 <= bmi < 25:
            result = "น้ำหนักเกิน (ท้วม)"
        elif 25 <= bmi < 30:
            result = "อ้วน (ระดับ 1)"
        else:
            result = "อ้วนมาก (ระดับ 2)"
            
        print(f"ผลลัพธ์: {result}")
        
    except ValueError:
        print("ข้อผิดพลาด: กรุณากรอกเฉพาะตัวเลขเท่านั้น")

# เรียกใช้งานฟังก์ชัน
if __name__ == "__main__":
    calculate_bmi()