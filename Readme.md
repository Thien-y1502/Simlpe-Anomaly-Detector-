# 📊 Anomaly Detection using Simple Thresholding

Đây là dự án cá nhân sử dụng phương pháp đơn giản để phát hiện lưu lượng mạng bất thường, sử dụng ngưỡng thống kê dựa trên trung bình và độ lệch chuẩn.

## 🚀 Cách chạy ứng dụng

### 1. Cài đặt thư viện

```bash
pip install -r requirements.txt
```

### 2. Chạy ứng dụng Streamlit

```bash
streamlit run main.py
```

## 📁 Cấu trúc dự án

```
anomaly-detector/
├── main.py                  # Ứng dụng chính
├── data/
│   └── traffic.csv         # Dữ liệu mẫu (nếu có)
├── requirements.txt        # Danh sách thư viện cần cài
└── README.md               # Tài liệu hướng dẫn này
```

## 📈 Dữ liệu mẫu (CSV)

```csv
timestamp,connection_count
2025-05-01 08:00:00,15
2025-05-01 08:01:00,16
2025-05-01 08:02:00,18
2025-05-01 08:03:00,95
2025-05-01 08:04:00,17
2025-05-01 08:05:00,16
2025-05-01 08:06:00,17
2025-05-01 08:07:00,15
2025-05-01 08:08:00,100
2025-05-01 08:09:00,16

```

## 🧠 Kiến thức cần có

* Python cơ bản
* Xử lý dữ liệu với Pandas
* Vẽ biểu đồ với matplotlib
* Giao diện web đơn giản bằng Streamlit
* Kiến thức về thống kê (mean, std deviation)

## 🎯 Ứng dụng thực tế

* Phân tích dữ liệu log mạng
* Phát hiện hành vi bất thường trong bảo mật
* Kiểm tra lưu lượng truy cập tăng đột biến
---

Made with ❤️ for Cybersecurity projects.
