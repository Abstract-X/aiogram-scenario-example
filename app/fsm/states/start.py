from aiogram_scenario import AbstractState, StateRegistrar, FSMPointer
from aiogram import Bot
from aiogram.types import Message

from app import resources


async def handle_start_command(update: Message, bot: Bot, fsm: FSMPointer):

    await bot.send_message(
        chat_id=update.from_user.id,
        text=resources.text.GREETING_MESSAGE.format(full_name=update.from_user.full_name)
    )

    await fsm.go_next()


class StartState(AbstractState):

    async def process_transition(self, *args, **kwargs) -> None:

        pass

    def register_handlers(self, registrar: StateRegistrar) -> None:

        registrar.register_message_handler(
            handle_start_command,
            commands=["start"]
        )
