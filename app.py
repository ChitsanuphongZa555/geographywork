from flask import Flask, render_template

app = Flask(__name__)

places = [
    {
        "name": "Temple of the Emerald Buddha",
        "name_th": "วัดพระแก้ว",
        "province": "Bangkok, Thailand",
        "description": "วัดคู่บ้านคู่เมือง ประดิษฐานพระแก้วมรกต สถาปัตยกรรมงดงามอลังการ",
        "image": "https://commons.wikimedia.org/wiki/Special:FilePath/The_Grand_Palace_@_Bangkok.jpg?width=500",
        "lat": 13.7515,
        "lng": 100.4927
    },
    {
        "name": "Tokyo Tower",
        "name_th": "โตเกียวทาวเวอร์",
        "province": "Tokyo, Japan",
        "description": "หอคอยสัญลักษณ์ของโตเกียว สีแดง-ขาวโดดเด่น ชมวิวเมืองได้แบบ 360 องศา",
        "image": "https://images.unsplash.com/photo-1536098561742-ca998e48cbcc?w=500",
        "lat": 35.6586,
        "lng": 139.7454
    },
    {
        "name": "Eiffel Tower",
        "name_th": "หอไอเฟล",
        "province": "Paris, France",
        "description": "สัญลักษณ์ของกรุงปารีส หอคอยเหล็กสูง 330 เมตร วิวเมืองสวยที่สุดตอนพระอาทิตย์ตก",
        "image": "https://images.unsplash.com/photo-1502602898657-3e91760cbb34?w=500",
        "lat": 48.8584,
        "lng": 2.2945
    },
    {
        "name": "Sydney Opera House",
        "name_th": "โรงอุปรากรซิดนีย์",
        "province": "Sydney, Australia",
        "description": "อาคารสถาปัตยกรรมรูปเปลือกหอยอันโด่งดัง สัญลักษณ์ของประเทศออสเตรเลีย",
        "image": "https://images.unsplash.com/photo-1523059623039-a9ed027e7fad?w=500",
        "lat": -33.8568,
        "lng": 151.2153
    },
    {
        "name": "Leaning Tower of Pisa",
        "name_th": "หอเอนเมืองปิซ่า",
        "province": "Pisa, Italy",
        "description": "หอระฆังเอียงชื่อดัง เกิดจากฐานรากที่ไม่มั่นคง กลายเป็นแลนด์มาร์กที่มีเอกลักษณ์ที่สุดในโลก",
        "image": "https://commons.wikimedia.org/wiki/Special:FilePath/Pisa_Cathedral_and_Pisa_Tower,_Campo_dei_Miracoli_(Field_of_Miracles),_Pisa,_Italy.jpg?width=500",
        "lat": 43.7230,
        "lng": 10.3966
    },
    {
        "name": "Big Ben",
        "name_th": "หอนาฬิกาบิ๊กเบน",
        "province": "London, United Kingdom",
        "description": "หอนาฬิกาอันเป็นสัญลักษณ์ของกรุงลอนดอน ตั้งอยู่ติดกับอาคารรัฐสภาอังกฤษ",
        "image": "https://commons.wikimedia.org/wiki/Special:FilePath/Big_Ben_Elizabeth_Tower_London_2023_01.jpg?width=500",
        "lat": 51.5007,
        "lng": -0.1246
    },
    {
        "name": "Chichen Itza",
        "name_th": "พีระมิดชิเชนอิตซา",
        "province": "Yucatan, Mexico",
        "description": "วิหารโบราณของชาวมายา หนึ่งใน 7 สิ่งมหัศจรรย์ของโลกยุคใหม่ สถาปัตยกรรมล้ำค่าทางดาราศาสตร์",
        "image": "https://images.unsplash.com/photo-1518638150340-f706e86654de?w=500",
        "lat": 20.6843,
        "lng": -88.5678
    },
    {
        "name": "Statue of Liberty",
        "name_th": "เทพีเสรีภาพ",
        "province": "New York, USA",
        "description": "สัญลักษณ์แห่งอิสรภาพและประชาธิปไตย ตั้งอยู่บนเกาะกลางอ่าวนิวยอร์ก",
        "image": "https://commons.wikimedia.org/wiki/Special:FilePath/Statue_of_Liberty,_NY.jpg?width=500",
        "lat": 40.6892,
        "lng": -74.0445
    },
    {
        "name": "Angkor Wat",
        "name_th": "นครวัด",
        "province": "Siem Reap, Cambodia",
        "description": "ปราสาทหินโบราณที่ใหญ่ที่สุดในโลก สถาปัตยกรรมขอมอันวิจิตรงดงาม มรดกโลกของยูเนสโก",
        "image": "https://commons.wikimedia.org/wiki/Special:FilePath/Angkor_Wat_with_its_reflection_(cropped).jpg?width=500",
        "lat": 13.4125,
        "lng": 103.8670
    },
    {
        "name": "Great Pyramid of Giza",
        "name_th": "พีระมิดกีซา",
        "province": "Cairo, Egypt",
        "description": "หนึ่งใน 7 สิ่งมหัศจรรย์ของโลกยุคโบราณที่ยังคงเหลืออยู่จนถึงปัจจุบัน",
        "image": "https://images.unsplash.com/photo-1503177119275-0aa32b3a9368?w=500",
        "lat": 29.9792,
        "lng": 31.1342
    },
]

@app.route("/")
def home():
    return render_template("index.html", places=places)

if __name__ == "__main__":
    app.run(debug=True)