import flet as ft

from widgets.drawer import Drawer


def HelpScreen(page: ft.Page):
    style_titles = ft.TextStyle(size=20, weight=ft.FontWeight.BOLD)
    style_subtitle = ft.TextStyle(size=15, weight=ft.FontWeight.BOLD)
    style_normal = ft.TextStyle(size=15)
    return ft.View(
        route="/help",
        drawer=Drawer(page=page),
        scroll=ft.ScrollMode.ADAPTIVE,
        controls=[
            ft.AppBar(
                title=ft.Text("Ayuda"),
                center_title=True,
            ),
            ft.Column(
                controls=[
                    ft.Text("Ayuda y Documentación", style=style_titles),
                    ft.Text(
                        "Bienvenido a la sección de ayuda y documentación de la aplicación de conteo de varillas.", style=style_normal),
                    ft.Divider(height=20),
                    ft.Container(
                        padding=ft.padding.only(left=50, right=50),
                        content=ft.Column(
                            controls=[
                                ft.Text("1. Introducción", style=style_titles),
                                ft.Text("1.1. Descripción del proyecto",
                                        style=style_subtitle),
                                ft.Text(
                                    "Nuestra aplicación de conteo de varillas es una herramienta diseñada para facilitar el proceso de conteo automático de varillas en imágenes utilizando técnicas de visión por computadora. La aplicación emplea la biblioteca OpenCV para el procesamiento y análisis de imágenes, y está construida sobre el framework Flet para ofrecer una interfaz de usuario intuitiva y fácil de usar.", text_align=ft.TextAlign.JUSTIFY, style=style_normal
                                ),
                                ft.Text("1.2. Objetivo", style=style_subtitle),
                                ft.Text(
                                    "El objetivo principal de esta aplicación es proporcionar una solución rápida y precisa para contar varillas en imágenes, eliminando la necesidad de realizar conteos manuales tediosos y propensos a errores. Está dirigida a profesionales y empresas que requieren un método eficiente para contabilizar varillas, ya sea en entornos industriales, de construcción o en cualquier otra aplicación donde se utilicen varillas.", text_align=ft.TextAlign.JUSTIFY, style=style_normal
                                ),
                                ft.Text("2. Requisitos", style=style_titles),
                                ft.Text("2.1. Requisitos del sistema",
                                        style=style_subtitle),
                                ft.Text(
                                    "Para ejecutar la aplicación de conteo de varillas, se requiere un sistema con las siguientes especificaciones mínimas:", text_align=ft.TextAlign.JUSTIFY, style=style_normal

                                ),
                                ft.Text(
                                    "- Procesador: Intel Core i5 o superior"),
                                ft.Text(
                                    "- Espacio en disco: 1 GB de espacio libre"),
                                ft.Text("- Memoria RAM: 4 GB de RAM"),
                                ft.Text(
                                    "- Sistema operativo: Windows 10 o superior"),
                                ft.Text(
                                    "- Cámara web o dispositivo de captura de imágenes"),
                                ft.Text(
                                    "- Conexión a Internet (para la instalación de bibliotecas y dependencias)"),
                                ft.Text("2.2. Requisitos de software",
                                        style=style_subtitle),
                                ft.Text("- Python 3.7 o superior"),
                                ft.Text("Librerías y dependencias:"),
                                ft.Text("- opencv-contrib-python==4.8.1.78"),
                                ft.Text("- numpy==1.26.4"),
                                ft.Text("- flet==0.22.0"),
                                ft.Text("3. Guía de uso", style=style_titles),
                                ft.Text("3.1. Interfaz de usuario",
                                        style=style_subtitle),
                                ft.Text(
                                    "La aplicación de conteo de varillas consta de las siguientes secciones principales:", text_align=ft.TextAlign.JUSTIFY, style=style_normal
                                ),
                                ft.Row(
                                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                    wrap=True,
                                    controls=[
                                        ft.Column(
                                            controls=[
                                                ft.Text("Inicio de sesión"),
                                                ft.Image(
                                                    src="assets/login_screen.png", width=500, height=400, border_radius=20),
                                            ]
                                        ),
                                        ft.Column(
                                            controls=[
                                                ft.Text("Pantalla principal"),
                                                ft.Image(
                                                    src="assets/portada.png", width=500, height=400, border_radius=20),
                                            ]
                                        ),

                                    ]
                                ),
                                ft.Row(
                                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                    wrap=True,
                                    controls=[
                                        ft.Column(
                                            controls=[
                                                ft.Text("Pantalla de Conteo y procesamiento de imágenes"),
                                                ft.Image(
                                                    src="assets/procces.png", width=500, height=400, border_radius=20),
                                            ]
                                        ),
                                        ft.Column(
                                            controls=[
                                                ft.Text("Menú de navegación"),
                                                ft.Image(
                                                    src="assets/menu.png", width=500, height=400, border_radius=20),
                                            ]
                                        ),
                                    ]
                                ),

                                






                            ]
                        ),
                    ),

                ]
            ),
        ],

    )
