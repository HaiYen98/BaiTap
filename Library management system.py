import tkinter as tk
from tkinter import ttk, messagebox, simpledialog

# Lớp Tài Liệu
class TaiLieu:
    def __init__(self, ma_tai_lieu, ten_nxb, so_ban_phat_hanh):
        self.__ma_tai_lieu = ma_tai_lieu
        self.__ten_nxb = ten_nxb
        self.__so_ban_phat_hanh = so_ban_phat_hanh

    def get_ma_tai_lieu(self):
        return self.__ma_tai_lieu

    def get_thong_tin(self):
        return f"Mã TL: {self.__ma_tai_lieu}, NXB: {self.__ten_nxb}, Số bản: {self.__so_ban_phat_hanh}"

# Lớp Sách kế thừa Tài Liệu
class Sach(TaiLieu):
    def __init__(self, ma_tai_lieu, ten_nxb, so_ban_phat_hanh, so_trang, ten_tac_gia):
        super().__init__(ma_tai_lieu, ten_nxb, so_ban_phat_hanh)
        self.__so_trang = so_trang
        self.__ten_tac_gia = ten_tac_gia

    def get_thong_tin(self):
        return super().get_thong_tin() + f", Tác giả: {self.__ten_tac_gia}, Số trang: {self.__so_trang}"

# Lớp Tạp chí kế thừa Tài Liệu
class TapChi(TaiLieu):
    def __init__(self, ma_tai_lieu, ten_nxb, so_ban_phat_hanh, so_phat_hanh, thang_phat_hanh):
        super().__init__(ma_tai_lieu, ten_nxb, so_ban_phat_hanh)
        self.__so_phat_hanh = so_phat_hanh
        self.__thang_phat_hanh = thang_phat_hanh

    def get_thong_tin(self):
        return super().get_thong_tin() + f", Số phát hành: {self.__so_phat_hanh}, Tháng: {self.__thang_phat_hanh}"

# Lớp Báo kế thừa Tài Liệu
class Bao(TaiLieu):
    def __init__(self, ma_tai_lieu, ten_nxb, so_ban_phat_hanh, ngay_phat_hanh):
        super().__init__(ma_tai_lieu, ten_nxb, so_ban_phat_hanh)
        self.__ngay_phat_hanh = ngay_phat_hanh

    def get_thong_tin(self):
        return super().get_thong_tin() + f", Ngày phát hành: {self.__ngay_phat_hanh}"

# Lớp Quản lý sách
class QuanLySach:
    def __init__(self):
        self.danh_sach = []

    def them_tai_lieu(self, tai_lieu):
        self.danh_sach.append(tai_lieu)

    def tim_kiem(self, ma_tai_lieu):
        for tl in self.danh_sach:
            if tl.get_ma_tai_lieu() == ma_tai_lieu:
                return tl
        return None

    def xoa_tai_lieu(self, ma_tai_lieu):
        self.danh_sach = [tl for tl in self.danh_sach if tl.get_ma_tai_lieu() != ma_tai_lieu]

    def lay_toan_bo(self):
        return self.danh_sach

# Giao diện tkinter
class LibraryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quản Lý Thư Viện")
        self.quan_ly = QuanLySach()
        self.create_widgets()

    def create_widgets(self):
        frame = ttk.Frame(self.root, padding="10")
        frame.pack(fill=tk.BOTH, expand=True)

        ttk.Button(frame, text="Thêm Tài Liệu", command=self.them_tai_lieu).grid(row=0, column=0, padx=10, pady=5)
        ttk.Button(frame, text="Xem Danh Sách", command=self.xem_danh_sach).grid(row=0, column=1, padx=10, pady=5)
        ttk.Button(frame, text="Tìm Kiếm", command=self.tim_kiem).grid(row=0, column=2, padx=10, pady=5)
        ttk.Button(frame, text="Xóa Tài Liệu", command=self.xoa_tai_lieu).grid(row=0, column=3, padx=10, pady=5)

        self.status = tk.StringVar(value="Sẵn sàng")
        ttk.Label(self.root, textvariable=self.status, relief="sunken", anchor="w").pack(side=tk.BOTTOM, fill=tk.X)

    def them_tai_lieu(self):
        loai = simpledialog.askstring("Loại tài liệu", "Nhập loại (sach/tapchi/bao):").lower()
        ma = simpledialog.askstring("Mã tài liệu", "Nhập mã tài liệu:")
        nxb = simpledialog.askstring("Nhà xuất bản", "Nhập tên nhà xuất bản:")
        so_ban = simpledialog.askinteger("Số bản", "Nhập số bản phát hành:")

        if loai == "sach":
            tac_gia = simpledialog.askstring("Tác giả", "Nhập tên tác giả:")
            so_trang = simpledialog.askinteger("Số trang", "Nhập số trang:")
            sach = Sach(ma, nxb, so_ban, so_trang, tac_gia)
            self.quan_ly.them_tai_lieu(sach)
        elif loai == "tapchi":
            so_ph = simpledialog.askinteger("Số phát hành", "Nhập số phát hành:")
            thang_ph = simpledialog.askstring("Tháng phát hành", "Nhập tháng phát hành:")
            tap_chi = TapChi(ma, nxb, so_ban, so_ph, thang_ph)
            self.quan_ly.them_tai_lieu(tap_chi)
        elif loai == "bao":
            ngay_ph = simpledialog.askstring("Ngày phát hành", "Nhập ngày phát hành:")
            bao = Bao(ma, nxb, so_ban, ngay_ph)
            self.quan_ly.them_tai_lieu(bao)
        else:
            messagebox.showerror("Lỗi", "Loại tài liệu không hợp lệ!")
            return

        self.status.set(f"Đã thêm {loai} thành công!")

    def xem_danh_sach(self):
        danh_sach = self.quan_ly.lay_toan_bo()
        if not danh_sach:
            messagebox.showinfo("Danh Sách", "Không có tài liệu nào.")
        else:
            info = "\n\n".join([tl.get_thong_tin() for tl in danh_sach])
            messagebox.showinfo("Danh Sách Tài Liệu", info)

    def tim_kiem(self):
        ma = simpledialog.askstring("Tìm kiếm", "Nhập mã tài liệu:")
        tai_lieu = self.quan_ly.tim_kiem(ma)
        if tai_lieu:
            messagebox.showinfo("Kết Quả", tai_lieu.get_thong_tin())
        else:
            messagebox.showinfo("Kết Quả", "Không tìm thấy tài liệu.")

    def xoa_tai_lieu(self):
        ma = simpledialog.askstring("Xóa", "Nhập mã tài liệu cần xóa:")
        if self.quan_ly.tim_kiem(ma):
            self.quan_ly.xoa_tai_lieu(ma)
            self.status.set(f"Đã xoá tài liệu có mã {ma}")
        else:
            messagebox.showinfo("Thông báo", "Không tìm thấy tài liệu.")

if __name__ == "__main__":
    root = tk.Tk()
    app = LibraryApp(root)
    root.mainloop()
