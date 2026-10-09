
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Ayesha's Website</title>
        <meta name="viewport" content="width=device-width, initial-scale=1">

        <style>
            body {
                font-family: Arial, sans-serif;
                background: linear-gradient(135deg, #fbc2eb, #a6c1ee);
                text-align: center;
                padding: 50px 15px;
                color: #713b8f;
            }

            .card {
                background: white;
                max-width: 500px;
                margin: auto;
                padding: 35px 25px;
                border-radius: 25px;
                box-shadow: 0 10px 30px #0002;
            }

            h1 {
                font-size: 45px;
                color: #c044a0;
            }

            p {
                color: #555;
                line-height: 1.8;
            }

            .tag {
                background: #f8e8ff;
                padding: 12px;
                border-radius: 12px;
                margin: 10px 0;
            }
        </style>
    </head>

    <body>
        <div class="card">
            <h1>🌸 Ayesha 🌸</h1>
            <h3>Welcome to My Little World</h3>

            <div class="tag">🎓 KIPS College</div>
            <div class="tag">✨ 17 Years Old</div>

            <h2>About Me 💜</h2>

            <p>
                Hello! My name is Ayesha, and I am a student
                at KIPS College. I believe in learning new
                things, being kind, and working towards my
                dreams. Every day is a new opportunity to
                grow, improve, and build a bright future.
            </p>

            <h3>Dream Big & Shine Bright ✨</h3>
        </div>
    </body>
    </html>
    """


if __name__ == "__main__":
    app.run(debug=True)