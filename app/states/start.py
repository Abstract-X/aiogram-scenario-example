from aiogram_scenario import AbstractState, StateRegistrar, FSMPointer
from aiogram import Bot
from aiogram.types import Message

from app import resources


class StartState(AbstractState):

    @classmethod
    async def process_transition(cls, *args, **kwargs) -> None:

        pass

    @classmethod
    async def handle_start_command(cls, update: Message, bot: Bot, fsm: FSMPointer):

        await bot.send_message(
            chat_id=update.from_user.id,
            text=resources.text.GREETING_MESSAGE.format(full_name=update.from_user.full_name)
        )

        await fsm.go_next()

    def register_handlers(self, registrar: StateRegistrar) -> None:

        registrar.register_message_handler(
            self.handle_start_command,
            commands=["start"]
        )
