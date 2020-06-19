from aiogram_scenario import AbstractState, FSMPointer, StateRegistrar
from aiogram import Bot
from aiogram.types import Message
from aiogram.dispatcher import FSMContext

from app import resources


async def _handle_arithmetic_operator(update: Message, bot: Bot, fsm_context: FSMContext, operator: str):

    data = await fsm_context.get_data()
    first_number = data["first_number"]
    second_number = data["second_number"]

    if operator == "+":
        result = first_number + second_number
    elif operator == "-":
        result = first_number - second_number
    elif operator == "*":
        result = first_number * second_number
    elif operator == "/":
        try:
            result = first_number / second_number
        except ZeroDivisionError:
            await bot.send_message(
                chat_id=update.from_user.id,
                text=resources.text.ZERO_DIVISION_MESSAGE
            )
            return
    else:
        raise ValueError(f"unknown arithmetic operator: {operator}")

    await bot.send_message(
        chat_id=update.from_user.id,
        text=resources.text.CALCULATE_RESULT_MESSAGE.format(
            first_number=first_number,
            operator=operator,
            second_number=second_number,
            result=result
        )
    )


class RequestOperatorState(AbstractState):

    @classmethod
    async def process_transition(cls, update: Message, bot: Bot) -> None:

        await bot.send_message(
            chat_id=update.from_user.id,
            text=resources.text.REQUEST_OPERATOR_MESSAGE,
            reply_markup=resources.reply_keyboards.make_selecting_arithmetic_operator_keyboard()
        )

    @classmethod
    async def handle_addition_reply_button(cls, update: Message, bot: Bot, fsm_context: FSMContext):

        await _handle_arithmetic_operator(update, bot, fsm_context, "+")

    @classmethod
    async def handle_subtraction_reply_button(cls, update: Message, bot: Bot, fsm_context: FSMContext):

        await _handle_arithmetic_operator(update, bot, fsm_context, "-")

    @classmethod
    async def handle_multiplication_reply_button(cls, update: Message, bot: Bot, fsm_context: FSMContext):

        await _handle_arithmetic_operator(update, bot, fsm_context, "*")

    @classmethod
    async def handle_division_reply_button(cls, update: Message, bot: Bot, fsm_context: FSMContext):

        await _handle_arithmetic_operator(update, bot, fsm_context, "/")

    @classmethod
    async def handle_back_reply_button(cls, update: Message, fsm: FSMPointer):

        await fsm.go_back()

    def register_handlers(self, registrar: StateRegistrar) -> None:

        registrar.register_message_handler(
            self.handle_back_reply_button,
            text=resources.text.BACK_REPLY_BUTTON
        )

        registrar.register_message_handler(
            self.handle_addition_reply_button,
            text=resources.text.ADDITION_REPLY_BUTTON
        )

        registrar.register_message_handler(
            self.handle_subtraction_reply_button,
            text=resources.text.SUBTRACTION_REPLY_BUTTON
        )

        registrar.register_message_handler(
            self.handle_multiplication_reply_button,
            text=resources.text.MULTIPLICATION_REPLY_BUTTON
        )

        registrar.register_message_handler(
            self.handle_division_reply_button,
            text=resources.text.DIVISION_REPLY_BUTTON
        )
