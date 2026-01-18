from nicegui import ui
from pages import home, record, admin


ui.add_css('''

    .nicegui-content{
        align-items: center;
    }''', shared=True)


home.page()
record.page()
admin.page()
ui.run()
