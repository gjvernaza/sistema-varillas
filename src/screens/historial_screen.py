import flet as ft

from services.db.database import DB
from widgets.card_historial import CardHistorial
from widgets.drawer import Drawer



def HistorialScreen(page: ft.Page):

    db =DB("./src/services/db/users.db")    
    images = db.get_images()
    row_card = ft.Row()


    if len(images) == 0:
        row_card.controls.append(
            ft.Text("No hay imágenes guardadas")
        )
    for img in images:
        str_base64 = img["base64_str"]
        count = img["count"]
        date = img["date"]
        hour = img["hour"]
        row_card.controls.append(
            CardHistorial(src_base64=str_base64, count=count, date=date, hour=hour)
        )
        row_card.wrap = True
        row_card.alignment = ft.MainAxisAlignment.CENTER

    
    return ft.View(
        route="/historial",
        drawer=Drawer(page=page),
        scroll=ft.ScrollMode.ADAPTIVE, 
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,       
        controls=[
            ft.AppBar(
                title=ft.Text("Historial de producción"),
                center_title=True,
              
            ),                      
            row_card
            

        ],

    )