const chatBox = document.getElementById("chat-box");
const sendBtn = document.getElementById("send-btn");
const userInput = document.getElementById("user-input");
const modeSelect = document.getElementById("mode-select");

function appendMessage(sender, message) {
    const msgDiv = document.createElement("div");
    msgDiv.innerHTML = `<strong>${sender}:</strong> ${message}`;
    msgDiv.classList.add("message");
    chatBox.appendChild(msgDiv);
    chatBox.scrollTop = chatBox.scrollHeight;
}

function speakMessage(message) {
    const utterance = new SpeechSynthesisUtterance(message);
    speechSynthesis.speak(utterance);
}

sendBtn.onclick = async () => {
    const message = userInput.value.trim();
    const mode = modeSelect.value;

    if (!message) return;

    appendMessage("You", message);
    userInput.value = "";

    try {
        const res = await fetch("/chat", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ message, mode })
        });

        if (!res.ok) throw new Error("Failed to get response from server");

        const data = await res.json();
        appendMessage("Gemini", data.reply);
        speakMessage(data.reply);

    } catch (err) {
        console.error("❌ Error:", err);
        appendMessage("Error", "Failed to connect to the chatbot.");
    }
};
