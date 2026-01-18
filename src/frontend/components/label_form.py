from nicegui import ui
from state.label_state import LabelFormState
from api.label_client import post_label


def label_form(label: LabelFormState):
    ui.label("Label").classes("text-h4")

    ui.input(
        "Label",
        placeholder="Enter Label Name",
        on_change=lambda e:
            setattr(label, "name", e.value) or
            update_save_button()
    )

    save_button = ui.button(
        "Save",
        on_click=lambda: post_label(label.to_payload())
    )

    def update_save_button():
        save_button.set_enabled(label.is_valid())

    update_save_button()
