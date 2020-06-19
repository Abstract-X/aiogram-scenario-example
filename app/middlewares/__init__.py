from aiogram import Dispatcher, Bot
from aiogram_scenario import FSM, FSMMiddleware

from .service import ServiceMiddleware


def setup(dispatcher: Dispatcher, bot: Bot, fsm: FSM):

    dispatcher.middleware.setup(ServiceMiddleware(dispatcher, bot))
    dispatcher.middleware.setup(FSMMiddleware(fsm=fsm))
