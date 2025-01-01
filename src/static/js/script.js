document.getElementById("transcript-form").addEventListener("submit", async function (e) {
    e.preventDefault();

    const transcript = document.getElementById("transcript").value;

    if (!transcript) {
        alert("Please enter a transcript.");
        return;
    }

    try {
        const response = await fetch("/generate", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({ transcript }),
        });

        const data = await response.json();

        if (data.error) {
            alert("Error: " + data.error);
            return;
        }

        const questionsList = document.getElementById("questions-list");
        questionsList.innerHTML = ""; // Clear previous questions

        data.questions.forEach((question) => {
            const li = document.createElement("li");
            li.textContent = question;
            questionsList.appendChild(li);
        });
    } catch (err) {
        alert("An error occurred: " + err.message);
    }
});
