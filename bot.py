import config
import telebot
from keyboard import keyboard, states
import logging
import strings

log = telebot.logger
telebot.logger.setLevel(logging.INFO)
bot = telebot.TeleBot(token=config.token)

kb = states.FirstKeyBoardState(keyboard.custom_inline_keyboard(strings.dialogs.get('first_dialog')))
kb.update_keyboard()
@bot.message_handler(commands=["start"])
def start_work(message):
  chat_id = message.chat.id
  bot.send_message(config.admin_id, strings.new_user_conn + str(chat_id))
  bot.send_message(chat_id, "Hello, " + str(message.from_user.first_name) + "!")
  bot.send_message(chat_id, kb.arg.mess, reply_markup=kb.arg)


@bot.callback_query_handler(func=lambda call: True)
def go_callback(query):
  cb.y_n_dialog_cb(query, bot)


if __name__ == '__main__':
  bot.polling(none_stop=True)