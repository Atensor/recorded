from nicegui import ui
from pages import home, record, track, admin, artist


ui.add_css('''

    .nicegui-content{
        align-items: center;
    }''', shared=True)


home.page()
record.page()
admin.page()
artist.page()
track.page()
ui.run()
