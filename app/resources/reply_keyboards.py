from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from app import resources


back_button = KeyboardButton(resources.text.BACK_REPLY_BUTTON)
cancel_button = KeyboardButton(resources.text.CANCEL_REPLY_BUTTON)


def make_main_menu_keyboard():

    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    calculator_button = KeyboardButton(resources.text.CALCULATOR_REPLY_BUTTON)
    echo_button = KeyboardButton(resources.text.ECHO_REPLY_BUTTON)

    keyboard.row(calculator_button, echo_button)

    return keyboard


def make_cancel_keyboard():

    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

    keyboard.row(cancel_button)

    return keyboard


def make_back_and_cancel_keyboard():

    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

    keyboard.row(back_button, cancel_button)

    return keyboard


def make_selecting_arithmetic_operator_keyboard():

    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=4)
    addition_button = KeyboardButton(resources.text.ADDITION_REPLY_BUTTON)
    subtraction_button = KeyboardButton(resources.text.SUBTRACTION_REPLY_BUTTON)
    multiplication_button = KeyboardButton(resources.text.MULTIPLICATION_REPLY_BUTTON)
    division_button = KeyboardButton(resources.text.DIVISION_REPLY_BUTTON)

    keyboard.row(addition_button, subtraction_button, multiplication_button, division_button)
    keyboard.row(back_button, cancel_button)

    return keyboard
