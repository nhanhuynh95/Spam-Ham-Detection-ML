terminal
python -m uvicorn app.main:app --reload

Lệnh uvicorn app.main:app có nghĩa là:

app.main: Hãy tìm file main.py nằm trong folder app.

:app: Bên trong file đó, hãy tìm biến có tên là app (đây chính là đối tượng FastAPI của bạn).

Nếu bạn đặt tên biến là my_api = FastAPI(), thì bạn phải chạy lệnh uvicorn app.main:my_api --reload.

hãy mở file app/main.py lên và kiểm tra xem đã có dòng app = FastAPI(...) chưa? 
Nếu có rồi, hãy copy toàn bộ nội dung file đó dán vào đây, tôi sẽ chỉ ra ngay dòng nào đang làm hệ thống bị lỗi!

install sqlite viewer to see 
====
access Browser http://127.0.0.1:8000/docs
Will see Swagger UI interface - this is API automated

http://127.0.0.1:8000/ui




===

pip install pandas matplotlib seaborn nltk wordcloud scikit-learn

pip install fastapi uvicorn scikit-learn pydantic joblib numpy

python -m uvicorn app.main:app --reload
uvicorn app.main:app --reload
docker build -t spam-detection-app .
====