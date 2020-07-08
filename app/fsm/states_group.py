import aiogram_scenario
from . import states


class StatesGroup(aiogram_scenario.StatesGroup):

    start_state = states.StartState()
    main_menu_state = states.MainMenuState()
    request_echo_message_state = states.RequestEchoMessageState()
    request_first_number_state = states.RequestFirstNumberState()
    request_second_number_state = states.RequestSecondNumberState()
    request_operator_state = states.RequestOperatorState()
