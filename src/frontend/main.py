from nicegui import ui
from pages import home, record


ui.add_css('''

    .nicegui-content{
        align-items: center;
    }''', shared=True)


home.page()
record.page()
ui.run()
