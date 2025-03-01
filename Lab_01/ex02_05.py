so_gio_lam = float(input("Nhập số giờ làm mỗi tuần: "))
luong_gio = float(input("Nhập lương mỗi giờ: "))
gio_tuan_chuan = 44
gio_vuot_chuan = max(0, so_gio_lam - gio_tuan_chuan)
thuc_linh = so_gio_lam * luong_gio + gio_vuot_chuan * luong_gio * 1.5
print(f"Số tiền lương thực lĩnh của nhân viên là: {thuc_linh}")