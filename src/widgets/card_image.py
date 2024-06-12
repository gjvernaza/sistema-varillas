import flet as ft

def CardImage(src_base64, name, count):
    return ft.Card(
        width=350,
        height=350,
        elevation=20,
        margin=20,
        content=ft.Container(
            padding=7,
            content=ft.Column(
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    ft.Text(value=name, style=ft.TextStyle(
                        size=20, weight=ft.FontWeight.BOLD)),
                    ft.Image(
                        src_base64=src_base64,
                        fit=ft.ImageFit.COVER,
                    ),
                    ft.Text(value=f"Número de varillas: {count}", style=ft.TextStyle(
                        size=20, weight=ft.FontWeight.BOLD)),
                ]
            ),
        )
    )