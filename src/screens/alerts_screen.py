import flet as ft

from widgets.drawer import Drawer

def AlertsScreen(page: ft.Page):


    return ft.View(
        route="/alerts",
        drawer=Drawer(page=page),
        scroll=ft.ScrollMode.ADAPTIVE,
        controls=[
            ft.AppBar(
                title=ft.Text("Alertas y Mensajes"),
                center_title=True,
            ),
            ft.Column(
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    
                    ft.Text("Alerta o mensaje de cuando el conteo del lote supera las 70 varillas", style=ft.TextStyle(size=15)),
                    ft.Image(
                        src="assets/alerta_2.png",
                        width=800,     
                        fit=ft.ImageFit.COVER,                                         
                    ),
                    ft.Divider(height=20),
                    ft.Text("Alerta o mensaje de cuando el conteo del lote es menor a 10 varillas", style=ft.TextStyle(size=15)),
                    ft.Image(
                        src="assets/alerta_3.png", 
                        width=800, 
                        fit=ft.ImageFit.COVER,                                             
                    ),
                    ft.Divider(height=20),
                    ft.Text("Alerta o mensaje cuando no se detectan varillas en la imagen", style=ft.TextStyle(size=15)),
                    ft.Image(
                        src="assets/alerta.png",  
                        width=800,   
                        fit=ft.ImageFit.COVER,                                         
                    ),
                ]
            ),
        ],
    )