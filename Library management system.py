import tkinter as tk
from tkinter import ttk, messagebox, simpledialog

class LibraryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Hệ thống Quản lý Thư viện")
        self.books = ["Tiếng Anh", "Hóa học", "Toán học", "Vật lý", "Tin học", "Phần mềm"]
        self.create_widgets()

    def create_widgets(self):
        # Tạo thanh Menu
        self.menu = tk.Menu(self.root)
        self.root.config(menu=self.menu)
        self.file_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Tệp", menu=self.file_menu)
        self.file_menu.add_command(label="Lưu", command=self.save_books)
        self.file_menu.add_command(label="Tải", command=self.load_books)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Thoát", command=self.root.quit)

        # Tạo khung chính
        self.main_frame = ttk.Frame(self.root, padding="10")
        self.main_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        # Nút Thêm sách
        self.add_book_button = ttk.Button(self.main_frame, text="Thêm sách", command=self.add_book)
        self.add_book_button.grid(row=0, column=0, padx=10, pady=5)

        # Nút Xem sách
        self.view_books_button = ttk.Button(self.main_frame, text="Xem sách", command=self.view_books)
        self.view_books_button.grid(row=0, column=1, padx=10, pady=5)

        # Nút Tìm kiếm sách
        self.search_book_button = ttk.Button(self.main_frame, text="Tìm kiếm sách", command=self.search_book)
        self.search_book_button.grid(row=0, column=2, padx=10, pady=5)

        # Thanh trạng thái
        self.status = tk.StringVar()
        self.status.set("Sẵn sàng")
        self.status_bar = ttk.Label(self.root, textvariable=self.status, relief="sunken", anchor='w', padding="5")
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)

    def add_book(self):
        book_name = simpledialog.askstring("Thêm sách", "Nhập tên sách:")
        if book_name:
            if book_name not in self.books:
                self.books.append(book_name)
                self.status.set(f"'{book_name}' đã được thêm.")
            else:
                self.status.set(f"'{book_name}' đã tồn tại.")
            self.update_status()
        else:
            self.status.set("Chưa nhập tên sách!")
            self.update_status()

    def view_books(self):
        if self.books:
            books_list = "\n".join(self.books)
            number_of_books = len(self.books)
            messagebox.showinfo("Sách trong thư viện", f"Các sách:\n{books_list}\n\nTổng số sách: {number_of_books}")
        else:
            messagebox.showinfo("Sách trong thư viện", "Không có sách nào.")

    def search_book(self):
        search_term = simpledialog.askstring("Tìm kiếm sách", "Nhập tên sách để tìm kiếm:")
        if search_term:
            if search_term in self.books:
                messagebox.showinfo("Kết quả tìm kiếm", f"'{search_term}' có trong thư viện.")
            else:
                messagebox.showinfo("Kết quả tìm kiếm", f"'{search_term}' không có trong thư viện.")
        else:
            messagebox.showwarning("Lỗi nhập liệu", "Chưa nhập từ khóa tìm kiếm!")

    def save_books(self):
        # Chức năng Lưu (chưa khả dụng)
        messagebox.showinfo("Chức năng Lưu", "Chức năng lưu chưa khả dụng trong phiên bản này.")

    def load_books(self):
        # Chức năng Tải (chưa khả dụng)
        messagebox.showinfo("Chức năng Tải", "Chức năng tải chưa khả dụng trong phiên bản này.")

    def update_status(self):
        self.status_bar.config(text=self.status.get())

if __name__ == "__main__":
    root = tk.Tk()
    app = LibraryApp(root)
    root.mainloop()
