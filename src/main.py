
import flet as ft

from screens.alerts_screen import AlertsScreen
from screens.form_screen import FormScreen
from screens.help_screen import HelpScreen
from screens.historial_screen import HistorialScreen
from screens.home_screen import HomeScreen
from screens.images_screen import ImagesScreen
from screens.portada_screen import PortadaScreen
from screens.settings_screen import SettingsScreen

def main(page: ft.Page):
    
    def route_change(route):
        page.views.clear()
        if page.route == "/historial":
            page.views.append(
                HistorialScreen(page=page)
            )
        elif page.route == "/images":
            page.views.append(
                ImagesScreen(page=page)                
            )
        elif page.route == "/home":
            page.views.append(
                HomeScreen(page=page)
            )
        elif page.route == "/portada":
            page.views.append(
                PortadaScreen(page=page)
            )
        elif page.route == "/help":
            page.views.append(
                HelpScreen(page=page)
            )
        elif page.route == "/alerts":
            page.views.append(
                AlertsScreen(page=page)
            )
        elif page.route == "/settings":
            page.views.append(
                SettingsScreen(page=page)
            )
        elif page.route == "/":            
            page.views.append(
                FormScreen(page=page)
            )

        page.update()

    page.title = "Vision SCADA"    
    page.theme = ft.Theme(color_scheme_seed="indigo", font_family="Roboto", appbar_theme=ft.AppBarTheme(bgcolor=ft.colors.INDIGO))
    
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window_width = 950
    page.window_height = 700
    page.on_route_change = route_change
    page.go(page.route)

ft.app(target=main)
