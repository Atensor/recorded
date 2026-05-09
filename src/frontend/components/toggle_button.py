from nicegui import ui
from api.user_client import post_record_tag, delete_record_tag
from pages import TAG_STRINGS, ACTIVE_TAG_ICONS, DISABLED_TAG_ICONS


class ToggleButton(ui.button):

    def __init__(self, state: bool, *args, **kwargs) -> None:
        self._state = state
        super().__init__(*args, **kwargs)

    def update(self) -> None:
        with self.props.suspend_updates():
            if self._state:
                self.props("rounded", remove="outline")
            else:
                self.props("rounded outline")
        super().update()


class TagToggleButton(ToggleButton):

    def __init__(self, record_id: int, tag_index: str, *args, **kwargs):
        self._record_id = record_id
        self._tag_index = tag_index
        super().__init__(*args, **kwargs)
        self.on_click(self.toggle)
        self.classes("justify-start text-xl")

    def toggle(self):
        response = None
        if self._state:
            response = delete_record_tag(
                self._record_id, TAG_STRINGS[self._tag_index])
        else:
            response = post_record_tag(
                self._record_id, TAG_STRINGS[self._tag_index])
        if response.status_code == 200:
            self._state = not self._state
            self.icon = ACTIVE_TAG_ICONS[self._tag_index] if self._state else DISABLED_TAG_ICONS[self._tag_index]
            self.update()
