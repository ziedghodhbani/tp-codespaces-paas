import os
from flask import Flask, jsonify
app = Flask(__name__)
MESSAGE = os.environ.get(
 "MESSAGE",
 "Bienvenue sur mon application Cloud !"
)
# Image publique hébergée sur Wikimedia Commons.
IMAGE_URL = (
 "https://commons.wikimedia.org/wiki/Special:FilePath/Datacenter.jpg"
)
@app.route("/")
def home():
 return f"""
 <!DOCTYPE html>
 <html lang="fr">
 <head>
 <meta charset="UTF-8">
 <meta name="viewport" content="width=device-width, initial-scale=1">
 <title>Mon application Cloud</title>
 <style>
 body {{
 font-family: Arial, sans-serif;
 max-width: 850px;
 margin: 40px auto;
 padding: 0 18px;
 color: #243447;
 line-height: 1.6;
 }}
 h1 {{ color: #174a7e; }}
 img {{
 width: 100%;
 max-width: 760px;
 height: auto;
 border-radius: 8px;
 }}
 .caption {{ font-size: 0.9em; color: #555; }}
 </style>
 </head>
 <body>
 <h1>{MESSAGE}</h1>
 <p>Cette application Flask est développée avec GitHub Codespaces
 et déployée sur Render.</p>
 <img src="{IMAGE_URL}"
 alt="Baies de serveurs dans un centre de données">
 <p class="caption">
 Image : Datacenter.jpg – Wikimedia Commons
 (<a href="https://commons.wikimedia.org/wiki/File:Datacenter.jpg"
 target="_blank" rel="noopener">source de l’image</a>).
 </p>
 <p><strong>Version 2</strong></p>
 </body>
 </html>
 """
@app.route("/api/health")
def health():
 return jsonify(status="ok")
if __name__ == "__main__":
 port = int(os.environ.get("PORT", 5000))
 app.run(host="0.0.0.0", port=port)