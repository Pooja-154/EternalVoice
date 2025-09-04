<script>
  document.getElementById('sendBtn').onclick = async function () {
    const input = document.getElementById('userInput');
    const mode = document.getElementById('mode').value;
    const message = input.value;

    if (!message) return;

    const response = await fetch('/chat', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ message, mode })
    });

    const data = await response.json();
    const chatDiv = document.getElementById('chatBox');

    chatDiv.innerHTML += `<div><strong>You:</strong> ${message}</div>`;
    chatDiv.innerHTML += `<div><strong>Gemini (${mode}):</strong> ${data.reply}</div>`;
    input.value = '';
  };
</script>
