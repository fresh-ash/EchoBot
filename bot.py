import config
import telebot
from keyboard import dialog
import logging
import strings


log = telebot.logger
telebot.logger.setLevel(logging.INFO)
bot = telebot.TeleBot(token=config.token)
dialogs = {}

@bot.message_handler(commands=["start"])
def start_work(message):
  chat_id = message.chat.id
  dialogs[str(chat_id)] = dialog.Dialog()
  dialogs.get(str(chat_id)).update_dialog('d0')
  bot.send_message(config.admin_id, strings.new_user_conn + str(chat_id))
  bot.send_photo(chat_id, photo=open('/var/tmp/bot/index.jpeg', 'rb'))
  bot.send_message(chat_id, text="Hello, <b>" + str(message.from_user.first_name) + "</b>!", parse_mode='HTML')
  curr_dialog = dialogs[str(chat_id)]
  bot.send_message(chat_id, curr_dialog.mess, reply_markup=curr_dialog.kb)

@bot.message_handler(commands=["addtobasket"])
def add_to_basket(message):
  chat_id = message.chat.id
  args = message.text
  d = dialogs[str(chat_id)]
  d.add_to_basket(args)

@bot.message_handler(content_types=["text"])
def repeat_every_mess(message):
  chat_id = message.chat.id
  args = message.text
  d = dialogs[str(chat_id)]
  bot.send_message(config.admin_id, message.text)
  if message.text[:12] == "/addtobasket":
    d.add_to_basket(args[12:])
  bot.send_message(chat_id, "Thanks for your message!")

@bot.callback_query_handler(func=lambda call: True)
def get_callback(query):
  bot.answer_callback_query(query.id)
  curr_dialog = dialogs.get(str(query.message.chat.id))
  curr_dialog.update_dialog(str(query.data))
  print(curr_dialog.states)
  print(curr_dialog.basket)
  bot.edit_message_text(text=curr_dialog.mess, chat_id=query.message.chat.id, message_id=query.message.message_id, reply_markup=curr_dialog.kb, parse_mode='HTML')


if __name__ == '__main__':
  bot.polling(none_stop=True)