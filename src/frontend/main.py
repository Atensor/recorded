from nicegui import ui
from config import get_storage_secret_key
from pages import home, record, track, admin, artist, label, genre, login


ui.add_css('''
    .nicegui-content{
        align-items: center;
        color: white;
        filter: brightness(75%);
        background: #202225;
    }
    .clean-link {
        color: inherit;
        text-decoration: none;
    }
    .clean-link:hover {
        color: inherit;
        text-decoration: underline;
    }
    .clean-link-header {
        color: inherit;
        text-decoration: none;
    }
    .clean-link-header:hover {
        filter: brightness(75%);
    }
    .nicegui-card{
        border-radius: 25px;
        min-width: 80%;
        background: #2F3136;
    }
    .nicegui-tab-panel {
        background: #2F3136;
    }
    .image{
        border-radius: 25px;
        filter: brightness(100%)
    }
''', shared=True)


home.page()
record.page()
admin.page()
artist.page()
track.page()
label.page()
genre.page()
login.page()

ui.run(show=False, storage_secret=get_storage_secret_key())
