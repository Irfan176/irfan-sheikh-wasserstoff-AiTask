document.getElementById('chatbot-send').addEventListener('click', function() {
    const query = document.getElementById('chatbot-input').value;
    const chatbotWindow = document.getElementById('chatbot-window');
    const userMessage = document.createElement('div');
    userMessage.className = 'user-message';
    userMessage.textContent = query;
    chatbotWindow.appendChild(userMessage);

    fetch('http://localhost:8000/query', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ query: query, previous_context: [] })
    })
    .then(response => response.json())
    .then(data => {
        const botMessage = document.createElement('div');
        botMessage.className = 'bot-message';
        botMessage.textContent = data.response;
        chatbotWindow.appendChild(botMessage);
        document.getElementById('chatbot-input').value = '';
    });
});
