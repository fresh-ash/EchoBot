import config
import telebot
from keyboard import dialog
import logging
import strings


log = telebot.logger
telebot.logger.setLevel(logging.INFO)
bot = telebot.TeleBot(token=config.token)
d = dialog.Dialog()


@bot.message_handler(commands=["start"])
def start_work(message):
  chat_id = message.chat.id
  d.restart()
  d.update_dialog('d0')
  bot.send_message(config.admin_id, strings.new_user_conn + str(chat_id))
  bot.send_photo(chat_id, photo=open('/tmp/img1.png', 'rb'))
  bot.send_message(chat_id, text="Hello, <b>" + str(message.from_user.first_name) + "</b>!", parse_mode='HTML')
  bot.send_message(chat_id, d.mess, reply_markup=d.kb)

@bot.message_handler(content_types=["text"])
def repeat_every_mess(message):
  bot.send_message(config.admin_id, message.text)
  bot.send_message(message.chat.id, "Thanks for your message!")

@bot.callback_query_handler(func=lambda call: True)
def get_callback(query):
  bot.answer_callback_query(query.id)
  d.update_dialog(str(query.data))
  print(d.states)
  bot.edit_message_text(text=d.mess, chat_id=query.message.chat.id, message_id=query.message.message_id, reply_markup=d.kb, parse_mode='HTML')
  #bot.send_message(query.message.chat.id, d.mess, reply_markup=d.kb, parse_mode='HTML')

if __name__ == '__main__':
  bot.polling(none_stop=True)