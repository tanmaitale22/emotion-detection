# app/web.py
from flask import Flask, request, jsonify, render_template_string
from .nlu_client import WatsonNLUClient
from .emotion import parse_emotion_response, pretty_json

def create_app():
    app = Flask(__name__)
    nlu = WatsonNLUClient()

    @app.route("/")
    def index():
        html = """
        <h1>Emotion Detection (Watson NLU)</h1>
        <form method="post" action="/analyze">
          <textarea name="text" rows="6" cols="60" placeholder="Enter text"></textarea><br/>
          <button type="submit">Analyze</button>
        </form>
        """
        return render_template_string(html)

    @app.route("/analyze", methods=["POST"])
    def analyze():
        text = request.form.get("text") or request.json.get("text")
        if not text or not text.strip():
            return jsonify({"error": "text is required"}), 400
        try:
            resp = nlu.analyze_emotion(text)
            parsed = parse_emotion_response(resp)
            return jsonify({"emotion": parsed})
        except Exception as e:
            # simple error handling — see Task 7
            return jsonify({"error": str(e)}), 500

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, host="0.0.0.0", port=5000)
