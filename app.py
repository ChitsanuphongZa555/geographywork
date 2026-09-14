from flask import Flask, render_template

app = Flask(__name__)

places = [
    {
        "name": "Temple of the Emerald Buddha",
        "name_th": "วัดพระแก้ว",
        "province": "Bangkok, Thailand",
        "photo_credit": "Created by ปภินวิช ชาตาสุข",
        "images": ["/static/image/wat1.png","/static/image/wat2.png"],
        "lat": 13.7515,
        "lng": 100.4927
    },
    {
        "name": "Tokyo Tower",
        "name_th": "โตเกียวทาวเวอร์",
        "province": "Tokyo, Japan",
        "photo_credit": "Created by ศรณ์ศีล ชูสัตยานนท์",
        "images": ["/static/image/tokyo1.png","/static/image/tokyo2.png"],
        "lat": 35.6586,
        "lng": 139.7454
    },
    {
        "name": "Eiffel Tower",
        "name_th": "หอไอเฟล",
        "province": "Paris, France",
        "photo_credit": "Created by วชิรวิทย์ ตันรุ่งเรือง",
        "images": [
            "/static/image/eiffel1.png","/static/image/eiffel2.png"
        ],
        "lat": 48.8584,
        "lng": 2.2945
    },
    {
        "name": "Sydney Opera House",
        "name_th": "โรงอุปรากรซิดนีย์",
        "province": "Sydney, Australia",
        "photo_credit": "Created by แทนไทย เตาไธสง",
        "images": ["/static/image/ope1.png","/static/image/ope2.png"],
        "lat": -33.8568,
        "lng": 151.2153
    },
    {
        "name": "Leaning Tower of Pisa",
        "name_th": "หอเอนเมืองปิซ่า",
        "province": "Pisa, Italy",
        "photo_credit": "Created by ณัฎฐ์ธนัน ชื่นบรรลือสุข",
        "images": ["/static/image/pisa1.png","/static/image/pisa2.png"],
        "lat": 43.7230,
        "lng": 10.3966
    },
    {
        "name": "Big Ben",
        "name_th": "หอนาฬิกาบิ๊กเบน",
        "province": "London, United Kingdom",
        "photo_credit": "Created by ธนกฤต กราพงศ์",
        "images": ["/static/image/bigben1.png","/static/image/bigben2.png"],
        "lat": 51.5007,
        "lng": -0.1246
    },
    {
        "name": "Chichen Itza",
        "name_th": "พีระมิดชิเชนอิตซา",
        "province": "Yucatan, Mexico",
        "photo_credit": "Created by แทนเตชิน จันทรลักษณา",
        "images": ["/static/image/chic1.png","/static/image/chic2.png"],
        "lat": 20.6843,
        "lng": -88.5678
    },
    {
        "name": "Statue of Liberty",
        "name_th": "เทพีเสรีภาพ",
        "province": "New York, USA",
        "photo_credit": "Created by ภาวัช วังส์ไพจิตร",
        "images": ["/static/image/state1.png","/static/image/state2.png"],
        "lat": 40.6892,
        "lng": -74.0445
    },
    {
        "name": "Angkor Wat",
        "name_th": "นครวัด",
        "province": "Siem Reap, Cambodia",
        "photo_credit": "Created by ปธานิน ชื่นรัตนกุล",
        "images": ["/static/image/ang1.png","/static/image/ang2.png"],
        "lat": 13.4125,
        "lng": 103.8670
    },
    {
        "name": "Great Pyramid of Giza",
        "name_th": "พีระมิดกีซา",
        "province": "Cairo, Egypt",
        "photo_credit": "Created by ชิษณุพงศ์ ทวีโชติกิจเจริญ",
        "images": ["/static/image/giza1.png","/static/image/giza2.png"],
        "lat": 29.9792,
        "lng": 31.1342
    },
]

@app.route("/")
def home():
    return render_template("index.html", places=places)

if __name__ == "__main__":
    app.run(debug=True)