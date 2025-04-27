# Chú thích code của Nguyên
# Tạo lớp TaiLieu (Tài Liệu)
class TaiLieu:
    def __init__(self, ma_tai_lieu, ten_nxb, so_ban_phat_hanh): #Hàm khởi tạo với 3 thuộc tính: mã tài liệu, tên nhà xuất bản, số bản phát hành
        self.__ma_tai_lieu = ma_tai_lieu #Thuộc tính mã tài liệu (private)
        self.__ten_nxb = ten_nxb #Thuộc tính tên nhà xuất bản (private)
        self.__so_ban_phat_hanh = so_ban_phat_hanh #Thuộc tính số bản phát hành (private)

    def get_ma_tai_lieu(self): #Phương thức getter để truy cập thuộc tính mã tài liệu (private)
        return self.__ma_tai_lieu

    def set_ma_tai_lieu(self, ma): #Phương thức setter để truy cập thuộc tính mã tài liệu (private)
        self.__ma_tai_lieu = ma

    def get_ten_nxb(self): #Phương thức getter để truy cập thuộc tính tên nhà xuất bản (private)
        return self.__ten_nxb

    def set_ten_nxb(self, nxb): #Phương thức setter để truy cập thuộc tính tên nhà xuất bản (private)
        self.__ten_nxb = nxb

    def get_so_ban_phat_hanh(self): #Phương thức getter để truy cập thuộc tính số bản phát hành (private)
        return self.__so_ban_phat_hanh

    def set_so_ban_phat_hanh(self, so_ban): #Phương thức setter để truy cập thuộc tính số bản phát hành (private)
        self.__so_ban_phat_hanh = so_ban

    def thong_tin(self): #Phương thức hiển thị thông tin cơ bản của tài liệu
        print(f"Mã TL: {self.get_ma_tai_lieu()}, NXB: {self.get_ten_nxb()}, Số bản: {self.get_so_ban_phat_hanh()}")


#Tạo lớp Sach (sách) kế thừa từ lớp TaiLieu
class Sach(TaiLieu):
    def __init__(self, ma_tai_lieu, ten_nxb, so_ban_phat_hanh, so_trang, ten_tg): #Hàm khởi tạo, kế thừa các thuộc tính của TaiLieu, thêm số trang và tên tác giả
        super().__init__(ma_tai_lieu, ten_nxb, so_ban_phat_hanh) #Gọi hàm khởi tạo của lớp cha
        self.__so_trang = so_trang #Thuộc tính số trang (private)
        self.__ten_tg = ten_tg #Thuộc tính tên tác giả (private)

    def get_so_trang(self): #Phương thức getter để truy cập thuộc tính số trang (private)
        return self.__so_trang

    def set_so_trang(self, so): #Phương thức setter để truy cập thuộc tính số trang (private)
        self.__so_trang = so

    def get_ten_tg(self): #Phương thức getter để truy cập thuộc tính tên tác giả (private)
        return self.__ten_tg

    def set_ten_tg(self, ten): #Phương thức setter để truy cập thuộc tính tên tác giả (private)
        self.__ten_tg = ten

    def thong_tin(self): #Ghi đè phương thứC hiển thị thông tin, thêm thông tin của sách
        super().thong_tin()
        print(f"Tác giả: {self.get_ten_tg()}, Số trang: {self.get_so_trang()}")


# Tạo lớp TapChi (tạp chí) kế thừa từ lớp TaiLieu
class TapChi(TaiLieu):
    def __init__(self, ma_tai_lieu, ten_nxb, so_ban_phat_hanh, so_phat_hanh, thang_phat_hanh): #Hàm khởi tạo với 3 thuộc tính: mã tài liệu, tên nhà xuất bản, số bản phát hành
        super().__init__(ma_tai_lieu, ten_nxb, so_ban_phat_hanh) #Hàm khởi tạo mở rộng từ TaiLieu, thêm thuộc tính số phát hành và tháng phát hành
        self.__so_phat_hanh = so_phat_hanh #Thuộc tính số phát hành (private)
        self.__thang_phat_hanh = thang_phat_hanh #Thuộc tính tháng phát hành (private)

    def get_so_phat_hanh(self): #Phương thức getter để truy cập thuộc tính số phát hành (private)
        return self.__so_phat_hanh

    def set_so_phat_hanh(self, so): #Phương thức setter để truy cập thuộc tính số phát hành (private)
        self.__so_phat_hanh = so

    def get_thang_phat_hanh(self): #Phương thức getter để truy cập thuộc tính tháng phát hành (private)
        return self.__thang_phat_hanh

    def set_thang_phat_hanh(self, thang):#Phương thức Setter để truy cập thuộc tính tháng phát hành (private)
        self.__thang_phat_hanh = thang

    def thong_tin(self): #Ghi đè phương thứC hiển thị thông tin, thêm thông tin của tạp chí
        super().thong_tin()
        print(f"Số phát hành: {self.get_so_phat_hanh()}, Tháng phát hành: {self.get_thang_phat_hanh()}")


# Tạo lớp Bao (báo) kế thừa từ TaiLieu
class Bao(TaiLieu):
    def __init__(self, ma_tai_lieu, ten_nxb, so_ban_phat_hanh, ngay_phat_hanh):
        super().__init__(ma_tai_lieu, ten_nxb, so_ban_phat_hanh)
        self.__ngay_phat_hanh = ngay_phat_hanh

    def get_ngay_phat_hanh(self):
        return self.__ngay_phat_hanh

    def set_ngay_phat_hanh(self, ngay):
        self.__ngay_phat_hanh = ngay

    def thong_tin(self):
        super().thong_tin()
        print(f"Ngày phát hành: {self.get_ngay_phat_hanh()}")


# Tạo lớp QuanLySach (quản lý sách)
class QuanLySach:
    def __init__(self): #Hàm khởi tạo
        self.danh_sach = [] #Khởi tạo danh sách trống để lưu trữ tài liệu

    def them_tai_lieu(self, tai_lieu): #Phương thức thêm tài liệu vào danh sách
        self.danh_sach.append(tai_lieu) #Thêm tài liệu vào cuối danh sách

    def xoa_tai_lieu(self, ma_tai_lieu): #Phương thức xóa tài liệu dựa trên mã tài liệu
        self.danh_sach = [tl for tl in self.danh_sach if tl.get_ma_tai_lieu() != ma_tai_lieu]
        print("Đã xoá tài liệu.")

    def hien_thi_thong_tin(self): #Phương thức hiển thị thông tin các tài liệu
        for tl in self.danh_sach:
            tl.thong_tin()
            print("---------")

    def tim_kiem_theo_loai(self, loai): #Phương thức tìm kiếm tài liệu theo loại (sách/tạp chí/báo)
        loai_tai_lieu = {
            "sach": Sach,
            "tapchi": TapChi,
            "bao": Bao
        }

        if loai not in loai_tai_lieu: #Kiểm tra nếu loại tài liệu không tồn tại
            print("Không tìm thấy loại tài liệu.")
            return

        for tl in self.danh_sach: #Hiển thị thông tin các tài liệu thuộc loại cần tìm
            if isinstance(tl, loai_tai_lieu[loai]): #Kiểm tra kiểu của đối tượng
                tl.thong_tin()
                print("---------")


def menu(): #Hàm hiển thị menu và xử lý lựa chọn
    ql = QuanLySach() #Tạo đối tượng quản lý danh sách

    while True: #Sử dụng vòng lặp vô hạn để hiển thị Menu liên tục
        print("\n--- DANH SÁCH TÀI LIỆU ---")
        print("1. Thêm tài liệu")
        print("2. Xoá tài liệu")
        print("3. Hiển thị thông tin tài liệu")
        print("4. Tìm kiếm theo loại")
        print("5. Thoát")

        lua_chon = input("Chọn chức năng (1-5): ")

        if lua_chon == "1": #Xử lý thêm tài liệu mới
            print("\n1. Sách | 2. Tạp chí | 3. Báo")
            loai = input("Chọn loại tài liệu: ")

            #Thêm thông tin chung cho tài liệu
            ma = input("Mã tài liệu: ")
            nxb = input("Nhà xuất bản: ")
            so_ban = int(input("Số bản phát hành: "))

            if loai == "1":
                #Nhập thông tin riêng cho sách
                tac_gia = input("Tên tác giả: ")
                so_trang = int(input("Số trang: "))
                sach = Sach(ma, nxb, so_ban, so_trang, tac_gia)
                ql.them_tai_lieu(sach)

            elif loai == "2":
                #Nhập thông tin riêng cho tạp chí
                so_ph = int(input("Số phát hành: "))
                thang_ph = input("Tháng phát hành: ")
                tap_chi = TapChi(ma, nxb, so_ban, so_ph, thang_ph)
                ql.them_tai_lieu(tap_chi)

            elif loai == "3":
                #Nhập thông tin riêng cho báo
                ngay_ph = input("Ngày phát hành: ")
                bao = Bao(ma, nxb, so_ban, ngay_ph)
                ql.them_tai_lieu(bao)

        elif lua_chon == "2":
            #Xử lý xóa tài liệu theo mã
            ma = input("Nhập mã tài liệu cần xoá: ")
            ql.xoa_tai_lieu(ma)

        elif lua_chon == "3":
            #Xử lý hiển thị toàn bộ thông tin tài liệu
            ql.hien_thi_thong_tin()

        elif lua_chon == "4":
            #Xử lý tìm kiếm tài liệu theo thể loại
            loai = input("Nhập thể loại (sach/tapchi/bao): ").lower()
            ql.tim_kiem_theo_loai(loai)

        elif lua_chon == "5":
            #Xử lý thoát chương trình
            print("Thoát chương trình")
            break

        else:
            #Xử lý lựa chọn không hợp lệ
            print("Lựa chọn không hợp lệ!")


#Gọi hàm menu để bắt đầu chương trình
menu()
