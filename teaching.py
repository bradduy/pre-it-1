class HocVien:
    def __init__(self, ten, tuoi, ho_so_da_nop):
        self.ten = ten
        self.tuoi = tuoi
        self.ho_so_da_nop = ho_so_da_nop  # danh sách tên các loại hồ sơ

    def thong_tin(self):
        print(f"Học viên: {self.ten}, Tuổi: {self.tuoi}")
        print(f"Đã nộp hồ sơ: {', '.join(self.ho_so_da_nop)}\n")

class TrungTamTiengHan:
    def __init__(self, ten_trung_tam):
        self.ten_trung_tam = ten_trung_tam
        self.danh_sach_hoc_vien = []

    def them_hoc_vien(self, hoc_vien):
        self.danh_sach_hoc_vien.append(hoc_vien)
        print(f"✅ Đã thêm học viên: {hoc_vien.ten}")

    def liet_ke_hoc_vien(self):
        print(f"\n📋 Danh sách học viên tại {self.ten_trung_tam}:")
        for hv in self.danh_sach_hoc_vien:
            hv.thong_tin()

    def tim_kiem_theo_ten(self, tu_khoa):
        print(f"\n🔍 Kết quả tìm kiếm tên chứa '{tu_khoa}':")
        for hv in self.danh_sach_hoc_vien:
            if tu_khoa.lower() in hv.ten.lower():
                hv.thong_tin()

# Tạo trung tâm
trung_tam = TrungTamTiengHan("BradDuy Academny")

# Tạo học viên
hv1 = HocVien("Nguyen Van A", 22, ["Học bạ", "CMND", "Bằng tốt nghiệp"])
hv2 = HocVien("Le Thi B", 20, ["CMND", "Giấy khai sinh"])
hv3 = HocVien("Pham Minh C", 23, ["Học bạ", "Passport"])

# Thêm học viên vào trung tâm
trung_tam.them_hoc_vien(hv1)
trung_tam.them_hoc_vien(hv2)
trung_tam.them_hoc_vien(hv3)

# Liệt kê học viên
trung_tam.liet_ke_hoc_vien()

# Tìm kiếm theo tên
trung_tam.tim_kiem_theo_ten("minh")

l = [1,2,3]
print(dir(l))