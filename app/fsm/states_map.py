from aiogram_scenario import StatesMap

from app import common_handlers
from .states_group import StatesGroup
from . import states


def make_map() -> StatesMap:

    states_map = StatesMap(start_state=StatesGroup.start_state)

    states_map.add_routings({

        # MAIN MENU
        StatesGroup.main_menu_state: [
            states.start.handle_start_command,
            states.request_echo_message.handle_echo_message,
            common_handlers.handle_start_command,
            common_handlers.handle_cancel_reply_button
        ],

        # REQUEST ECHO MESSAGE
        StatesGroup.request_echo_message_state: [
            states.main_menu.handle_echo_reply_button
        ],

        # REQUEST FIRST NUMBER
        StatesGroup.request_first_number_state: [
            states.main_menu.handle_calculate_reply_button
        ],

        # REQUEST SECOND NUMBER
        StatesGroup.request_second_number_state: [
            states.request_numbers.handle_first_number_message
        ],

        # REQUEST OPERATOR
        StatesGroup.request_operator_state: [
            states.request_numbers.handle_second_number_message
        ]

    })

    return states_map
