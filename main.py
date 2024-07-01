import telebot
import database
TOKEN = ''
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['add'])
def upload(message):
    bot.send_message(message.chat.id, '😊 Отправьте файл, для сохранения в базу данных!')
    bot.register_next_step_handler(message, addData)

def addData(message):
    database.addFile(message.from_user.id, message.message_id, message.caption)
    bot.send_message(message.chat.id, '✅ Файл добавлен в систему!')

@bot.message_handler(commands=['get'])
def download(message):
    bot.send_message(message.chat.id, '😊 Отправьте ключ, по которому вы сохраняли файл!')
    bot.register_next_step_handler(message, getData)

def getData(message):
        id = database.getFile(message.from_user.id, message.text)
        if (id != []):
            bot.send_message(message.chat.id, '👆 Нажмите на прикрепленное сообщение, чтобы перейти к файлу', reply_to_message_id=id)
        else:
            bot.send_message(message.chat.id, '❌ Файл не найден, попробуйте заново!', reply_to_message_id=id)

@bot.message_handler(commands=['remove'])
def remove(message):
    bot.send_message(message.chat.id, '😊 Отправьте ключ, который надо удалить!')
    bot.register_next_step_handler(message, removeData)

def removeData(message):
    database.removeFile(message.from_user.id, message.text)
    bot.send_message(message.chat.id, '✅ Файл удален из системы!')


@bot.message_handler(commands=['list'])
def listOfFiles(message):
    fileString = database.getListOfFiles(message.from_user.id)
    bot.send_message(message.chat.id, f"""
📑 Список ваших файлов:
<pre><code>{fileString}</code></pre>             
""", parse_mode='HTML')


database.open_connection()
bot.polling()
