import flet as ft


def PortadaScreen(page: ft.Page):

    img = ft.Container(
        content=ft.Image(
            src="./assets/logo_blanco.jpg" if page.theme_mode == ft.ThemeMode.LIGHT else "./assets/logo_negro.jpg",
            fit=ft.ImageFit.COVER,
            
        ),
        border_radius=ft.border_radius.all(30),
        width=350,
        height=350,
        

    )

    return ft.View(
        route="/portada",
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        vertical_alignment=ft.MainAxisAlignment.CENTER,
        scroll=ft.ScrollMode.ADAPTIVE,
        controls=[
            ft.Text(value="SISTEMA SCADA DE CONTEO DE VARILLAS",
                    style=ft.TextStyle(size=20, weight=ft.FontWeight.BOLD)),
            img,
            ft.Container(
                width=800,

                content=ft.Column(
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        ft.Row(
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                            controls=[
                                ft.ElevatedButton(
                                    text="Configuración",
                                    on_click=lambda e: page.go("/settings"),
                                    elevation=10,
                                    icon=ft.icons.SETTINGS,
                                    width=300,
                                ),
                                ft.ElevatedButton(
                                    text="Historial de producción",
                                    on_click=lambda e: page.go("/historial"),
                                    elevation=10,
                                    icon=ft.icons.HISTORY,
                                    width=300,
                                ),
                            ]
                        ),
                        ft.Row(
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                            controls=[
                                ft.ElevatedButton(
                                    text="Visualización de imágenes",
                                    on_click=lambda e: page.go("/images"),
                                    elevation=10,
                                    icon=ft.icons.IMAGE,
                                    width=300,
                                ),
                                ft.ElevatedButton(
                                    text="Ayuda y Documentación",
                                    on_click=lambda e: page.go("/help"),
                                    elevation=10,
                                    icon=ft.icons.HELP,
                                    width=300,
                                ),
                            ]
                        ),
                        ft.Row(
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                            controls=[
                                ft.ElevatedButton(
                                    text="Cerrar sesión",
                                    on_click=lambda e: page.go("/"),
                                    elevation=10,
                                    icon=ft.icons.LOGOUT,
                                    width=300,
                                ),
                                ft.ElevatedButton(
                                    text="Alertas y mensajes",
                                    on_click=lambda e: page.go("/alerts"),
                                    elevation=10,
                                    icon=ft.icons.NOTIFICATIONS,
                                    width=300,
                                ),
                            ]
                        ),
                        ft.ElevatedButton(
                            text="Inicio y Procesamiento",
                            on_click=lambda e: page.go("/home"),
                            elevation=10,
                            icon=ft.icons.HOME,
                            width=300,
                        ),

                    ]
                ),
            ),





        ]
    )
