from aiogram_scenario import AbstractState, FSMPointer, StateRegistrar
from aiogram import Bot
from aiogram.types import Message

from app import resources


class MainMenuState(AbstractState):

    @classmethod
    async def process_transition(cls, update: Message, bot: Bot) -> None:

        await bot.send_message(
            chat_id=update.from_user.id,
            text=resources.text.MAIN_MENU_MESSAGE,
            reply_markup=resources.reply_keyboards.make_main_menu_keyboard()
        )

    @classmethod
    async def handle_calculate_reply_button(cls, update: Message, fsm: FSMPointer):

        await fsm.go_next()

    @classmethod
    async def handle_echo_reply_button(cls, update: Message, fsm: FSMPointer):

        await fsm.go_next()

    def register_handlers(self, registrar: StateRegistrar) -> None:

        registrar.register_message_handler(
            self.handle_calculate_reply_button,
            text=resources.text.CALCULATOR_REPLY_BUTTON
        )

        registrar.register_message_handler(
            self.handle_echo_reply_button,
            text=resources.text.ECHO_REPLY_BUTTON
        )
