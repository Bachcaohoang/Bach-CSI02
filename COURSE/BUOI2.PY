# LIST_3 = [x for x in range (10)]
# print(LIST_3)

# list =['af','r','dy','aud','c','a','c','bd']
# list.sort(reverse=True)
# print(list)

# set = set("mindx")

# partice\
#1.cho hai daayy so arr1 va arr2 duoi dang list,nhap hai so thanh 1 day va sap xep theo thu tu giam dan
# import numpy as np
# arr1 = np.random.randint(0, 1000, 50).tolist()
# arr2 = np.random.randint(0, 1000, 50).tolist()

# all = arr1 + arr2

# all.sort(reverse=True)

# print("Dãy số sau khi kết hợp và sắp xếp giảm dần:")
# print(all)

# arr1 = [int(x) for x in input('Nhập số').split() ]
# arr2 = [int(x) for x in input('Nhập số').split() ]

# all = arr1 + arr2
# all.sort(reverse=True)
# print("Dãy số sau khi kết hợp và sắp xếp giảm dần:")
# print(all)

#2. nhập 1 dãy số ,trả về cái giá trị: số lớn nhất , số nhỏ nhất  và số trung bình cộng dưới dạng tuple
arr1 = [int(x) for x in input('Nhập số').split() ]
lon = max(arr1)
nho = min(arr1)

average = sum(arr1) / len(arr1)

result = (lon, nho, average)

print("Số lớn nhất, số nhỏ nhất và trung bình cộng trong dãy:", result)
#3. 