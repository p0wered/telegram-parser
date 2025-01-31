from telethon import TelegramClient, events

# параметры
api_id = 'your_app_id'
api_hash = 'your_app_hash'
phone_number = 'your_phone_number'
chat_name_or_id = 'your_chat_name_or_id'
client = TelegramClient('session_name', api_id, api_hash)

# получение старых сообщений
async def print_old_messages(chat):
    async for message in client.iter_messages(chat):
        print(f"Пользователь: {message.sender_id}, Сообщение: {message.text}")

# получение новых сообщений
@client.on(events.NewMessage(chats=chat_name_or_id))
async def handler(event):
    print(f"Новое сообщение. Пользователь: {event.sender_id}, Сообщение: {event.text}")

async def main():
    await client.start(phone_number)
    print("Парсер запущен.")

    try:
        chat = await client.get_entity(chat_name_or_id)
        print(f"Успешно подключено к чату: {chat.title if hasattr(chat, 'title') else chat.username}")
    except Exception as e:
        print(f"Ошибка подключения к чату: {e}")
        return

    await print_old_messages(chat)
    print("Ожидание новых сообщений...")
    await client.run_until_disconnected()

# запуск асинхронного цикла
if __name__ == '__main__':
    import asyncio
    asyncio.run(main())