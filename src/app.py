from transformers import pipeline
from flask import Flask, render_template, request, jsonify


app = Flask(__name__)



messages = [
    {"role": "user", "content": "Who are you?"},
]
question_generator = pipeline("text-generation", model="meta-llama/Llama-3.3-70B-Instruct")
question_generator(messages)


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():
    # Get transcript input from the form
    transcript = request.form.get("transcript", "")
    if not transcript:
        return jsonify({"error": "No transcript provided"}), 400

    # Generate questions using the Hugging Face model
    try:
        questions = question_generator(transcript, max_length=64, num_return_sequences=5)
        question_texts = [q['generated_text'] for q in questions]
    except Exception as e:
        return jsonify({"error": f"Error generating questions: {str(e)}"}), 500

    return jsonify({"questions": question_texts})

if __name__ == "__main__":
    app.run(debug=True)
