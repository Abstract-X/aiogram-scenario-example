# noinspection PyUnresolvedReferences
from aiogram.utils.markdown import (
    hbold as b,            # <b>...</b>
    hitalic as i,          # <i>...</i>
    hpre as pre,           # <pre>...</pre>
    hcode as code,         # <code>...</code>
    hlink as link,         # <a href="{link}">...</a>
    hide_link,             # <a href="{link}">&#8203;</a>
    hstrikethrough as s,   # <s>...</s>
    hunderline as u        # <u>...</u>
)


GREETING_MESSAGE = """✌🏼 Greetings, {full_name}! 
In this bot, you can calculate two numbers and listen to your own echo!"""
MAIN_MENU_MESSAGE = """💠 Main menu."""
REQUEST_FIRST_NUMBER_MESSAGE = f"""1️⃣  Please send me the {u('first')} number."""
REQUEST_SECOND_NUMBER_MESSAGE = f"""2️⃣  Please send me the {u('second')} number."""
REQUEST_OPERATOR_MESSAGE = """📟 Please select a arithmetic operator."""
REQUEST_ECHO_MESSAGE_MESSAGE = """💬 What would you like to hear back?"""
GOOD_NUMBER_MESSAGE = """👍🏼 Great number!"""
INCORRECT_NUMBER_TYPE_MESSAGE = """♻️ Hrm... Strange type, I wanted a number... Please try again."""
NUMBER_IS_NOT_INTEGER_MESSAGE = """♻️ Hrm... I wanted an integer, not a fractional... Please try again."""
CALCULATE_RESULT_MESSAGE = """✅ {first_number} {operator} {second_number} = {result:.1f}!
Let's try something else?"""
ZERO_DIVISION_MESSAGE = """⛔️ Hrm... You tried to divide by zero, this is impossible.
Select a different operator."""

CALCULATOR_REPLY_BUTTON = """📟 Calculator"""
ECHO_REPLY_BUTTON = """📢 Echo"""
BACK_REPLY_BUTTON = """↩️ Back"""
CANCEL_REPLY_BUTTON = """❎ Cancel"""
ADDITION_REPLY_BUTTON = """➕"""
SUBTRACTION_REPLY_BUTTON = """➖"""
MULTIPLICATION_REPLY_BUTTON = """✖️"""
DIVISION_REPLY_BUTTON = """➗"""
