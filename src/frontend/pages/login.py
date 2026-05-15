from nicegui import ui
from src.frontend.components import header, user_form
from src.frontend.state.user_sate import UserFormState
from src.frontend.api.user_client import post_user
from src.frontend.api.auth_client import post_token


def page():
    @ui.page("/login/signin")
    def login():
        header.header()
        user_state = UserFormState()

        user_form.user_form_card(user_state, "Sign In", post_token)

    @ui.page("/login/signup")
    def signup():
        header.header()
        user_state = UserFormState()

        user_form.user_form_card(user_state, "Sign Up", post_user)
