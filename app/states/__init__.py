import aiogram_scenario
from aiogram_scenario import StatesMap

from .start import StartState
from .main_menu import MainMenuState
from .request_echo_message import RequestEchoMessageState
from .request_numbers import RequestFirstNumberState, RequestSecondNumberState
from .request_operator import RequestOperatorState
from app import common_handlers


class StatesGroup(aiogram_scenario.StatesGroup):

    start_state = StartState()
    main_menu_state = MainMenuState()
    request_echo_message_state = RequestEchoMessageState()
    request_first_number_state = RequestFirstNumberState()
    request_second_number_state = RequestSecondNumberState()
    request_operator_state = RequestOperatorState()


def make_map() -> StatesMap:

    states_map = StatesMap(start_state=StatesGroup.start_state)

    states_map.add_routings({

        # MAIN MENU
        StatesGroup.main_menu_state: [
            StartState.handle_start_command,
            RequestEchoMessageState.handle_echo_message,
            common_handlers.handle_start_command,
            common_handlers.handle_cancel_reply_button
        ],

        # REQUEST ECHO MESSAGE
        StatesGroup.request_echo_message_state: [
            MainMenuState.handle_echo_reply_button
        ],

        # REQUEST FIRST NUMBER
        StatesGroup.request_first_number_state: [
            MainMenuState.handle_calculate_reply_button
        ],

        # REQUEST SECOND NUMBER
        StatesGroup.request_second_number_state: [
            RequestFirstNumberState.handle_first_number_message
        ],

        # REQUEST OPERATOR
        StatesGroup.request_operator_state: [
            RequestSecondNumberState.handle_second_number_message
        ]

    })

    return states_map
