from flask import Flask, render_template

app = Flask(__name__)

places = [
    {
        "name": "วัดพระแก้ว",
        "province": "กรุงเทพฯ",
        "description": "วัดคู่บ้านคู่เมือง ประดิษฐานพระแก้วมรกต สถาปัตยกรรมงดงามอลังการ",
        "image": "https://images.unsplash.com/photo-1552465011-b4e21bf6e79a?w=500"
    },
    {
        "name": "ดอยอินทนนท์",
        "province": "เชียงใหม่",
        "description": "ยอดเขาที่สูงที่สุดในประเทศไทย อากาศเย็นสบายตลอดปี วิวทะเลหมอกสวยงาม",
        "image": "https://images.unsplash.com/photo-1528181304800-259b08848526?w=500"
    },
    {
        "name": "เกาะพีพี",
        "province": "กระบี่",
        "description": "เกาะที่มีน้ำทะเลใสสีเทอร์คอยส์ หาดทรายขาวละเอียด เหมาะกับดำน้ำดูปะการัง",
        "image": "https://images.unsplash.com/photo-1552733407-5d5c46c3bb3b?w=500"
    },
]

@app.route("/")
def home():
    return render_template("index.html", places=places)

if __name__ == "__main__":
    app.run(debug=True)