#  PHẦN 1: KIẾN THỨC CHUNG VỀ LẬP TRÌNH
# Câu 1: Giải thích sự khác nhau giữa biến toàn cục (global variable) và biến cục bộ (local variable) trong lập trình -->
# Biến toàn cục và biến cục bộ là hai khái niệm quan trọng trong lập trình, giúp quản lý phạm vi và vòng đời của biến. Biến toàn cục được khai báo ngoài tất cả các hàm và có thể được sử dụng ở bất kỳ đâu trong chương trình, trong khi biến cục bộ chỉ tồn tại trong phạm vi của một hàm nhất định. Việc sử dụng biến toàn cục giúp chia sẻ dữ liệu giữa các hàm, nhưng có thể gây ra lỗi nếu không kiểm soát tốt. Ngược lại, biến cục bộ giúp tăng tính bảo mật và dễ bảo trì hơn do phạm vi ảnh hưởng nhỏ. Vì vậy, lập trình viên nên ưu tiên sử dụng biến cục bộ trừ khi thật sự cần đến biến toàn cục.
#  Câu 2: Viết một đoạn mã Python để kiểm tra một số có phải là số nguyên tố hay không. 
import math

def is_prime(n):
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    for i in range(5, int(math.sqrt(n)) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False

    return True

num = int(input("Nhập một số: "))
if is_prime(num):
    print(f"{num} là số nguyên tố")
else:
    print(f"{num} không phải số nguyên tố")
#  Câu 3: Trong mô hình Client-Server, hãy mô tả cách trình duyệt tải một trang web từ máy chủ. 
# Mô hình Client-Server là một mô hình kiến trúc mạng trong đó một máy chủ cung cấp
# dịch vụ và các máy khách (client) yêu cầu dịch vụ từ máy chủ. Khi trình
# dụng (client) muốn tải một trang web từ máy chủ, quá trình tải trang diễn
# ra như sau:
# 1. Trình duyệt (client) gửi yêu cầu tải trang đến máy chủ (server) thông
# qua địa chỉ URL của trang web.
# 2. Máy chủ nhận yêu cầu và tìm kiếm trang web yêu cầu trên hệ thống của
# mình.
# 3. Nếu trang web tồn tại, máy chủ sẽ gửi lại nội dung trang web cho
# trình duyệt (client) thông qua kết nối mạng.
# 4. Trình duyệt nhận được nội dung trang web và hiển thị trang web lên
# màn hình.






