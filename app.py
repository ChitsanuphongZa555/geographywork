from flask import Flask, render_template

app = Flask(__name__)

places = [
    {
        "name": "Temple of the Emerald Buddha (วัดพระแก้ว)",
        "province": "Bangkok, Thailand",
        "description": "วัดคู่บ้านคู่เมือง ประดิษฐานพระแก้วมรกต สถาปัตยกรรมงดงามอลังการ",
        "image": "https://images.unsplash.com/photo-1552465011-b4e21bf6e79a?w=500",
        "lat": 13.7515,
        "lng": 100.4927
    },
    {
        "name": "Tokyo Tower (โตเกียวทาวเวอร์)",
        "province": "Tokyo, Japan",
        "description": "หอคอยสัญลักษณ์ของโตเกียว สีแดง-ขาวโดดเด่น ชมวิวเมืองได้แบบ 360 องศา",
        "image": "https://images.unsplash.com/photo-1536098561742-ca998e48cbcc?w=500",
        "lat": 35.6586,
        "lng": 139.7454
    },
    {
        "name": "Eiffel Tower (หอไอเฟล)",
        "province": "Paris, France",
        "description": "สัญลักษณ์ของกรุงปารีส หอคอยเหล็กสูง 330 เมตร วิวเมืองสวยที่สุดตอนพระอาทิตย์ตก",
        "image": "https://images.unsplash.com/photo-1543349689-9a4d426bee8e?w=500",
        "lat": 48.8584,
        "lng": 2.2945
    },
    {
        "name": "Sydney Opera House (โรงอุปรากรซิดนีย์)",
        "province": "Sydney, Australia",
        "description": "อาคารสถาปัตยกรรมรูปเปลือกหอยอันโด่งดัง สัญลักษณ์ของประเทศออสเตรเลีย",
        "image": "https://images.unsplash.com/photo-1524293581917-878a6d017c71?w=500",
        "lat": -33.8568,
        "lng": 151.2153
    },
    {
        "name": "Leaning Tower of Pisa (หอเอนเมืองปิซ่า)",
        "province": "Pisa, Italy",
        "description": "หอระฆังเอียงชื่อดัง เกิดจากฐานรากที่ไม่มั่นคง กลายเป็นแลนด์มาร์กที่มีเอกลักษณ์ที่สุดในโลก",
        "image": "https://images.unsplash.com/photo-1543429257-16d1e5cf2fd7?w=500",
        "lat": 43.7230,
        "lng": 10.3966
    },
    {
        "name": "Big Ben (หอนาฬิกาบิ๊กเบน)",
        "province": "London, United Kingdom",
        "description": "หอนาฬิกาอันเป็นสัญลักษณ์ของกรุงลอนดอน ตั้งอยู่ติดกับอาคารรัฐสภาอังกฤษ",
        "image": "https://images.unsplash.com/photo-1529655683826-aba9b3e77383?w=500",
        "lat": 51.5007,
        "lng": -0.1246
    },
    {
        "name": "Chichen Itza (พีระมิดชิเชนอิตซา)",
        "province": "Yucatan, Mexico",
        "description": "วิหารโบราณของชาวมายา หนึ่งใน 7 สิ่งมหัศจรรย์ของโลกยุคใหม่ สถาปัตยกรรมล้ำค่าทางดาราศาสตร์",
        "image": "https://images.unsplash.com/photo-1518638150340-f706e86654de?w=500",
        "lat": 20.6843,
        "lng": -88.5678
    },
    {
        "name": "Statue of Liberty (เทพีเสรีภาพ)",
        "province": "New York, USA",
        "description": "สัญลักษณ์แห่งอิสรภาพและประชาธิปไตย ตั้งอยู่บนเกาะกลางอ่าวนิวยอร์ก",
        "image": "https://images.unsplash.com/photo-1524492412937-b28074a5d7da?w=500",
        "lat": 40.6892,
        "lng": -74.0445
    },
    {
        "name": "Angkor Wat (นครวัด)",
        "province": "Siem Reap, Cambodia",
        "description": "ปราสาทหินโบราณที่ใหญ่ที่สุดในโลก สถาปัตยกรรมขอมอันวิจิตรงดงาม มรดกโลกของยูเนสโก",
        "image": "https://images.unsplash.com/photo-1600100397608-f440db54366b?w=500",
        "lat": 13.4125,
        "lng": 103.8670
    },
    {
        "name": "Great Pyramid of Giza (พีระมิดกีซา)",
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