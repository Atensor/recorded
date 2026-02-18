from nicegui import ui


def header():
    with ui.header().classes("items-center justify-between") as header:
        header.style("bg-color: #62a3d6; filter: brightness(75%);")
        ui.link("recorded", "/").classes("clean-link-header text-5xl font-bold")
        with ui.row().style("margin-top: auto; margin-bottom: auto;"):
            ui.link("about", "/about").classes("clean-link-header text-xl")
            ui.link("Log In", "/login").classes("clean-link-header text-xl")
