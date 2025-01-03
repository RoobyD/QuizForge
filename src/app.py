from flask import Flask, render_template, request, jsonify
from transformers import pipeline

app = Flask(__name__)

# Initialize the pipeline with the correct model
question_generator = pipeline("text-generation", model="meta-llama/Llama-3.2-1B")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():
    # Get transcript input from the form
    transcript = request.form.get("transcript", "")
    if not transcript:
        return jsonify({"error": "No transcript provided"}), 400

    try:
        # Generate questions using the Llama model pipeline
        prompt = f"Generate questions based on the following transcript: {transcript}"
        generated_output = question_generator(prompt, num_return_sequences=3, truncation=True, max_new_tokens=50)

        # Extract questions from the output
        questions = [output["generated_text"] for output in generated_output]

        return jsonify({"questions": questions})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)

