import logging

from aiogram import Bot, Dispatcher, executor
from aiogram.types import ParseMode
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram_scenario import CommonRegistrar, StatesMap, FSM

import app
from app.fsm import StatesGroup


scenario_logger = logging.getLogger("aiogram_scenario")
bot = Bot(token=app.config.BOT_TOKEN, parse_mode=ParseMode.HTML)
dispatcher = Dispatcher(bot, storage=MemoryStorage())
common_registrar = CommonRegistrar(dispatcher)
states_map = app.fsm.make_map()
fsm = FSM(stack_storage=MemoryStorage(), states_map=states_map, dispatcher=dispatcher)


def setup_scenario_logger(logger):

    logger.setLevel(logging.DEBUG)
    stream_handler = logging.StreamHandler()
    formatter = logging.Formatter("[%(asctime)s] - %(message)s", datefmt="%d.%m %H:%M:%S")
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)


def register_handlers(registrar: CommonRegistrar, states_map: StatesMap):

    registrar.register_message_handler(
        app.common_handlers.handle_start_command,
        states=StatesGroup.get_states(exclude=[StatesGroup.start_state]),
        commands=["start"]
    )
    registrar.register_message_handler(
        app.common_handlers.handle_cancel_reply_button,
        states=StatesGroup.get_states(exclude=[StatesGroup.start_state]),
        text=app.resources.text.CANCEL_REPLY_BUTTON
    )
    registrar.register_map_handlers(states_map)


async def execute_on_startup(_):

    setup_scenario_logger(scenario_logger)
    app.middlewares.setup(dispatcher, bot, fsm)
    register_handlers(common_registrar, states_map)


if __name__ == '__main__':
    scenario_logger.info("Launched!")
    executor.start_polling(dispatcher, on_startup=execute_on_startup, fast=False)
