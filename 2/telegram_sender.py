import sys
import os
import asyncio                  
from dotenv import load_dotenv
from telegram import Bot
from telegram.error import TelegramError

load_dotenv()

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

if not TOKEN or not CHAT_ID:
    print("Ошибка: не найдены TELEGRAM_BOT_TOKEN или TELEGRAM_CHAT_ID в файле .env")
    sys.exit(1)

async def send_text_from_file(file_path):          
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            text = f.read().strip()
        
        if not text:
            print("Файл пустой, ничего не отправляем.")
            return

        bot = Bot(token=TOKEN)
        await bot.send_message(                        
            chat_id=CHAT_ID,
            text=text,
            parse_mode='HTML'                          
        )
        print("Сообщение успешно отправлено!")
    
    except FileNotFoundError:
        print(f"Файл не найден: {file_path}")
    except TelegramError as e:
        print(f"Ошибка Telegram API: {e}")
    except Exception as e:
        print(f"Неизвестная ошибка: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Использование: python telegram_sender.py путь/к/файлу.txt")
        sys.exit(1)
    
    file_path = sys.argv[1]
    asyncio.run(send_text_from_file(file_path))        