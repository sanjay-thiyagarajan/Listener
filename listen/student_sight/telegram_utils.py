import requests


class sight_bot():
    def __init__(self):
        self.token = '1642684715:AAGJnYmaq9KZGbE8xqBkit88ikW2wE4ooVY'  ## bot token 
        self.chatID = '1013796379'  ## https://medium.com/@ManHay_Hong/how-to-create-a-telegram-bot-and-send-messages-with-python-4cf314d9fa3e

    def send_message(self, message):
        send_text = 'https://api.telegram.org/bot' + self.token + '/sendMessage?chat_id=' + self.chatID + '&parse_mode=Markdown&text=' + message

        response = requests.get(send_text)

        return response.json()
