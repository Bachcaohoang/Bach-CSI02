# arr1 = [int(x) for x in input("Nhập các số, cách nhau bằng khoảng trắng: ").split()]

# if 5 in arr1:
#     positions = [i for i, value in enumerate(arr1) if value == 5]
#     print("Giá trị 5 có trong mảng tại các vị trí:", positions)
# else:
#     print("Giá trị 5 không có trong mảng.")
### GV SỬA
# def input_array():
#   arr = []
#   n = int(input("Nhap so phan tu cua mang: "))
#   for i in range(n):
#     value = int(input(f"Phan tu thu {i+1}: "))
#     arr.append(value)
#   return arr

# def sequential_search(arr, target):
#  #c1
#   # ans = []
#   # counter = 0
#   # for i in arr:
#   #   if i == target:
#   #     ans.append(counter)
#   #   counter += 1
#   # return ans
# #C2
#   for i in range(len(arr)):
#     if arr[i] == target:
#       return i
#     return -1
  
# b2 Cho 1 mang arr tìm vị trí num trong mảng 
# Bắt đầu với khoảng tìm kiếm từ phần từ đầu đến phần tử cuối arr tìm phần tử mid với num neu mid==num ket thuc 
# neu mid > num tim kiem sang mang con ben trai cua mid 
# neu mid< num tim kiem sang mang con ben phai cua mid 
# neu khoang trong num ko ton tai trong arr ket thuc
def binary_search(arr, num):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2  # Tính chỉ số giữa

        if arr[mid] == num:  # Nếu phần tử giữa bằng num
            return mid  # Trả về vị trí của num
        elif arr[mid] > num:  # Nếu phần tử giữa lớn hơn num
            right = mid - 1  # Tìm kiếm bên trái
        else:  # Nếu phần tử giữa nhỏ hơn num
            left = mid + 1  # Tìm kiếm bên phải

    return -1  # Nếu không tìm thấy num trong arr

# Ví dụ sử dụng hàm
arr = [2,5,8,12,16,23,38,56,72,91]  # Mảng đã được sắp xếp
num= 23
result = binary_search(arr, num)

if result != -1:
    print(f"Số {num} có trong mảng tại vị trí: {result}")
else:
    print(f"Số {num} không có trong mảng.")
