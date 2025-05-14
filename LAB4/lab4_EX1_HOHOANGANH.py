# Hồ Hoàng anh - 22115054122103

# # c1
# str1 = input('File path: ')
# # Hàm rfind() trong Python trả về chỉ mục cuối cùng nơi
# # chuỗi str được tìm thấy, hoặc -1 nếu không tìm thấy.
#
# print(str1)
# s = str1.rfind('\\')
# b = str1[s+1:]
# print(b)
# a = str1[:s]
# print(a)


# Hàm split() trong Python chia chuỗi theo delimeter đã cho
# (là space nếu không được cung cấp) và trả về danh sách các chuỗi con
# nếu bạn cung cấp đối số num thì chia chuỗi thành num + 1 chuỗi con.


# c2

str1 = input('File path: ')
s = str1.split('\\')
# print(s[1])
# print(s[2])
# print(s[3])
print(s[4])
print(s[-1])
a = '\\'

# Hàm join() trong Python nối chuỗi các biểu diễn chuỗi
# của các phần tử trong dãy seq thành một chuỗi.
print(a.join(s[:-1]))