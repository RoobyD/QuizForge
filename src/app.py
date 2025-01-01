from flask import Flask, render_template, request, jsonify
from transformers import pipeline

# Initialize Flask app
app = Flask(__name__)

# Load the pipeline with the 7B model
model_name = "meta-llama/Llama-3.3-7B-Instruct"
question_generator = pipeline("text-generation", model=model_name, device_map="auto")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():
    # Get transcript input from the form
    transcript = request.form.get("transcript", "")
    if not transcript:
        return jsonify({"error": "No transcript provided"}), 400

    # Generate questions from the transcript
    try:
        # Use the pipeline to generate questions
        messages = [{"role": "user", "content": transcript}]
        generated_texts = question_generator(messages, max_length=150, num_return_sequences=5)
        
        questions = [f"Question {i+1}: {result['generated_text']}" for i, result in enumerate(generated_texts)]
        return jsonify({"questions": questions})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
