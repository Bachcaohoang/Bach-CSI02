#Bài 1 
# input:một số thực a
# output: giá trị gấp đôi của a
# vd:
# input a=5
# output result =10

# def double_a():
#   a = float(input('Nhập số a: '))
#   return a * 2

# print(double_a())

#Bài2
# input mot so thuc r la ban kinh duong tron
# output chu vi va dien tich duong tron
# Pi = 3,1416
# r = int(input('nhập bán kính hình tròn'))

# def S(r):
#     return r*r*Pi
# def P(r):
#     return 2*Pi*r
# print(P(r))
# print(S(r))

#Bài 3
# input :một số nguyên n>0 và số n nguyên dương
# output: tổng các số nguyên dương chăn được nhập
# Nhập số nguyên dương n
n = int(input("Nhập số nguyên dương n: "))
# Khởi tạo tổng
tong = 0

for i in range(n):
    so = int(input(f"Nhập số thứ {i + 1}: "))
    if so > 0 and so % 2 == 0:  # Kiểm tra số dương và chẵn
        tong += so

# In ra tổng các số chẵn
print("Tổng các số nguyên dương chẵn được nhập là:", tong)
