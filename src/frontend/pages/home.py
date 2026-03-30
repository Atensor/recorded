from nicegui import ui
import json
from datetime import date
from components.header import header
from components.record_card import record_card
from components.toggle_button import TagToggleButton
from api.record_client import get_records
from api.user_client import get_my_record_tags


def page():
    @ui.page("/")
    def home():
        header()
        ui.link(text="Admin Panel", target=("/admin")
                ).classes("clean-link")  # TEMP
        for record in get_records():
            with ui.element("div").classes("nicegui-card items-center"):
                record_card(record)
                tags = get_my_record_tags(record["id"])
                if tags.status_code == 200:
                    with ui.button_group().props("rounded") as button_group:
                        TAG_STRINGS = ["favourite",
                                       "wanted", "digital", "physical"]
                        tag_states: list[bool] = [
                            False for _ in range(len(TAG_STRINGS))
                        ]
                        for tag in tags.json():
                            tag_states[TAG_STRINGS.index(tag["tag"])] = True
                        for i in range(len(TAG_STRINGS)):
                            TagToggleButton(record_id=record["id"],
                                            state=tag_states[i], text=TAG_STRINGS[i].capitalize())
