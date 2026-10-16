
from flask import Flask, request, render_template_string

app = Flask(__name__)

PASSWORD = "07122009"

HTML = """
<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Một điều muốn nói 💗</title>

<style>
* {
    box-sizing: border-box;
}

body {
    margin: 0;
    min-height: 100vh;
    display: grid;
    place-items: center;
    padding: 20px;
    overflow-x: hidden;
    font-family: "Segoe UI", sans-serif;
    color: #884c78;
    background: linear-gradient(135deg, #ffdce9, #f0e0ff, #dff4ff);
}

.credit {
    position: fixed;
    top: 10px;
    right: 15px;
    z-index: 10;
    background: white;
    color: #000;
    padding: 8px;
    border-radius: 8px;
    font-size: 13px;
    font-weight: bold;
}

.heart {
    position: fixed;
    bottom: -40px;
    pointer-events: none;
    animation: float 8s linear infinite;
    z-index: 0;
}

.heart:nth-child(1) { left: 8%; }
.heart:nth-child(2) { left: 25%; animation-delay: 2s; }
.heart:nth-child(3) { left: 75%; animation-delay: 1s; }
.heart:nth-child(4) { left: 90%; animation-delay: 3s; }

@keyframes float {
    0% {
        transform: translateY(0);
        opacity: 0;
    }
    15% { opacity: 1; }
    100% {
        transform: translateY(-115vh) rotate(35deg);
        opacity: 0;
    }
}

.card {
    position: relative;
    z-index: 1;
    width: min(100%, 430px);
    padding: 35px 28px;
    text-align: center;
    background: rgba(255, 255, 255, .82);
    border: 2px solid white;
    border-radius: 30px;
    box-shadow: 0 20px 60px #c17eae40;
    backdrop-filter: blur(12px);
    animation: appear .6s ease;
}

@keyframes appear {
    from {
        opacity: 0;
        transform: translateY(20px) scale(.96);
    }
    to {
        opacity: 1;
        transform: translateY(0) scale(1);
    }
}

.bunny {
    font-size: 65px;
    margin-bottom: 12px;
    animation: bounce 2s infinite ease-in-out;
}

@keyframes bounce {
    0%, 100% { transform: translateY(0) rotate(-4deg); }
    50% { transform: translateY(-10px) rotate(4deg); }
}

h1 {
    color: #d65b9a;
    font-size: 27px;
    margin: 0 0 12px;
}

.subtitle {
    color: #a17d9c;
    line-height: 1.7;
    font-size: 14px;
    margin-bottom: 24px;
}

input {
    width: 100%;
    padding: 15px;
    border: 2px solid #f5d5e8;
    border-radius: 15px;
    background: #fffafd;
    font-size: 15px;
    outline: none;
}

input:focus {
    border-color: #ee8cbd;
}

button {
    border: none;
    border-radius: 15px;
    padding: 14px 18px;
    background: linear-gradient(100deg, #ff85b5, #b59aff);
    color: white;
    font-size: 15px;
    font-weight: bold;
    cursor: pointer;
    box-shadow: 0 7px 18px #e78dbd50;
    transition: .25s;
}

button:hover {
    transform: translateY(-3px) scale(1.02);
}

.full-button {
    width: 100%;
    margin-top: 14px;
}

.choices {
    display: flex;
    gap: 10px;
    margin-top: 20px;
}

.choices button {
    flex: 1;
}

.no-button {
    background: linear-gradient(100deg, #a6a6b8, #818ba8);
}

.question-box, .love-note, .sad-note {
    padding: 22px 16px;
    border: 2px dashed #efa5ca;
    border-radius: 22px;
    background: linear-gradient(135deg, #fff4fa, #f5efff);
}

.question {
    font-size: 25px;
    font-weight: bold;
    color: #cc5797;
    margin: 12px 0;
}

.big-heart {
    font-size: 55px;
    animation: beat 1.2s infinite;
}

@keyframes beat {
    0%, 100% { transform: scale(1); }
    50% { transform: scale(1.2); }
}

.love-text {
    font-size: 23px;
    font-weight: bold;
    line-height: 1.7;
    color: #d44f97;
}

.sad-emoji {
    font-size: 65px;
    animation: sad 2s infinite ease-in-out;
}

@keyframes sad {
    0%, 100% { transform: translateY(0); }
    50% { transform: translateY(6px); }
}

.sad-text {
    color: #85839a;
    font-size: 22px;
    line-height: 1.7;
    font-weight: bold;
}

.footer {
    color: #b18eac;
    font-size: 12px;
    margin-top: 22px;
}

.music-button {
    position: fixed;
    bottom: 15px;
    right: 15px;
    z-index: 100;
    border-radius: 20px;
}

@media (max-width: 420px) {
    .card { padding: 28px 20px; }
    .choices { flex-direction: column; }
}
</style>
</head>

<body>

<div class="credit">cre: QxrexMC</div>

<span class="heart">💗</span>
<span class="heart">💕</span>
<span class="heart">✨</span>
<span class="heart">💖</span>

<main class="card">

{% if page == "love" %}

    <div class="bunny">💌</div>
    <h1>Tui có điều muốn nói...</h1>
    <p class="subtitle">Tui đã lấy hết can đảm rồi đó 🥺</p>

    <section class="love-note">
        <div class="big-heart">💖</div>
        <p class="love-text">
            Tui thích bạn,<br>
            bạn làm người yêu tui nha!
        </p>
        <p>Hy vọng chúng ta có thật nhiều kỷ niệm đẹp ♡</p>
    </section>

    <p class="footer">Một chiếc thư tình dành riêng cho bạn 🎀</p>

{% elif page == "sad" %}

    <div class="sad-emoji">🥺</div>
    <h1>À... tui hiểu rồi</h1>

    <section class="sad-note">
        <p class="sad-text">Xin lỗi vì đã làm phiền :(</p>
        <p style="color:#a5a1b5">Chúc bạn luôn vui vẻ nhé...</p>
        <div style="font-size:35px">🥀💧</div>
    </section>

    <p class="footer">Mong mọi điều tốt đẹp sẽ đến với bạn.</p>

{% elif page == "question" %}

    <div class="bunny">🐰</div>
    <h1>Tui hỏi cái này nha...</h1>
    <p class="subtitle">Bạn trả lời thật lòng cho tui biết với 🥺</p>

    <section class="question-box">
        <div class="question">Bạn có thích tui hong? 💗</div>
        <div style="font-size:42px">૮ ˶ᵔ ᵕ ᵔ˶ ა</div>

        <form method="POST" class="choices">
            <button name="answer" value="yes" type="submit">
                Có chứ 💖
            </button>

            <button name="answer" value="no" type="submit"
                    class="no-button">
                Không nhé 😢
            </button>
        </form>
    </section>

{% else %}

    <div class="bunny">🐰</div>
    <h1>Chào bạn đáng yêu! 💗</h1>

    <p class="subtitle">
        Tui có một món quà bí mật dành cho bạn.
        Nhập mật khẩu để mở nha! ✨
    </p>

    <form method="POST">
        <input type="password" name="password"
               placeholder="🔒 Nhập mật khẩu..." required>
        <button class="full-button" type="submit">Mở bí mật ♡</button>
    </form>

    {% if error %}
        <p style="color:#d84e79">{{ error }}</p>
    {% endif %}

    <p class="footer">Được gói ghém bằng một chút dễ thương 🎀</p>

{% endif %}

</main>

<audio id="backgroundMusic" loop preload="auto">
    <source src="{{ url_for('static', filename='music.mp3') }}"
            type="audio/mpeg">
</audio>

<button id="musicButton" class="music-button" type="button" hidden>
    🎵 Bật nhạc nền
</button>

<script>
const music = document.getElementById("backgroundMusic");
const musicButton = document.getElementById("musicButton");

async function playMusic() {
    try {
        await music.play();
        musicButton.hidden = true;
    } catch (error) {
        musicButton.hidden = false;
        musicButton.textContent = "🎵 Bấm để bật nhạc";
        console.log("Trình duyệt chưa cho phép tự phát nhạc.");
    }
}

window.addEventListener("load", playMusic);

musicButton.addEventListener("click", playMusic);
</script>

</body>
</html>
"""


@app.route("/", methods=["GET", "POST"])
def home():
    page = "password"
    error = None

    if request.method == "POST":
        if "password" in request.form:
            if request.form.get("password") == PASSWORD:
                page = "question"
            else:
                error = "Mật khẩu chưa đúng rồi, thử lại nha!"

        elif request.form.get("answer") == "yes":
            page = "love"

        elif request.form.get("answer") == "no":
            page = "sad"

    return render_template_string(
        HTML,
        page=page,
        error=error
    )


if __name__ == "__main__":
    import os

    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 2009)),
        debug=False
    )
