from nicegui import ui
from components import header, user_form
from state.user_sate import UserFormState
from api.user_client import post_user
from api.auth_client import post_token


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
