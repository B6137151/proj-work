
ProjWork FastAPI Project

การตั้งค่าและรันโปรเจค FastAPI ที่เชื่อมต่อกับฐานข้อมูล PostgreSQL

ขั้นตอนที่ 1: คลอนโค้ดจาก Git Repository
bash
git clone <repository-url>
cd <repository-directory>

ขั้นตอนที่ 2: ติดตั้งและตั้งค่า Docker
ติดตั้ง Docker และ Docker Compose หากยังไม่มี สามารถติดตั้งได้จาก:
- Docker: https://docs.docker.com/get-docker/
- Docker Compose: https://docs.docker.com/compose/install/

ขั้นตอนที่ 3: สร้างและเปิดใช้งาน Virtual Environment
สร้าง virtual environment:
bash
python3 -m venv venv

จากนั้นเปิดใช้งาน virtual environment:
bash
# สำหรับ macOS/Linux
source venv/bin/activate

# สำหรับ Windows
venv\Scripts\activate

ขั้นตอนที่ 4: ติดตั้ง Dependencies
ติดตั้ง dependencies จากไฟล์ requirements.txt:
bash
pip install -r requirements.txt

ขั้นตอนที่ 5: ตั้งค่าและรัน Docker Compose
ตั้งค่าและรัน Docker Compose เพื่อเริ่มฐานข้อมูล PostgreSQL:
bash
docker-compose up

ขั้นตอนที่ 6: รันแอปพลิเคชัน FastAPI
หลังจากที่ฐานข้อมูล PostgreSQL รันแล้ว รันแอปพลิเคชัน FastAPI โดยใช้ Uvicorn:
bash
uvicorn internal.main:app --reload

การใช้งาน API
- เข้าถึงเอกสาร API ที่สร้างขึ้นโดยอัตโนมัติได้ที่ http://localhost:8000/docs
- ในหน้าเอกสารนี้ สามารถทดสอบ endpoints ต่าง ๆ รวมถึง endpoint สำหรับสร้างผู้ใช้ใหม่ (/users/) ได้

ด้วยคำแนะนำเหล่านี้ เค้าจะสามารถตั้งค่าและรันโปรเจค FastAPI ของเธอได้อย่างสมบูรณ์

