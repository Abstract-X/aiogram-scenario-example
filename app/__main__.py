import logging

from aiogram import Bot, Dispatcher, executor
from aiogram.types import ParseMode
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram_scenario import CommonRegistrar, FSM

import app


logger = logging.getLogger("aiogram_scenario")
app.config.setup_logger(logger)

bot = Bot(token=app.config.BOT_TOKEN, parse_mode=ParseMode.HTML)
dispatcher = Dispatcher(bot, storage=MemoryStorage())
registrar = CommonRegistrar(dispatcher)
states_map = app.states.make_map()
fsm = FSM(stack_storage=MemoryStorage(), states_map=states_map, dispatcher=dispatcher)

app.register_handlers(registrar, states_map)
app.middlewares.setup(dispatcher, bot, fsm)

logger.info("Launched!")
executor.start_polling(dispatcher, fast=False)
