from nicegui import ui, events
from state.record_state import RecordMinState, Artist
from api.cover_art_client import put_cover_art
from api.record_client import get_records_min


def cover_art_form(record_state: RecordMinState):
    records = get_records_min()
    global file
    file = None

    ui.label("Upload Cover Art").classes("text-h4")
    ui.select(
        {r["id"]: r["title"] for r in records},
        label="Select Record",
        on_change=lambda e:
            set_record(e.value) or
            update_save_button()
    ).classes("max-w-full")

    def set_record(record_id: int):
        for record in records:
            if record["id"] == record_id:
                setattr(record_state, "id", record_id)
                setattr(record_state, "title", record["title"])
                setattr(record_state, "artist", Artist(record["artist"]))
                return

    async def handle_upload(e: events.UploadEventArguments):
        global file
        file = e.file
        file.content = await e.file.read()
        update_save_button()
        ui.notify(f"Uploaded {file.name}")

    ui.upload(
        on_upload=handle_upload,
        max_file_size=50_000_000,
        auto_upload=True
    ).classes("max-w-full")

    def update_save_button():
        if file is not None:
            save_button.set_enabled(record_state.is_valid() and file)
            return
        save_button.disable()

    save_button = ui.button(
        "Save",
        on_click=lambda:
        put_cover_art(record_state.id, get_files()) or
        update_save_button()
    )

    def get_files():
        return {
            "file": (f"{record_state.title}.{file.content_type.split("/")[1]}", file.content, file.content_type)
        }
    update_save_button()
