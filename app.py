from flask import Flask, render_template

app = Flask(__name__)

places = [
    {
        "name": "หอไอเฟล",
        "province": "ปารีส, ฝรั่งเศส",
        "description": "สัญลักษณ์ของกรุงปารีส หอคอยเหล็กสูง 330 เมตร วิวเมืองสวยที่สุดตอนพระอาทิตย์ตก",
        "image": "https://th.wikipedia.org/wiki/%E0%B8%AB%E0%B8%AD%E0%B9%84%E0%B8%AD%E0%B9%80%E0%B8%9F%E0%B8%A5",
        "lat": 48.8584,
        "lng": 2.2945
    },
    {
        "name": "กำแพงเมืองจีน",
        "province": "ปักกิ่ง, จีน",
        "description": "กำแพงโบราณที่ยาวที่สุดในโลก สร้างขึ้นเพื่อป้องกันการรุกรานจากศัตรู",
        "image": "https://images.unsplash.com/photo-1508804185872-d7badad00f7d?w=500",
        "lat": 40.4319,
        "lng": 116.5704
    },
    {
        "name": "ทัชมาฮาล",
        "province": "อักรา, อินเดีย",
        "description": "อนุสรณ์สถานหินอ่อนสีขาว สร้างด้วยความรักของจักรพรรดิ สวยงามระดับ 7 สิ่งมหัศจรรย์ของโลก",
        "image": "https://images.unsplash.com/photo-1564507592333-c60657eea523?w=500",
        "lat": 27.1751,
        "lng": 78.0421
    },
    {
        "name": "เทพีเสรีภาพ",
        "province": "นิวยอร์ก, สหรัฐอเมริกา",
        "description": "สัญลักษณ์แห่งอิสรภาพและประชาธิปไตย ตั้งอยู่บนเกาะกลางอ่าวนิวยอร์ก",
        "image": "https://images.unsplash.com/photo-1524492412937-b28074a5d7da?w=500",
        "lat": 40.6892,
        "lng": -74.0445
    },
    {
        "name": "โคลอสเซียม",
        "province": "โรม, อิตาลี",
        "description": "สนามกีฬากลางแจ้งขนาดใหญ่สมัยโรมันโบราณ สถาปัตยกรรมที่ยิ่งใหญ่และเก่าแก่กว่า 2,000 ปี",
        "image": "https://images.unsplash.com/photo-1552832230-c0197dd311b5?w=500",
        "lat": 41.8902,
        "lng": 12.4922
    },
    {
        "name": "พีระมิดกีซา",
        "province": "ไคโร, อียิปต์",
        "description": "หนึ่งใน 7 สิ่งมหัศจรรย์ของโลกยุคโบราณที่ยังคงเหลืออยู่จนถึงปัจจุบัน",
        "image": "https://images.unsplash.com/photo-1503177119275-0aa32b3a9368?w=500",
        "lat": 29.9792,
        "lng": 31.1342
    },
    {
        "name": "ซิดนีย์โอเปร่าเฮาส์",
        "province": "ซิดนีย์, ออสเตรเลีย",
        "description": "อาคารสถาปัตยกรรมรูปเปลือกหอยอันโด่งดัง สัญลักษณ์ของประเทศออสเตรเลีย",
        "image": "https://images.unsplash.com/photo-1524293581917-878a6d017c71?w=500",
        "lat": -33.8568,
        "lng": 151.2153
    },
    {
        "name": "มาชูปิกชู",
        "province": "เปรู",
        "description": "เมืองโบราณของชาวอินคาบนยอดเขาแอนดีส สวยงามลึกลับท่ามกลางหมอกและภูเขา",
        "image": "https://images.unsplash.com/photo-1526392060635-9d6019884377?w=500",
        "lat": -13.1631,
        "lng": -72.5450
    },
]

@app.route("/")
def home():
    return render_template("index.html", places=places)

if __name__ == "__main__":
    app.run(debug=True)