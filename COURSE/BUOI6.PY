# Bài tập 1 - Linear Search: Viết một hàm thực hiện thuật toán Linear Search để tìm một phần tử trong danh sách. Hàm trả về:
# + Vị trí của phần tử đầu tiên nếu tìm thấy.
# + -1 nếu không tìm thấy.
# Input list of numbers
arr1 = [int(x) for x in input("Nhập các số: ").split()]

# Function to search for an element in a list
def search(numberlist, n, Z): 
    for i in range(n): 
        if numberlist[i] == Z: 
            return i
    return -1

Z = int(input("Nhập số cần tìm: "))

n = len(arr1)

result = search(arr1, n, Z)

if result == -1: 
    print("Element is not present in array") 
else: 
    print(f"Element is present at index {result}")
#Đếm số lần xuất hiện của các phần tử trong danh sách.
# def count_appearances(arr:list):
#     counts = {}
#     for num in arr:
#         if num in counts:
#             counts[num] += 1
#         else:
#             counts[num] = 1
#     return counts

# myList = input_array()

# print(count_appearances(myList))
#Viết hàm tìm tất cả các vị trí của một phần tử trong danh sách




