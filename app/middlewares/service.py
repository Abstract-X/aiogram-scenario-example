from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram import Bot, Dispatcher


class ServiceMiddleware(BaseMiddleware):

    def __init__(self, dispatcher: Dispatcher, bot: Bot):

        super().__init__()
        self.dispatcher = dispatcher
        self.bot = bot

    async def on_process_message(self, _, data: dict):

        self._setup_instances(data)

    def _setup_instances(self, data: dict):

        data["bot"] = self.bot
        data["dispatcher"] = self.dispatcher
        data["fsm_context"] = data.get("state")
