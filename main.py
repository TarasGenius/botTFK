import telebot
import time
from telebot import types
from Handler import AnswersHandler, HandlerForConfig


info_answers = AnswersHandler()   # Об'єкт класу з відповідями на всі питання
info_config = HandlerForConfig()  # Об'єкт класу з токеном

bot = telebot.TeleBot(token=info_config.get_token())

ANSWER = ("Оберіть ⌨ цікаву вам вкладку в меню або зв`яжіться з відповідальним секретарем приймальної комісії ТФК ЛНТУ 👨‍🏫 - (091) 956-61-44 ☎️",)
BACK_ANSWER = ('Що вас цікавить? 😉',)


# Універсальна функція надсилання повідомлень
def bot_answer(message, answers, keyboard, next_options):
        user = bot.send_message(message.chat.id,
                                text='\n\n'.join(answers),
                                reply_markup=keyboard())
        bot.register_next_step_handler(user, next_options)


@bot.message_handler(commands=['start'])
def message_start(message):
    print(message)
    name = message.from_user.__dict__['first_name']
    user = bot.send_message(message.chat.id,
                            text=f'Привіт 💙, {name}, мене звуть Гід-бот 🤖, я буду твоїм персональним помічником 🕵‍♂ з питань вступу в коледж 👨‍🎓 ',
                            reply_markup=keyboard_main())
    bot.register_next_step_handler(user,
                                   options_main)


# Перше меню вибору
def options_main(message):
    match message.text:
        case 'Загальноосвітній процес':
            answer = ('Цей розділ перебуває на стадії розробки ⏳',)
            bot_answer(message=message, answers=answer, keyboard=keyboard_main, next_options=options_main)
        case 'Вступ ТФК':
            answer = ('Виберіть 🧐 рівень освіти 🎓, на який плануєте вступ 🏢',)
            bot_answer(message=message, answers=answer, keyboard=keyboard_for_admission,
                       next_options=options_admission)
        case _:
            bot_answer(message=message, answers=ANSWER, keyboard=keyboard_main,
                       next_options=options_main)


# Меню вибору між кваліфікованим робітником і бакалавром
def options_admission(message):
    match message.text:
        case 'Фаховий молодший бакалавр':
            answer = ('Що вас цікавить? 😉',)
            bot_answer(message=message, answers=answer,
                       keyboard=keyboard_for_associate_bachelor, next_options=options_associate_bachelor)
        case 'Кваліфікований робітник':
            answer = ('Що вас цікавить? 😉',)
            bot_answer(message=message, answers=answer,
                       keyboard=keyboard_for_qualified_worker, next_options=options_qualified_worker)
        case 'Повернутись назад':
            bot_answer(message=message, answers=BACK_ANSWER,
                       keyboard=keyboard_main, next_options=options_main)
        case _:
            bot_answer(message=message, answers=ANSWER, keyboard=keyboard_for_admission,
                       next_options=options_admission)


# Менюв ибору для кваліфікованого робітника
def options_qualified_worker(message):
    keyboard = keyboard_for_qualified_worker
    next_options = options_qualified_worker
    match message.text:
        case 'Професії':
            bot_answer(message=message, answers=info_answers.column_value['professions'],
                       keyboard=keyboard, next_options=next_options)
        case 'Документи':
            bot_answer(message=message, answers=info_answers.column_value['documents_worker'],
                       keyboard=keyboard, next_options=next_options)
        case 'Набір. Регіональне замовлення':
            bot_answer(message=message, answers=info_answers.column_value['enrollment_worker'],
                       keyboard=keyboard, next_options=next_options)
        case 'Вступні випробування':
            bot_answer(message=message, answers=info_answers.column_value['entrance_examinations_worker'],
                       keyboard=keyboard, next_options=next_options)
        case 'Етапи вступу':
            bot_answer(message=message, answers=info_answers.column_value['stages_of_admission_worker'],
                       keyboard=keyboard, next_options=next_options)
        case 'Вартість навчання':
            bot_answer(message=message, answers=info_answers.column_value['price_worker'],
                       keyboard=keyboard, next_options=next_options)
        case 'Гуртожиток':
            bot_answer(message=message, answers=info_answers.column_value['dormitory_worker'],
                       keyboard=keyboard, next_options=next_options)
        case 'Пільги на вступ':
            bot_answer(message=message, answers=info_answers.column_value['admission_privilege_worker'],
                       keyboard=keyboard, next_options=next_options)
        case 'Вступ на контракт':
            bot_answer(message=message, answers=info_answers.column_value['contract-based_admission_worker'],
                       keyboard=keyboard, next_options=next_options)
        case 'Контакти':
            bot_answer(message=message, answers=info_answers.column_value['contacts_worker'],
                       keyboard=keyboard, next_options=next_options)
        case 'Повернутись назад':
            bot_answer(message=message, answers=BACK_ANSWER,
                       keyboard=keyboard_for_admission, next_options=options_admission)
        case _:
            bot_answer(message=message, answers=ANSWER, keyboard=keyboard,
                       next_options=next_options)


# Меню вибору для бакалавра
def options_associate_bachelor(message):
    keyboard = keyboard_for_associate_bachelor
    next_options = options_associate_bachelor
    match message.text:
        case 'Перелік спеціальностей':
            bot_answer(message=message, answers=info_answers.column_value['list_of_specialties'],
                       keyboard=keyboard, next_options=next_options)
        case 'Документи та електронний кабінет вступника':
            bot_answer(message=message, answers=info_answers.column_value['documents'],
                       keyboard=keyboard, next_options=next_options)
        case 'Набір. Державне замовлення':
            bot_answer(message=message, answers=info_answers.column_value['state_order'],
                       keyboard=keyboard, next_options=next_options)
        case 'Вступні випробування':
            bot_answer(message=message, answers=info_answers.column_value['entrance_tests'],
                       keyboard=keyboard, next_options=next_options)
        case 'Етапи вступу':
            bot_answer(message=message, answers=info_answers.column_value['stages_of_admission'],
                       keyboard=keyboard, next_options=next_options)
        case 'Вартість навчання':
            bot_answer(message=message, answers=info_answers.column_value['price'],
                       keyboard=keyboard, next_options=next_options)
        case 'Гуртожиток':
            bot_answer(message=message, answers=info_answers.column_value['dormitory'],
                       keyboard=keyboard, next_options=next_options)
        case 'Пільги на вступ':
            bot_answer(message=message, answers=info_answers.column_value['admission_privilege'],
                       keyboard=keyboard, next_options=next_options)
        case 'Вступ на контракт':
            bot_answer(message=message, answers=info_answers.column_value['contract-based_admission'],
                       keyboard=keyboard, next_options=next_options)
        case 'Контакти':
            bot_answer(message=message, answers=info_answers.column_value['contacts'],
                       keyboard=keyboard, next_options=next_options)
        case 'Повернутись назад':
            bot_answer(message=message, answers=BACK_ANSWER,
                       keyboard=keyboard_for_admission, next_options=options_admission)
        case _:
            bot_answer(message=message, answers=ANSWER, keyboard=keyboard,
                       next_options=next_options)


def keyboard_for_associate_bachelor():
    buttons = types.ReplyKeyboardMarkup(resize_keyboard=True)

    button1 = types.KeyboardButton(text='Перелік спеціальностей')
    button2 = types.KeyboardButton(text='Документи та електронний кабінет вступника')
    button3 = types.KeyboardButton(text='Набір. Державне замовлення')
    button4 = types.KeyboardButton(text='Вступні випробування')
    button5 = types.KeyboardButton(text='Етапи вступу')
    button6 = types.KeyboardButton(text='Вартість навчання')
    button7 = types.KeyboardButton(text='Гуртожиток')
    button8 = types.KeyboardButton(text='Пільги на вступ')
    button9 = types.KeyboardButton(text='Вступ на контракт')
    button10 = types.KeyboardButton(text='Контакти')
    button11 = types.KeyboardButton(text='Повернутись назад')

    buttons.add(button1, button2, button3, button4, button5,
                button6, button7, button8, button9, button10,
                button11, row_width=1)
    return buttons


def keyboard_for_qualified_worker():
    buttons = types.ReplyKeyboardMarkup(resize_keyboard=True)

    button1 = types.KeyboardButton(text='Професії')
    button2 = types.KeyboardButton(text='Документи')
    button3 = types.KeyboardButton(text='Набір. Регіональне замовлення')
    button4 = types.KeyboardButton(text='Вступні випробування')
    button5 = types.KeyboardButton(text='Етапи вступу')
    button6 = types.KeyboardButton(text='Вартість навчання')
    button7 = types.KeyboardButton(text='Гуртожиток')
    button8 = types.KeyboardButton(text='Пільги на вступ')
    button9 = types.KeyboardButton(text='Вступ на контракт')
    button10 = types.KeyboardButton(text='Контакти')
    button11 = types.KeyboardButton(text='Повернутись назад')

    buttons.add(button1, button2, button3, button4, button5,
                button6, button7, button8, button9, button10,
                button11, row_width=1)
    return buttons


def keyboard_for_admission():
    buttons = types.ReplyKeyboardMarkup(resize_keyboard=True)

    button1 = types.KeyboardButton(text='Фаховий молодший бакалавр')
    button2 = types.KeyboardButton(text='Кваліфікований робітник')
    button3 = types.KeyboardButton(text='Повернутись назад')

    buttons.add(button1, button2, button3, row_width=1)
    return buttons


def keyboard_main():
    buttons = types.ReplyKeyboardMarkup(resize_keyboard=True)

    button1 = types.KeyboardButton(text='Загальноосвітній процес')
    button2 = types.KeyboardButton(text='Вступ ТФК')

    buttons.add(button1, button2)
    return buttons


if __name__ == '__main__':
    while True:
        try:
            bot.polling(none_stop=True)

        except Exception as e:
            print(e)
            time.sleep(15)
