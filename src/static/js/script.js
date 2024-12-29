document.getElementById("transcript-form").addEventListener("submit", async (e) => {
    e.preventDefault();

    const form = e.target;
    const formData = new FormData(form);
    const response = await fetch("/generate", {
        method: "POST",
        body: formData,
    });

    const result = await response.json();
    const questionsDiv = document.getElementById("questions");
    questionsDiv.innerHTML = "";

    if (response.ok) {
        result.questions.forEach((question, index) => {
            const p = document.createElement("p");
            p.textContent = `${index + 1}. ${question}`;
            questionsDiv.appendChild(p);
        });
    } else {
        questionsDiv.textContent = result.error || "An error occurred.";
    }
});
