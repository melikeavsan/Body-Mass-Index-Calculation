def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

def bmi_category(bmi):
    if bmi < 18.5:
        return "Zayıf"
    elif 18.5 <= bmi < 24.9:
        return "Normal"
    elif 25 <= bmi < 29.9:
        return "Fazla kilolu"
    elif 30 <= bmi < 34.9:
        return "1. Derece Obez"
    elif 35 <= bmi < 39.9:
        return "2. Derece Obez"
    else:
        return "3. Derece Obez"

def main():
    try:
        weight = float(input("Kilonuzu kilogram cinsinden giriniz: "))
        height = float(input("Boyunuzu metre cinsinden giriniz (örneğin, 1.60): "))
        
        bmi = calculate_bmi(weight, height)
        category = bmi_category(bmi)
        
        print(f"Vücut Kitle Endeksiniz (BMI): {bmi:.2f}")
        print(f"BMI Kategorisi: {category}")
    
    except ValueError:
        print("Lütfen geçerli bir sayı girin.")

if __name__ == "__main__":
    main()
