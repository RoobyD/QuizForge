from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():
    # Get transcript input from the form
    transcript = request.form.get("transcript", "")
    if not transcript:
        return jsonify({"error": "No transcript provided"}), 400

    # Placeholder: Process transcript and generate questions
    questions = [f"Question {i+1}: {line}" for i, line in enumerate(transcript.split('.')) if line.strip()]
    
    return jsonify({"questions": questions})

if __name__ == "__main__":
    app.run(debug=True)
