import time

# Hàm nhập danh sách chuỗi
def nhap_danh_sach_chu(n):
    danh_sach = []
    for i in range(n):
        chuoi = input(f"Nhập chuỗi ký tự thứ {i+1}: ")
        while len(chuoi) > 20:
            print("Độ dài chuỗi ký tự không được quá 20 ký tự. Vui lòng nhập lại!")
            chuoi = input(f"Nhập chuỗi ký tự thứ {i+1}: ")
        danh_sach.append(chuoi)
    return danh_sach

# Hàm nhập danh sách số
def nhap_danh_sach_so(n):
    danh_sach = []
    for i in range(n):
        while True:
            try:
                so = int(input(f"Nhập số nguyên thứ {i+1}: "))
                danh_sach.append(so)
                break
            except ValueError:
                print("Giá trị không hợp lệ. Vui lòng nhập số nguyên.")
    return danh_sach

# Thuật toán Selection Sort với đo hiệu suất
def selection_sort(numberlist):
    comparisons = 0
    x = len(numberlist)
    start_time = time.perf_counter()  # Sử dụng time.perf_counter() thay vì time.time()
    for i in range(x):
        min_x = i
        for j in range(i + 1, x):
            comparisons += 1  # Đếm số lần so sánh
            if numberlist[j] < numberlist[min_x]:
                min_x = j
        numberlist[i], numberlist[min_x] = numberlist[min_x], numberlist[i]
    end_time = time.perf_counter()
    return numberlist, comparisons, end_time - start_time

# Thuật toán Bubble Sort với đo hiệu suất
def bubble_sort(numberlist):
    comparisons = 0
    x = len(numberlist)
    start_time = time.perf_counter()  # Sử dụng time.perf_counter() thay vì time.time()
    for i in range(x):
        for j in range(0, x - i - 1):
            comparisons += 1  # Đếm số lần so sánh
            if numberlist[j] > numberlist[j + 1]:
                numberlist[j], numberlist[j + 1] = numberlist[j + 1], numberlist[j]
    end_time = time.perf_counter()
    return numberlist, comparisons, end_time - start_time

# Thuật toán Insertion Sort với đo hiệu suất
def insertion_sort(numberlist):
    comparisons = 0
    start_time = time.perf_counter()  # Sử dụng time.perf_counter() thay vì time.time()
    for i in range(1, len(numberlist)):
        key = numberlist[i]
        j = i - 1
        while j >= 0:
            comparisons += 1  # Đếm số lần so sánh
            if key >= numberlist[j]:
                break
            numberlist[j + 1] = numberlist[j]
            j -= 1
        numberlist[j + 1] = key
    end_time = time.perf_counter()
    return numberlist, comparisons, end_time - start_time

# Nhập dữ liệu
def nhap_so_luong_chuoi():
    while True:
        try:
            n_chu = int(input("Nhập số lượng chuỗi ký tự: "))
            if n_chu < 1:
                print("Số lượng chuỗi phải lớn hơn 0. Vui lòng thử lại.")
            else:
                return n_chu
        except ValueError:
            print("Giá trị không hợp lệ. Vui lòng nhập số nguyên hợp lệ.")

n_chu = nhap_so_luong_chuoi()
danh_sach_chu = nhap_danh_sach_chu(n_chu)
n_so = int(input("Nhập số lượng số: "))
danh_sach_so = nhap_danh_sach_so(n_so)

# Kết hợp chuỗi ban đầu
chuoi_ket_hop_chu = ', '.join(f'"{chuoi}"' for chuoi in danh_sach_chu)
chuoi_ket_hop_so = ', '.join(str(so) for so in danh_sach_so)
print(f"numberlist_chu = [{chuoi_ket_hop_chu}]")
print(f"numberlist_so = [{chuoi_ket_hop_so}]")

# Sắp xếp và đo hiệu suất
sorted_selection, comparisons_selection, time_selection = selection_sort(danh_sach_so.copy())
sorted_bubble, comparisons_bubble, time_bubble = bubble_sort(danh_sach_so.copy())
sorted_insertion, comparisons_insertion, time_insertion = insertion_sort(danh_sach_so.copy())

# Hiển thị kết quả
print("\nKết quả sắp xếp:")
print(f"Selection Sort: {sorted_selection}")
print(f"Bubble Sort: {sorted_bubble}")
print(f"Insertion Sort: {sorted_insertion}")

print("\nHiệu suất sắp xếp:")
print(f"Selection Sort: Comparisons: {comparisons_selection}, Time: {time_selection:.6f} seconds")
print(f"Bubble Sort: Comparisons: {comparisons_bubble}, Time: {time_bubble:.6f} seconds")
print(f"Insertion Sort: Comparisons: {comparisons_insertion}, Time: {time_insertion:.6f} seconds")

# Nhận xét
if time_selection < time_bubble and time_selection < time_insertion:
    print("\nNhận xét: Selection Sort là thuật toán hiệu quả nhất trong trường hợp này (ít thời gian thực thi nhất).")
elif time_bubble < time_selection and time_bubble < time_insertion:
    print("\nNhận xét: Bubble Sort là thuật toán hiệu quả nhất trong trường hợp này (ít thời gian thực thi nhất).")
elif time_insertion < time_selection and time_insertion < time_bubble:
    print("\nNhận xét: Insertion Sort là thuật toán hiệu quả nhất trong trường hợp này (ít thời gian thực thi nhất).")
else:
    print("\nNhận xét: Các thuật toán có thời gian thực thi tương đương.")
