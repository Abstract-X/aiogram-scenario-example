from aiogram_scenario import CommonRegistrar, StatesMap

from app import common_handlers, resources, config, states, middlewares
from app.states import StatesGroup


def register_handlers(registrar: CommonRegistrar, states_map: StatesMap):

    registrar.register_message_handler(
        common_handlers.handle_start_command,
        states=StatesGroup.get_states(exclude=[StatesGroup.start_state]),
        commands=["start"]
    )
    registrar.register_message_handler(
        common_handlers.handle_cancel_reply_button,
        states=StatesGroup.get_states(exclude=[StatesGroup.start_state]),
        text=resources.text.CANCEL_REPLY_BUTTON
    )
    registrar.register_map_handlers(states_map)
