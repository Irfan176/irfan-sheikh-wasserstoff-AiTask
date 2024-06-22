<?php
/*
Plugin Name: RAG Chatbot 
Description: Integrates RAG-based chatbot with WordPress.
Version: 1.0
Author: Your Name
*/

// Add settings page
function chatbot_settings_page() {
    add_options_page('RAG Chatbot Settings', 'RAG Chatbot', 'manage_options', 'rag-chatbot-settings', 'chatbot_settings_page_content');
}
add_action('admin_menu', 'chatbot_settings_page');

function chatbot_settings_page_content() {
    ?>
    <div class="wrap">
        <h2>RAG Chatbot Settings</h2>
        <form method="post" action="options.php">
            <?php
            settings_fields('rag-chatbot-settings');
            do_settings_sections('rag-chatbot-settings');
            submit_button();
            ?>
        </form>
    </div>
    <?php
}

function chatbot_register_settings() {
    register_setting('rag-chatbot-settings', 'rag_chatbot_api_url');
    add_settings_section('rag-chatbot-main', 'Main Settings', null, 'rag-chatbot-settings');
    add_settings_field('rag_chatbot_api_url', 'API URL', 'chatbot_api_url_callback', 'rag-chatbot-settings', 'rag-chatbot-main');
}
add_action('admin_init', 'chatbot_register_settings');

function chatbot_api_url_callback() {
    $api_url = get_option('rag_chatbot_api_url');
    echo "<input type='text' name='rag_chatbot_api_url' value='$api_url' />";
}

function enqueue_chatbot_assets() {
    wp_enqueue_style('chatbot_style', plugins_url('style.css', __FILE__));
    wp_enqueue_script('chatbot_script', plugins_url('script.js', __FILE__), array('jquery'), null, true);
    
    $api_url = get_option('rag_chatbot_api_url', 'http://localhost:8000');
    wp_localize_script('chatbot_script', 'chatbotApi', array(
        'url' => $api_url
    ));
}
add_action('wp_enqueue_scripts', 'enqueue_chatbot_assets');

function chatbot_widget() {
    echo '<div id="chatbot">
            <div id="chatbot-window"></div>
            <div id="chatbot-loading" style="display:none;">Loading...</div>
            <input id="chatbot-input" type="text" placeholder="Ask me anything..."/>
            <button id="chatbot-send">Send</button>
          </div>';
}
add_action('wp_footer', 'chatbot_widget');
?>