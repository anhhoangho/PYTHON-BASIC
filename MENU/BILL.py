san_pham_data = {}

with open('menu.txt', "r") as file:
    for line in file:
        line = line.strip()
        if not line:
            continue

        parts = line.split(",")
        ten_sp, gia = parts
        san_pham_data[ten_sp.strip()] = int(gia.strip())


ten_khach = input('Tên của khách hàng: ')
so_ban = input('Số bàn của khách: ')

danh_sach_san_pham = []

while True:
    sp = input('Nhập vào tên sản phẩm (done để kết thúc): ')
    if sp.lower() == 'done':
        break

    if sp not in san_pham_data:
        print("Sản phẩm không có trong menu, vui lòng nhập lại!")
        continue

    sl = int(input('Nhập vào số lượng sản phẩm: '))
    don = san_pham_data[sp]

    danh_sach_san_pham.append({
        "ten": sp,
        "so_luong": sl,
        "don_gia": don,
    })


ghi_chu = input("Ghi chú thêm cho hóa đơn (bấm Enter nếu không có): ")

hoa_don = {
    "khach_hang": ten_khach,
    "so_ban": so_ban,
    "danh_sach_san_pham": danh_sach_san_pham,
    "ghi_chu": ghi_chu,
}

hoa_don_mau = f"""
{' HỒ HOÀNG ANH ':^60}
{' 22115054122103 ':^60}
{'-' * 60}
{' HÓA ĐƠN THANH TOÁN ':=^60}
{'-' * 60} 
Số bàn: {hoa_don['so_ban']}
Khách hàng: {hoa_don["khach_hang"]}
Thu ngân: {'Hồ Hoàng Anh'}
{'=' * 60}
{'Tên SP':<20}{'SL':<10}{'Đơn giá':<15}{'Thành tiền':<10}
{'=' * 60}
"""


tong_tien = 0
for sp in hoa_don["danh_sach_san_pham"]:
    thanh_tien = sp["so_luong"] * sp["don_gia"]
    tong_tien += thanh_tien
    hoa_don_mau += f"{sp['ten']:<20}{sp['so_luong']:<10}{sp['don_gia']:^10}{thanh_tien:^15}\n"

phai_tra = float(input('Khach đưa: '))
thua = phai_tra - tong_tien

hoa_don_mau += "=" * 60 + f"\n{'Tổng tiền:':<40}{tong_tien:^15} VNĐ\n" + "=" * 60

if hoa_don["ghi_chu"]:
    hoa_don_mau += f"\nGhi chú: {hoa_don['ghi_chu']}\n" + "=" * 60

pay = tong_tien
paid = phai_tra

c = paid - pay

tien_thoi = {
    "500k": int(c // 500),
    "200k": int((c % 500) // 200),
    "100k": int((c % 200) // 100),
    "50k": int((c % 100) // 50),
    "20k": int((c % 50) // 20),
    "10k": int((c % 20) // 10),
    "5k": int((c % 10) // 5),
    "2k": int((c % 5) // 2),
    "1k": int((c % 2) // 1)
}

for menh_gia, so_to in tien_thoi.items():
    if so_to > 0:
        hoa_don_mau += f"\n{menh_gia}: {so_to}\n"
hoa_don_mau += "=" * 60

with open("hoa_don.txt", "w", encoding="utf-8") as file:
    file.write(hoa_don_mau)

print(hoa_don_mau)

