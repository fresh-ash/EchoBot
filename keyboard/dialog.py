from telebot import types
import strings
from emoji import emojize

class Dialog:

  def __init__(self):
    self.states = []
    self.photos = {}
    self.mess = ""
    self.kb = None
    self.basket = []



  def update_dialog(self, call_back_data):

    if call_back_data == 'back':
      self.states.pop()
      self.update_dialog(self.states.pop())
    elif call_back_data == 'home':
      self.restart()
      self.update_dialog('d0')
    else:
      data = strings.dialogs_us.get(call_back_data)
      self.kb = types.InlineKeyboardMarkup()

      for key, val in data.items():
        if (key == 'mess'):
          self.mess = data.get(key)
          if self.basket:
            self.mess += "\n\nYour basket:\n"
            for key in self.basket:
              self.mess += str(strings.goods.get(key)) + "\n"
        else:
          self.kb.add(types.InlineKeyboardButton(data.get(key), callback_data=str(key)))

      if not (self.states == []):
        self.kb.add(types.InlineKeyboardButton(emojize(":rewind:", use_aliases=True) + " Back", callback_data='back'))
        self.kb.add(types.InlineKeyboardButton(emojize(":house_with_garden:", use_aliases=True) + " Home", callback_data='home'))
      self.states.append(call_back_data)


  def add_to_basket(self, arg):
    self.basket.append(arg)


  def restart(self):
    self.states = []






