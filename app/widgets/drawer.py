import flet as ft

class Drawer(ft.NavigationDrawer):
    def __init__(self, page: ft.Page):

        super().__init__(
            on_change=self.check_item_clicked,
            elevation=4,
            controls=[
                ft.Container(height=12),
                ft.NavigationDrawerDestination(
                    label="Inicio y Procesamiento",
                    icon=ft.icons.HOME_WORK,

                ),
                ft.Divider(thickness=2),
                ft.NavigationDrawerDestination(
                    icon_content=ft.Icon(ft.icons.HISTORY),
                    label="Historial de producción",

                ),
                ft.NavigationDrawerDestination(
                    icon_content=ft.Icon(ft.icons.IMAGE_SEARCH),
                    label="Visualización de imágenes",

                ),
                ft.NavigationDrawerDestination(
                    icon_content=ft.Icon(ft.icons.HELP),
                    label="Ayuda y Documentación",
                ),
                ft.NavigationDrawerDestination(
                    icon_content=ft.Icon(ft.icons.NOTIFICATIONS),
                    label="Alertas y mensajes",
                ),
                ft.NavigationDrawerDestination(
                    icon_content=ft.Icon(ft.icons.SETTINGS),
                    label="Configuración",
                ),
                ft.NavigationDrawerDestination(
                    icon_content=ft.Icon(ft.icons.HOME),
                    label="Portada",
                ),
                ft.NavigationDrawerDestination(
                    icon_content=ft.Icon(ft.icons.LOGOUT),
                    label="Cerrar sesión",

                ),

            ],
        )
        self.page = page


    def check_item_clicked(self, e):
        current_index = e.control.selected_index
        print(current_index)
        if current_index == 0:
            self.page.go("/home")
        elif current_index == 1:
            self.page.go("/historial")
        elif current_index == 2:
            self.page.go("/images")
        elif current_index == 3:
            self.page.go("/help")
        elif current_index == 4:
            self.page.go("/alerts")
        elif current_index == 5:
            self.page.go("/settings")
        elif current_index == 6:
            self.page.go("/portada")
        elif current_index == 7:
            self.page.go("/")
