# Nhập thông tin khách hàng và thu ngân
khach_hang1 = input('Nhập tên khách hàng: ')
thu_ngan1 = input('Tên nhân viên: ')

# Nhập số lượng sản phẩm
so_san_pham = int(input("Nhập số lượng sản phẩm: "))

# Danh sách sản phẩm
danh_sach_san_pham = []

for i in range(so_san_pham):
    print(f"\nNhập thông tin sản phẩm {i+1}:")
    ten_sp = input("Tên sản phẩm: ")
    so_luong = int(input("Số lượng: "))
    don_gia = int(input("Đơn giá: "))

    # Thêm sản phẩm vào danh sách
    danh_sach_san_pham.append({"ten": ten_sp, "so_luong": so_luong, "don_gia": don_gia})

# Tạo hóa đơn
hoa_don = {
    'thu_ngan': thu_ngan1,
    "ma_hoa_don": "HD20250305",
    "ngay": "05/03/2025",
    "khach_hang": khach_hang1,
    "danh_sach_san_pham": danh_sach_san_pham
}

# Tính tổng tiền
tong_tien = sum(sp["so_luong"] * sp["don_gia"] for sp in hoa_don["danh_sach_san_pham"])

# In bill thanh toán
hoa_don_mau = f"""
{" HÓA ĐƠN THANH TOÁN ":=^50}
Mã hóa đơn: {hoa_don["ma_hoa_don"]}
Ngày: {hoa_don["ngay"]}
Khách hàng: {hoa_don["khach_hang"]}
Thu ngân: {hoa_don["thu_ngan"]}
{"="*50}
{"Tên SP":<20}{"SL":<10}{"Đơn giá":<10}{"Thành tiền":<10}
{"="*50}
"""

for sp in hoa_don["danh_sach_san_pham"]:
    thanh_tien = sp["so_luong"] * sp["don_gia"]
    hoa_don_mau += f"{sp['ten']:<20}{sp['so_luong']:<10}{sp['don_gia']:<10}{thanh_tien:<10}\n"

hoa_don_mau += f"{'='*50}\n"
hoa_don_mau += f"{'Tổng cộng:':<40}{tong_tien:>10}\n"

# In ra màn hình
print(hoa_don_mau)
