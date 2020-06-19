from aiogram.types import Message
from aiogram_scenario import FSMPointer


async def handle_start_command(update: Message, fsm: FSMPointer):

    await fsm.go_next()


async def handle_cancel_reply_button(update: Message, fsm: FSMPointer):

    await fsm.go_next()
