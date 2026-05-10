from nicegui import ui
from components import ROLES
from api.user_client import get_users_admin, get_user_admin, put_role


def user_management_form_overview():
    ui.label("User Management").classes("text-4xl")

    users = get_users_admin()

    changes: dict[int, str] = {}

    if users.status_code == 401:
        ui.label("You are Unauthorized to view this content")

        return

    if users.status_code == 200:
        with ui.grid(columns=3).classes("w-full gap-0"):
            ui.label("id").classes("border p2")
            ui.label("Username").classes("border p2")
            ui.label("Role").classes("border p2")

            for user in users.json():
                ui.label(user["id"]).classes("border p1")
                ui.label(user["username"]).classes("border p1")
                ui.select(ROLES, value=user["role"], on_change=lambda e, uid=user["id"]: changes.update(
                    {uid: e.value}) or update_save_button()).classes("border p1")

    def update_save_button():
        save_button.set_enabled(len(changes) > 0)

    save_button = ui.button(
        "Save",
        on_click=lambda: update_roles()
    )

    def update_roles():
        for id in changes.keys():
            put_role(id, changes.get(id))
        changes.clear()
        update_save_button()

    update_save_button()
