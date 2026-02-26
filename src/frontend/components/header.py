from nicegui import ui
from state.auth_state import TokenState, clear_token
from api.user_client import get_user_me


def header():
    with ui.header().classes("items-center justify-between") as header:
        header.style("bg-color: #62a3d6; filter: brightness(75%);")
        ui.link("recorded", "/").classes("clean-link-header text-5xl font-bold")
        with ui.row().style("margin-top: auto; margin-bottom: auto;"):
            response = get_user_me()
            ui.link("about", "/about").classes("clean-link-header text-xl")
            if response.status_code == 401:
                ui.link(
                    "Log In", "/login/signin").classes("clean-link-header text-xl")
            else:
                ui.link("Log Out", "/login/signin").on("click",
                                                       handler=lambda: clear_token()).classes("clean-link-header text-xl")
