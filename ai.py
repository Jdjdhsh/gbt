import requests
import concurrent.futures
import time

# Địa chỉ URL để kiểm tra
url = "https://l7.count123.org/test.php"  # Thay đổi thành URL bạn muốn kiểm tra

# Số lượng yêu cầu và số lượng worker
num_requests = 1000000000  # Số lượng yêu cầu cần gửi
num_workers = 10000000    # Số lượng yêu cầu đồng thời

# Hàm gửi yêu cầu
def send_request():
    try:
        response = requests.get(url)
        return response.status_code
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"

# Thời gian bắt đầu
start_time = time.time()

# Gửi yêu cầu đồng thời
with concurrent.futures.ThreadPoolExecutor(max_workers=num_workers) as executor:
    futures = [executor.submit(send_request) for _ in range(num_requests)]
    results = [future.result() for future in concurrent.futures.as_completed(futures)]

# Thời gian hoàn thành
end_time = time.time()

# Hiển thị kết quả
print(f"Thời gian hoàn thành: {end_time - start_time} giây")
print(f"Tổng số yêu cầu: {num_requests}")
print(f"Phản hồi: {results}")
