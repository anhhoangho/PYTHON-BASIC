
ten_khach = input('Tên của khách hàng: ')
so_ban = input('Số bàn của khách: ')


danh_sach_san_pham = []

n = int(input('Nhập vào số lượng sản phẩm: '))

for i in range(n):
    sp = input('Nhập vào tên sản phẩm: ')
    sl = int(input('Nhập vào số lượng sản phẩm: '))
    don = int(input('Nhập vào giá: '))


    danh_sach_san_pham.append({
        "ten": sp,
        "so_luong": sl,
        "don_gia": don
    })

hoa_don = {
    "ma_hoa_don": "HD20250305",
    "ngay": "05/03/2025",
    "khach_hang": ten_khach,
    "so_ban": so_ban,
    "danh_sach_san_pham": danh_sach_san_pham
}

# Tạo hóa đơn mẫu
hoa_don_mau = f"""
{" HỒ HOÀNG ANH - 22115054122103 ":^50}
{"-" * 50}
{" HÓA ĐƠN THANH TOÁN ":=^50}
{"-" * 50} 
Số bàn: {hoa_don['so_ban']}
Mã hóa đơn: {hoa_don["ma_hoa_don"]}
Ngày: {hoa_don["ngay"]}
Khách hàng: {hoa_don["khach_hang"]}
Thu ngân: {'Hồ Hoàng Anh'}
{"=" * 50}
{"Tên SP":<20}{"SL":<10}{"Đơn giá":<10}{"Thành tiền":<10}
{"=" * 50}
"""

tong_tien = 0
for sp in hoa_don["danh_sach_san_pham"]:
    thanh_tien = sp["so_luong"] * sp["don_gia"]
    tong_tien += thanh_tien
    hoa_don_mau += f"{sp['ten']:<20}{sp['so_luong']:<10}{sp['don_gia']:<10}{thanh_tien:<10}\n"

# Thêm tổng tiền vào hóa đơn
hoa_don_mau += "=" * 50 + f"\n{'Tổng tiền:':<40}{tong_tien:<10} VNĐ\n" + "=" * 50

# In hóa đơn
print(hoa_don_mau)
