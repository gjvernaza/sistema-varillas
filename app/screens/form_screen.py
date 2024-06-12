import flet as ft

from services.db.database import DB


def FormScreen(page: ft.Page):
    db = DB("./services/db/users.db")
    db.insert_user("admin", "admin")

    def login_click(e):
        users = db.get_users()
        if users[0]["password"] == text_field_password.value and users[0]["username"] == text_field_user.value:
            page.go("/portada")
            db.close()
        else:
            print("Usuario o contraseña incorrectos")
            text_incorrect.visible = True
            text_incorrect.update()

    text_incorrect = ft.Text(
        "Usuario o contraseña incorrectos",
        style=ft.TextStyle(size=17, weight=ft.FontWeight.BOLD),
        color=ft.colors.ERROR,
        visible=False,
        animate_size=15,
    )

    text_field_user = ft.TextField(label="Usuario")
    text_field_password = ft.TextField(
        label="Contraseña", password=True, can_reveal_password=True)

    return ft.View(
        route="/",
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        vertical_alignment=ft.MainAxisAlignment.CENTER,

        controls=[

            ft.Card(
                width=400,
                height=400,
                elevation=20,
                margin=20,

                content=ft.Container(
                    padding=20,
                    content=ft.Column(
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        controls=[
                            ft.Text(value="Inicio de sesión", style=ft.TextStyle(
                                size=20, weight=ft.FontWeight.BOLD)),
                            text_field_user,
                            text_field_password,
                            ft.ElevatedButton(
                                "Iniciar sesión", on_click=login_click),
                            text_incorrect,
                        ]
                    ),

                ),




            ),

        ]
    )
