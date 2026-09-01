from flask import Flask, render_template, request, jsonify
import urllib.parse

app = Flask(__name__)

# =========================
# HOME PAGE
# =========================
@app.route("/")
def home():
    return render_template("index.html")


# =========================
# IMAGE GENERATION (FREE)
# =========================
@app.route("/generate", methods=["POST"])
def generate():

    data = request.get_json()

    if not data:
        return jsonify({"error": "No data received"}), 400

    prompt = data.get("prompt", "").strip()

    if not prompt:
        return jsonify({"error": "Please enter a prompt"}), 400

    try:
        # Encode prompt safely for URL
        encoded_prompt = urllib.parse.quote(prompt)

        # FREE image generation (no API key)
        image_url = f"https://image.pollinations.ai/prompt/{encoded_prompt}"

        return jsonify({
            "image": image_url
        })

    except Exception as e:
        print("Error:", e)
        return jsonify({
            "error": "Something went wrong"
        }), 500


# =========================
# RUN SERVER
# =========================
if __name__ == "__main__":
    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True
    )