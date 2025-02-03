import json
from telethon import TelegramClient


api_id = 'your_id'
api_hash = 'your_hash'
phone_number = 'your_phone_number'
chat_name_or_id = 'your_chat_name_or_id'
client = TelegramClient('session_name', api_id, api_hash)


# сохранение в json
def save_to_json(data, filename='messages.json'):
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
    except Exception as e:
        print(f"Ошибка при записи в файл {filename}: {e}")


# формат сообщения
def save_message_info(message):
    return {
        "Отправитель ID": message.sender_id,
        "Отправитель": message.sender.username if message.sender else None,
        "Сообщение": message.text,
        "Дата": message.date.strftime('%Y-%m-%d %H:%M:%S'),
    }


# получение сообщений
async def save_old_messages(chat):
    all_messages = []
    async for message in client.iter_messages(chat, reverse=True):
        all_messages.append(save_message_info(message))
    save_to_json(all_messages)


async def main():
    await client.start(phone_number)
    print("Парсер запущен")

    try:
        chat = await client.get_entity(chat_name_or_id)
        print(f"Успешно подключено к чату: {chat.title if hasattr(chat, 'title') else chat.username}")
    except Exception as e:
        print(f"Ошибка подключения к чату: {e}")
        return

    await save_old_messages(chat)
    print("Загрузка сообщений завершена. Данные сохранены в messages.json")


# асинхронный цикл
if __name__ == '__main__':
    import asyncio
    asyncio.run(main())