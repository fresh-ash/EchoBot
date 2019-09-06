from telebot import types



class CustomKeyBoard(types.InlineKeyboardMarkup):

  def __init__(self, state, mess):
    self.mess = mess
    self.state = state
    super().__init__()

  def change_state(self, state):
    self.state = state


def custom_inline_keyboard(template, **kwargs):
  keyboard = CustomKeyBoard(state=None, mess=None, **kwargs)
  keyboard.mess = template.get("mess")
  for i in template.get("answ"):
      keyboard.add(types.InlineKeyboardButton(i, callback_data=i.lower()))
  return keyboard


# Keyboard Y/N

