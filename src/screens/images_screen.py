import flet as ft

from services.db.database import DB
from widgets.card_image import CardImage
from widgets.drawer import Drawer


def ImagesScreen(page: ft.Page):

    db = DB("./src/services/db/users.db")
    images = db.get_images()    
    row_images_card = ft.Row()
    if len(images) == 0:
        row_images_card.controls.append(
            ft.Text("No hay imágenes guardadas")
        )
    for img in images:
        str_base64 = img["base64_str"]
        name = img["name"]
        count = img["count"]
        row_images_card.controls.append(
            CardImage(src_base64=str_base64, name=name, count=count)
        )
        row_images_card.wrap = True


    return ft.View(
        route="/images",
        drawer=Drawer(page=page),
        scroll=ft.ScrollMode.ADAPTIVE,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        controls=[
            ft.AppBar(
                title=ft.Text("Visualización de imágenes"),
                center_title=True,
            ),
            ft.Container(
                padding=ft.padding.all(20),
                content=row_images_card
            )
        ]
    )
