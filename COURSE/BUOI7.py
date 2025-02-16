# Quick Sort Implementation
# arr = [5, 9, 1, 12, 30, 35, 75, 10, 15, 20, 4, 0, 20, 0, 20, 3, 6, 14]

# def partition(arr, left, right):
#     pivot = arr[left]
#     i = left
#     for j in range(left + 1, right + 1):
#         if arr[j] < pivot:
#             i += 1
#             arr[i], arr[j] = arr[j], arr[i]
#     arr[left], arr[i] = arr[i], arr[left]
#     return i

# def quick_sort(arr, left, right):
#     if right - left <= 1:
#         return
#     pivot_index = partition(arr, left, right)
#     pivot_index = partition(arr, left, right)
#     quick_sort(arr, left, pivot_index)  
#     quick_sort(arr, pivot_index + 1, right)  

# quick_sort(arr, 0, len(arr) - 1)

# print(arr)
# countinng sort
# def counting_sort(arr):
#     if len(arr) <= 1:
#         return 
#     max_val = max(arr)
#     cout = [0] * (max_val + 1)
    
#     # Count occurrences of each element
#     for el in arr:
#         cout[el] += 1
    
#     index = 0
#     # Reconstruct the sorted array
#     for i in range(len(cout)):
#         for j in range(cout[i]):  # Use cout instead of count
#             arr[index] = i  # Assign the value to arr
#             index += 1  # Increment index

# # Example usage
# arr = [5, 9, 1, 12, 30, 35, 75, 10, 15, 20, 4, 0, 20, 0, 20, 3, 6, 14]
# counting_sort(arr)
# print(arr)
# ĐỀ COUNTING SỐ ÂM
