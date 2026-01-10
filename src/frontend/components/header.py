from nicegui import ui


def header():
    ui.add_css('''
        @layer utilities{
        .clean-link{
            text-decoration-line: none;
            color: rgb(255 255 255);
        }
        .card{
            border-radius: 25px;
            min-width: 80%
        }
        .image{
            border-radius: 25px;
        }
    }''')
    with ui.header().classes("items-center justify-between bg-gray-100"):
        ui.link("recorded", "/").classes("clean-link text-5xl font-bold")
        with ui.row().style("margin-top: auto; margin-bottom: auto;"):
            ui.link("about", "/about").classes("clean-link text-xl")
            ui.link("Log In", "/login").classes("clean-link text-xl")
