import flet as ft

def CardHistorial(src_base64:str, count:int, date:str, hour:str):
    return ft.Card(
        width=300,
        height=150,                
        margin=20,
        
        content=ft.Row(
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                ft.Image(
                    src_base64=src_base64,
                    width=80,
                    height=80,
                    border_radius=20,
                    fit=ft.ImageFit.COVER,
                ),
                ft.Column(
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        ft.Text("Varillas detectadas: " + str(count)),
                        ft.Text("Fecha: " + date),
                        ft.Text("Hora: " + hour),
                    ]
                )
            ]
        
        )
    )