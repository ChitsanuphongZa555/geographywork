from flask import Flask, render_template

app = Flask(__name__)

# ใส่สถานที่เพิ่มทีหลังตรงนี้ พิกัดเป็นแบบ Decimal Degree (lat, lng)
# ตัวอย่างโครงสร้าง:
# {"name": "ชื่อสถานที่", "province": "เมือง, ประเทศ", "description": "รายละเอียด", "image": "URL รูป", "lat": 0.0000, "lng": 0.0000}
places = []

@app.route("/")
def home():
    return render_template("index.html", places=places)

if __name__ == "__main__":
    app.run(debug=True)