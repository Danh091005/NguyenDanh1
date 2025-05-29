![Uploading image.png…]()

Nguyễn Thanh danh -CNTT 17-07
Cách Thức Hoạt Động của Ứng Dụng Kiểm Tra Tính Toàn Vẹn Tệp Ảnh

* Mã Nguồn
Mã nguồn bao gồm các phần chính:
Thư viện cần thiết: Import các thư viện Flask và hashlib.
HTML Template: Mẫu HTML được định nghĩa trong biến html_template, bao gồm cả CSS để tạo kiểu cho giao diện.
Hàm Tính Băm: Hàm calculate_hash tính toán băm SHA-256 cho tệp ảnh được tải lên.
Routings: Định nghĩa các route cho ứng dụng.
* Giao Diện Web
Giao diện web cho phép người dùng:
Tải lên tệp ảnh.
Nhập băm đã lưu trước đó.
Nhấn nút "Kiểm tra" để xác nhận tính toàn vẹn.
* Quy Trình Hoạt Động
Khi người dùng mở trang:
Giao diện HTML được hiển thị với một biểu mẫu cho phép tải lên tệp và nhập băm.
Khi người dùng gửi biểu mẫu:
Ứng dụng nhận tệp ảnh và băm đã lưu từ người dùng.
Gọi hàm calculate_hash để tính toán băm SHA-256 cho tệp ảnh được tải lên.
So sánh băm hiện tại với băm đã lưu.
Hiển thị kết quả:
Nếu hai băm khớp, hiển thị thông báo rằng tệp không bị thay đổi.
Nếu không khớp, hiển thị thông báo rằng tệp đã bị thay đổi.
* Chạy Ứng Dụng
Lưu mã vào một tệp Python (ví dụ: app.py).
Chạy ứng dụng với lệnh:
bash


Mở trình duyệt và truy cập http://127.0.0.1:5000/ để sử dụng ứng dụng.
