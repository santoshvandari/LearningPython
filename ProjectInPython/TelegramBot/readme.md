# Telegram Bot
Install the Following Libarary
```bash

pip install python-telegram-bot
```

### Code
```bash
import telegram

bot = telegram.Bot(token='YOUR_API_KEY')
channel_id = 'YOUR_CHANNEL_ID'

# Send a text message
bot.send_message(chat_id=channel_id, text='Hello, World!')
```