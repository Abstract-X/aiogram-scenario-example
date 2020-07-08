from aiogram_scenario import AbstractState, FSMPointer, StateRegistrar
from aiogram import Bot
from aiogram.types import Message

from app import resources


async def handle_echo_message(update: Message, bot: Bot, fsm: FSMPointer):

    await bot.send_message(
        chat_id=update.from_user.id,
        text=update.text
    )

    await fsm.go_next()


class RequestEchoMessageState(AbstractState):

    async def process_transition(self, update: Message, bot: Bot) -> None:

        await bot.send_message(
            chat_id=update.from_user.id,
            text=resources.text.REQUEST_ECHO_MESSAGE_MESSAGE,
            reply_markup=resources.reply_keyboards.make_cancel_keyboard()
        )

    def register_handlers(self, registrar: StateRegistrar) -> None:

        registrar.register_message_handler(
            handle_echo_message
        )
