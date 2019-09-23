#admin messageges
from emoji import emojize

new_user_conn = "Somebody's knocking! ID:"

goods = {'1': u"Красный маркер", '2': u"Шариковая ручка"}
first_us_mess = "I am your assistant. I can help you create your own bot.\nAre you ready to follow my instructions?"
second_us_mess = "What kind of bot do you need? I offer you next variants!\nBut we can discuss another one... " \
                 "Describe your bot project and send me in text message."
third_us_mess = "I'll try to convince you. Please, read info about my bots!"
seller_info = "You can see some example this kind of bot. Please, click 'Example'!"
chat_mate_info = "About"
spy_info = "About"
assistant_info = "You can see some example this kind of bot. Please, click 'Example'!"
base_seller_mess = "<b>Beauty Studio</b>\n"
it1_mess = "Some"
it2_mess = emojize(":lower_left_crayon:", use_aliases=True) + " - Красный маркер\nPrice: 0.99$\n/addtobasket1\n" \
           + emojize(":lower_left_ballpoint_pen:", use_aliases=True) + " - Шариковая ручка\nPrice: 1.05$\n/addtobasket2\n"
dialogs_us = {'d0': {'y0': "Yes", 'n0': "I'm not sure...", 'mess': first_us_mess},
              'y0': {'seller': "Seller", 'chat_mate': "Chat mate", 'spy': "Spy", 'assistant': "Assistant", 'mess': second_us_mess},
              'n0': {'y0': "About", 'mess': third_us_mess},
              'seller': {'sell_ex': "Example", 'mess': seller_info},
              'sell_ex': {'goods': "Goods", 'services': "Services", 'mess': base_seller_mess},
              'goods': {'it1': emojize(":art:", use_aliases=True) + "Paint", 'it2':  emojize(":lower_left_fountain_pen:", use_aliases=True) + "Pens", 'mess': base_seller_mess + "I can offer you next goods:"},
              'it1': {'mess': it1_mess},
              'it2': {'mess': it2_mess},
              'services': {'s1': "Service1", 's2': "Service2", 'mess': base_seller_mess + "I can offer you next services:"},
              's1': {'mess': "Something"},
              's2': {'mess': "Something"},
              'chat_mate': {'mess': chat_mate_info},
              'spy': {'mess': spy_info},
              'assistant': {'mess': assistant_info}
              }
