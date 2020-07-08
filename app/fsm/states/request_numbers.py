from aiogram_scenario import AbstractState, FSMPointer, StateRegistrar
from aiogram import Bot
from aiogram.types import Message
from aiogram.dispatcher import FSMContext

from app import resources, checks


async def _handle_number_message(update: Message, bot: Bot, fsm: FSMPointer, fsm_context: FSMContext, data_key: str):

    text = resources.text.GOOD_NUMBER_MESSAGE

    try:
        number = checks.check_number(update.text)
    except checks.IncorrectNumberTypeError:
        text = resources.text.INCORRECT_NUMBER_TYPE_MESSAGE
    except checks.NumberIsNotIntegerError:
        text = resources.text.NUMBER_IS_NOT_INTEGER_MESSAGE
    else:
        await fsm_context.update_data({data_key: number})

    await bot.send_message(
        chat_id=update.from_user.id,
        text=text,
        reply_to_message_id=update.message_id
    )

    if text == resources.text.GOOD_NUMBER_MESSAGE:
        await fsm.go_next()


async def handle_first_number_message(update: Message, bot: Bot, fsm: FSMPointer, fsm_context: FSMContext):

    await _handle_number_message(update, bot, fsm, fsm_context, "first_number")


async def handle_second_number_message(update: Message, bot: Bot, fsm: FSMPointer, fsm_context: FSMContext):

    await _handle_number_message(update, bot, fsm, fsm_context, "second_number")


async def handle_back_reply_button(_, fsm: FSMPointer):

    await fsm.go_back()


class RequestFirstNumberState(AbstractState):

    @classmethod
    async def process_transition(cls, update: Message, bot: Bot) -> None:

        await bot.send_message(
            chat_id=update.from_user.id,
            text=resources.text.REQUEST_FIRST_NUMBER_MESSAGE,
            reply_markup=resources.reply_keyboards.make_cancel_keyboard()
        )

    def register_handlers(self, registrar: StateRegistrar) -> None:

        registrar.register_message_handler(
            handle_first_number_message
        )


class RequestSecondNumberState(AbstractState):

    async def process_transition(self, update: Message, bot: Bot) -> None:

        await bot.send_message(
            chat_id=update.from_user.id,
            text=resources.text.REQUEST_SECOND_NUMBER_MESSAGE,
            reply_markup=resources.reply_keyboards.make_back_and_cancel_keyboard()
        )

    def register_handlers(self, registrar: StateRegistrar) -> None:

        registrar.register_message_handler(
            handle_back_reply_button,
            text=resources.text.BACK_REPLY_BUTTON
        )

        registrar.register_message_handler(
            handle_second_number_message
        )
