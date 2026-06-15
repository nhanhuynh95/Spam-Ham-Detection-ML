# 1. Dùng một bản Python nhẹ làm nền móng
FROM python:3.10-slim

# 2. Tạo thư mục làm việc bên trong Docker
WORKDIR /code

# 3. Copy file danh sách thư viện vào trước
COPY ./requirement.txt /code/requirement.txt

# 4. Tiến hành cài đặt các thư viện đó bên trong Docker
RUN pip install --no-cache-dir --upgrade -r /code/requirement.txt

# 5. Copy toàn bộ các thư mục chứa code và model vào Docker
COPY ./app /code/app
COPY ./model /code/model
COPY ./templates /code/templates

# 6. Lệnh để kích hoạt server chạy tự động khi bật Docker lên
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]