from nicegui import ui
from collections.abc import Callable
from state.user_sate import UserFormState
from api.user_client import get_user_exists

PASSWORD_REQUIREMENTS = '''Password needs be at least 3 Characters long
And it has to contain at least one Character and Number'''


def user_form_card(user: UserFormState, top_label: str, api_request: Callable[[UserFormState], None]):
    with ui.card(align_items="center"):
        ui.label(top_label).classes("text-4xl")
        with ui.element("div"):
            username_input = ui.input(
                label="Username",
                placeholder="Enter Username",
                on_change=lambda e:
                    setattr(user, "username", e.value) or
                    update_button(),
                validation=lambda value: "Username needs to be 3 Characters long" if len(
                    value) < 3 else None
            )

            ui.input(
                label="Password",
                placeholder="Enter Password",
                password=True,
                on_change=lambda e:
                    setattr(user, "password", e.value) or
                    update_button(),
                validation=lambda value: None if validate_password(
                    value) else PASSWORD_REQUIREMENTS
            )

            ui.link(
                text="Sign Up" if top_label == "Sign In" else "Sign In",
                target=f"/login/{"signup" if top_label == "Sign In" else "signin"}",
            )

            button = ui.button(
                top_label,
                on_click=lambda: handle_submit()
            )

            def update_button():
                button.set_enabled(user.is_valid())

            update_button()

            def validate_password(password: str) -> bool:
                if len(password) < 3:
                    return False

                alpha_valid: bool = False
                num_valid: bool = False

                for c in password:
                    if c.isalpha():
                        alpha_valid = True
                    if c.isnumeric():
                        num_valid = True

                return alpha_valid and num_valid

            def handle_submit():
                if bool(get_user_exists(user.username)) and top_label == "Sign up":
                    username_input.props(
                        'error error-message="This Username is already taken"')
                else:
                    username_input.props('error=false')
                    if api_request(user):
                        button.props('error=false')
                        ui.navigate.back()
                    else:
                        button.props('error error-message="Unauthorized"')
