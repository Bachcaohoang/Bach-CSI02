#selection sort
# def selectnum(numberlist):
#     x = len(numberlist)
#     for i in range(x):
#         min_x = i  
#         for j in range(i + 1, x):
#             if numberlist[j] < numberlist[min_x]: 
#                 min_x = j
#         numberlist[i], numberlist[min_x] = numberlist[min_x], numberlist[i]
#     return numberlist
# numberlist = [5, 9, 1, 12, 30, 35, 75, 10, 15, 20, 4, 0, 20, 0, 20, 3, 6, 14]
# sorted_numberlist = selectnum(numberlist)
# print('Danh sach: ', sorted_numberlist)

#bubble sort
# def selectnum(numberlist):
#     x = len(numberlist)
#     for i in range(x):
#         for j in range(0, x - i - 1):
#             if numberlist[j] > numberlist[j + 1]:
#                 numberlist[j], numberlist[j + 1] = numberlist[j + 1], numberlist[j]
#     return numberlist
# numberlist = [5, 9, 1, 12, 30, 35, 75, 10, 15, 20, 4, 0, 20, 0, 20, 3, 6, 14]
# sorted_numberlist = selectnum(numberlist)
# print('danh sach:',sorted_numberlist)

#insertion sort

def insertion_sort(numberlist):
    for i in range(1, len(numberlist)):
        key = numberlist[i]
        j = i - 1
        while j >= 0 and key < numberlist[j]:
            numberlist[j + 1] = numberlist[j]
            j -= 1
        numberlist[j + 1] = key
    return numberlist

numberlist = [5, 9, 1, 12, 30, 35, 75, 10, 15, 20, 4, 0, 20, 0, 20, 3, 6, 14]
sorted_numberlist = insertion_sort(numberlist)
print('Danh sách đã sắp xếp:', sorted_numberlist)



