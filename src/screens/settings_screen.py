import flet as ft

from widgets.drawer import Drawer


def SettingsScreen(page: ft.Page):

    def change_theme(e):
        page.theme_mode = ft.ThemeMode.DARK if switch.value else ft.ThemeMode.LIGHT
        page.update()

    
    def button_clicked(e):
        color = radio_color.value
        page.theme.color_scheme_seed = color
        page.theme.appbar_theme.bgcolor = color
        page.update()
        
    def font_clicked(e):
        font = radio_font.value
        page.theme.font_family = font
        page.update()

    radio_color = ft.RadioGroup(
        on_change=button_clicked,
        content=ft.Column(
            [
                ft.Radio(value="red", label="Red"),
                ft.Radio(value="green", label="Green"),
                ft.Radio(value="blue", label="Blue"),
                ft.Radio(value="indigo", label="Indigo"),
            ]
        ),
    )

    radio_font = ft.RadioGroup(
        on_change=font_clicked,
        content=ft.Column(
            [
                ft.Radio(value="Roboto", label="Roboto"),
                ft.Radio(value="Times New Roman", label="Times New Roman"),
                ft.Radio(value="Courier New", label="Courier New"),
                ft.Radio(value="Verdana", label="Verdana"),
                ft.Radio(value="Georgia", label="Georgia"),
                ft.Radio(value="Comic Sans MS", label="Comic Sans MS"),
                ft.Radio(value="Impact", label="Impact"),
                ft.Radio(value="Lucida Console", label="Lucida Console"),

            ]
        )
    )

    switch = ft.Switch(
        value=True if page.theme_mode == ft.ThemeMode.DARK else False,
        label="Modo oscuro",
        label_position=ft.LabelPosition.RIGHT,
        on_change=change_theme,
        mouse_cursor=ft.MouseCursor.CLICK,
    )

    return ft.View(
        route="/settings",
        drawer=Drawer(page=page),
        scroll=ft.ScrollMode.ADAPTIVE,
        padding=ft.padding.only(left=40, top=20, bottom=20),
        controls=[
            ft.AppBar(
                title=ft.Text("Configuración"),
                center_title=True,
            ),
            ft.Column(

                controls=[
                    ft.Text("Configuración del SCADA", style=ft.TextStyle(
                        size=20, weight=ft.FontWeight.BOLD)),
                    switch,
                    ft.Text("Color del tema", style=ft.TextStyle(   size=16, weight=ft.FontWeight.BOLD)),
                    radio_color,
                    ft.Text("Fuente del tema", style=ft.TextStyle(size=16, weight=ft.FontWeight.BOLD)),
                    radio_font,

                ]
            ),
        ],
    )
