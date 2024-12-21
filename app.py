from flask import *
import os

app = Flask(
    __name__,
    static_folder="public",
    static_url_path="/"
)


@app.route("/")
def index():
    return render_template ("index.html")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Render 提供的 PORT 環境變數
    app.run(host="0.0.0.0", port=port)
