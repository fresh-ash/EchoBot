from telebot import types
import strings

class Dialog:

  states = []
  mess = ""
  kb = None

  def update_dialog(self, call_back_data):

    if call_back_data == 'back':
      self.states.pop()
      self.update_dialog(self.states.pop())
    else:
      data = strings.dialogs_us.get(call_back_data)
      self.kb = types.InlineKeyboardMarkup()
      for key, val in data.items():
        if (key == 'mess'):
          self.mess = data.get(key)
        else:
          self.kb.add(types.InlineKeyboardButton(data.get(key), callback_data=str(key)))

      if not (self.states == []):
        self.kb.add(types.InlineKeyboardButton("<< Back", callback_data='back'))
      self.states.append(call_back_data)

  def restart(self):
    self.states = []
    

