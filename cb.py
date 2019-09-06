

def dialog_cb(query, bot, func):
  bot.answer_callback_query(query.id)
  func(query, bot)