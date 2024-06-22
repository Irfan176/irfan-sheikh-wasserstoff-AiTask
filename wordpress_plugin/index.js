jQuery(document).ready(function($) {
    var chatWindow = $('#chatbot-window');
    var chatInput = $('#chatbot-input');
    var chatSend = $('#chatbot-send');
    var chatLoading = $('#chatbot-loading');
    var previousContext = [];

    function addMessage(message, isUser) {
        chatWindow.append('<div class="' + (isUser ? 'user-message' : 'bot-message') + '">' + message + '</div>');
        chatWindow.scrollTop(chatWindow[0].scrollHeight);
    }

    function sendMessage() {
        var message = chatInput.val().trim();
        if (message) {
            addMessage(message, true);
            chatInput.val('');
            chatLoading.show();

            $.ajax({
                url: chatbotApi.url + '/query',
                method: 'POST',
                contentType: 'application/json',
                data: JSON.stringify({
                    query: message,
                    previous_context: previousContext
                }),
                success: function(response) {
                    chatLoading.hide();
                    addMessage(response.response, false);
                    previousContext.push(message);
                    previousContext.push(response.response);
                    if (previousContext.length > 4) {
                        previousContext = previousContext.slice(-4);
                    }
                },
                error: function(jqXHR, textStatus, errorThrown) {
                    chatLoading.hide();
                    console.error("API error:", textStatus, errorThrown);
                    addMessage("Sorry, there was an error processing your request. Please try again later.", false);
                }
            });
        }
    }

    chatSend.click(sendMessage);
    chatInput.keypress(function(e) {
        if (e.which == 13) {  // Enter key
            sendMessage();
        }
    });
});