document.getElementById("quizForm").addEventListener("submit", async (event) => {
    event.preventDefault();
    const transcript = document.getElementById("transcript").value.trim();
    const questionsDiv = document.getElementById("questions");

    if (!transcript) {
        questionsDiv.innerHTML = "<p>Please provide a transcript.</p>";
        return;
    }

    questionsDiv.innerHTML = "<p>Generating questions...</p>";

    try {
        const response = await fetch("/generate", {
            method: "POST",
            headers: { "Content-Type": "application/x-www-form-urlencoded" },
            body: `transcript=${encodeURIComponent(transcript)}`,
        });

        const data = await response.json();

        if (data.error) {
            questionsDiv.innerHTML = `<p>Error: ${data.error}</p>`;
        } else if (data.questions && data.questions.length) {
            const questions = data.questions.map((q, i) => `<p><b>Question ${i + 1}:</b> ${q}</p>`).join("");
            questionsDiv.innerHTML = questions;
        } else {
            questionsDiv.innerHTML = "<p>No questions were generated. Please try again.</p>";
        }
    } catch (error) {
        questionsDiv.innerHTML = `<p>Error: ${error.message}</p>`;
    }
});
