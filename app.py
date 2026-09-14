from flask import Flask, render_template

app = Flask(__name__)

places = [
    {
        "name": "Temple of the Emerald Buddha",
        "name_th": "วัดพระแก้ว",
        "province": "Bangkok, Thailand",
        "photo_credit": "Created by ปภินวิช ชาตาสุข",
        "images": ["https://commons.wikimedia.org/wiki/Special:FilePath/The_Grand_Palace_@_Bangkok.jpg?width=800"],
        "lat": 13.7515,
        "lng": 100.4927
    },
    {
        "name": "Tokyo Tower",
        "name_th": "โตเกียวทาวเวอร์",
        "province": "Tokyo, Japan",
        "photo_credit": "Created by ศรณ์ศีล ชูสัตยานนท์",
        "images": ["https://images.unsplash.com/photo-1536098561742-ca998e48cbcc?w=800"],
        "lat": 35.6586,
        "lng": 139.7454
    },
    {
        "name": "Eiffel Tower",
        "name_th": "หอไอเฟล",
        "province": "Paris, France",
        "photo_credit": "Created by วชิรวิทย์ ตันรุ่งเรือง",
        "images": [
            "https://commons.wikimedia.org/wiki/Special:FilePath/Tour_Eiffel_Wikimedia_Commons.jpg?width=800",
            "https://commons.wikimedia.org/wiki/Special:FilePath/Eiffel_Tower_in_2022_02.jpg?width=800"
        ],
        "lat": 48.8584,
        "lng": 2.2945
    },
    {
        "name": "Sydney Opera House",
        "name_th": "โรงอุปรากรซิดนีย์",
        "province": "Sydney, Australia",
        "photo_credit": "Created by แทนไทย เตาไธสง",
        "images": ["https://images.unsplash.com/photo-1523059623039-a9ed027e7fad?w=800"],
        "lat": -33.8568,
        "lng": 151.2153
    },
    {
        "name": "Leaning Tower of Pisa",
        "name_th": "หอเอนเมืองปิซ่า",
        "province": "Pisa, Italy",
        "photo_credit": "Created by ณัฎฐ์ธนัน ชื่นบรรลือสุข",
        "images": ["https://commons.wikimedia.org/wiki/Special:FilePath/Pisa_Cathedral_and_Pisa_Tower,_Campo_dei_Miracoli_(Field_of_Miracles),_Pisa,_Italy.jpg?width=800"],
        "lat": 43.7230,
        "lng": 10.3966
    },
    {
        "name": "Big Ben",
        "name_th": "หอนาฬิกาบิ๊กเบน",
        "province": "London, United Kingdom",
        "photo_credit": "Created by ธนกฤต กราพงศ์",
        "images": ["https://commons.wikimedia.org/wiki/Special:FilePath/Big_Ben_Elizabeth_Tower_London_2023_01.jpg?width=800"],
        "lat": 51.5007,
        "lng": -0.1246
    },
    {
        "name": "Chichen Itza",
        "name_th": "พีระมิดชิเชนอิตซา",
        "province": "Yucatan, Mexico",
        "photo_credit": "Created by แทนเตชิน จันทรลักษณา",
        "images": ["https://images.unsplash.com/photo-1518638150340-f706e86654de?w=800"],
        "lat": 20.6843,
        "lng": -88.5678
    },
    {
        "name": "Statue of Liberty",
        "name_th": "เทพีเสรีภาพ",
        "province": "New York, USA",
        "photo_credit": "Created by ภาวัช วังส์ไพจิตร",
        "images": ["https://commons.wikimedia.org/wiki/Special:FilePath/Statue_of_Liberty,_NY.jpg?width=800"],
        "lat": 40.6892,
        "lng": -74.0445
    },
    {
        "name": "Angkor Wat",
        "name_th": "นครวัด",
        "province": "Siem Reap, Cambodia",
        "photo_credit": "Created by ปธานิน ชื่นรัตนกุล",
        "images": ["https://commons.wikimedia.org/wiki/Special:FilePath/Angkor_Wat_with_its_reflection_(cropped).jpg?width=800"],
        "lat": 13.4125,
        "lng": 103.8670
    },
    {
        "name": "Great Pyramid of Giza",
        "name_th": "พีระมิดกีซา",
        "province": "Cairo, Egypt",
        "photo_credit": "Created by ชิษณุพงศ์ ทวีโชติกิจเจริญ",
        "images": ["https://images.unsplash.com/photo-1503177119275-0aa32b3a9368?w=800"],
        "lat": 29.9792,
        "lng": 31.1342
    },
]

@app.route("/")
def home():
    return render_template("index.html", places=places)

if __name__ == "__main__":
    app.run(debug=True)