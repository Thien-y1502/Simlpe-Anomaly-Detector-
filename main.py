import pandas as pd
import matplotlib.pyplot as plt

# Đọc dữ liệu
data = pd.read_csv("data/traffic.csv", parse_dates=['timestamp'])

# Tính ngưỡng dựa trên thống kê
mean_val = data['connection_count'].mean()
std_val = data['connection_count'].std()
threshold = mean_val + 2 * std_val

# Gắn cờ bất thường
data['anomaly'] = data['connection_count'] > threshold

# In thông tin
print(f"Ngưỡng phát hiện bất thường: {threshold:.2f}")
print("Các điểm bất thường:")
print(data[data['anomaly']])

# Vẽ biểu đồ
plt.figure(figsize=(10, 5))
plt.plot(data['timestamp'], data['connection_count'], label="Lưu lượng")
plt.axhline(threshold, color='red', linestyle='--', label=f"Ngưỡng ({threshold:.2f})")
plt.scatter(data[data['anomaly']]['timestamp'],
            data[data['anomaly']]['connection_count'],
            color='red', label='Bất thường')
plt.xlabel("Thời gian")
plt.ylabel("Số kết nối")
plt.title("Phát hiện bất thường tự động (Mean + 2*Std)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
