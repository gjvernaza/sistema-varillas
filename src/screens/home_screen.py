import flet as ft
import base64
import cv2
import numpy as np
import datetime as dt

from services.camera import Camera
from services.db.database import DB
from widgets.drawer import Drawer

def HomeScreen(page: ft.Page):
    db = DB("./src/services/db/users.db")
    id_img = 0
    count = 0
    load_img = False
    num_varillas_sobrantes = 0

    def get_capture(e):
        
        img = camera_holder.get_image_from_frame()
        _, buffer = cv2.imencode('.jpg', img)
        img_base64 = base64.b64encode(buffer).decode()
        image_holder.content = ft.Image(
            src_base64=img_base64,
            fit=ft.ImageFit.COVER,
        )
        image_holder.bgcolor = None
        image_holder.content.visible = True
        image_holder.update()
        try:
            proccess_and_count(e)
        except Exception as e:
            print(e)
            open_dlg(e)           
            dialog_message.update()
        

    def proccess_and_count(e):
        nonlocal count, id_img, load_img, num_varillas_sobrantes
        num_imgs = len(db.get_images())
        if num_imgs > 0:
            id_img = num_imgs + 1
        else:
            id_img = 1
        count = id_img
        if load_img:
            img = image_holder.content.src_base64
            img = base64.b64decode(img)
            img = cv2.imdecode(np.frombuffer(img, np.uint8), -1)
        else:
            img = camera_holder.get_image_from_frame()
        img = cv2.resize(img, (350, 300))
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        blurred = cv2.GaussianBlur(gray, (7, 7), 0)
        circles = cv2.HoughCircles(blurred, cv2.HOUGH_GRADIENT, 1,
                                   minDist=21, param1=250, param2=6, minRadius=10, maxRadius=12)
        
        if circles is not None:
            circles = circles.round().astype(int)
            for (x, y, r) in circles[0]:
                cv2.circle(img, (x, y), r, (255, 0, 0), 2)
            num_circles = len(circles[0])
            num_varillas = num_circles
            _, buffer = cv2.imencode('.jpg', img)
            img_base64 = base64.b64encode(buffer).decode()
            image_process_holder.content = ft.Image(
                src_base64=img_base64,
                fit=ft.ImageFit.COVER,
            )
            image_process_holder.bgcolor = None
            image_process_holder.content.visible = True
            text_varillas.value = f"Número de varillas: {num_varillas}"
            date, hour = get_date()
            save_image_to_db(base64_str=img_base64,
                             name=f"image_{count}.jpg", count=num_varillas, date=date, hour=hour, e=e)
            if num_varillas>70:
                num_varillas_sobrantes = num_varillas - 70
                page.banner.content.value = f"Puede haber un exceso de {num_varillas_sobrantes} varillas en el lote. Por favor, verifique."
                open_banner(e)
            if num_varillas > 0 and num_varillas < 10:
                bs.open = True
                bs.update()
        else:
            open_dlg(e)
            dialog_message.update()
        

        text_varillas.update()
        image_process_holder.update()

        
    def save_image_to_db(base64_str: str, name: str, count: int, date: str, hour: str, e):
        
        db = DB("./src/services/db/users.db")
        db.insert_image(name=name, base64_str=base64_str, count=count, date=date, hour=hour)
        db.close()
        print("Imagen guardada en la base de datos")        

    def open_banner(e):
        page.banner.open = True
        page.update()

    def close_banner(e):
        page.banner.open = False
        page.update()
    
    
    def open_dlg(e):
        page.dialog = dialog_message
        dialog_message.open = True
        page.update()
    
    def close_dlg(e):
        dialog_message.open = False
        dialog_message.update()
    
    def show_bs(e):
        bs.open = True
        bs.update()

    
    
    
    
    def handle_load_file(e: ft.FilePickerResultEvent):
        nonlocal load_img
        load_img = True       

        if e.files and len(e.files) > 0:
            with open(e.files[0].path, "rb") as f:
                img = f.read()
                img_base64 = base64.b64encode(img).decode()
                image_holder.content = ft.Image(
                    src_base64=img_base64,
                    fit=ft.ImageFit.COVER,
                )
                image_holder.bgcolor = None
                image_holder.content.visible = True
                image_holder.update()
                try:
                    proccess_and_count(e)
                except Exception as e:
                    print(e)
                    open_dlg(e)           
                    dialog_message.update()
        
    def get_date():
        date = dt.datetime.now().strftime("%d-%m-%Y")
        hour = dt.datetime.now().strftime("%H:%M:%S")
        return date, hour



    camera_holder = Camera()

    image_holder = ft.Container(
        height=300,
        width=350,
        bgcolor=ft.colors.PRIMARY,
        border_radius=20,

    )

    image_process_holder = ft.Container(
        height=300,
        width=350,
        bgcolor=ft.colors.PRIMARY,
        border_radius=20,
    )

    text_varillas = ft.Text(
        "Número de varillas: 0",
        style=ft.TextStyle(size=20, weight=ft.FontWeight.BOLD),
    )

    dialog_message = ft.AlertDialog(
        modal=True,
        title=ft.Text("Nro de varillas"),
        content=ft.Text("No se detectaron varillas en la imagen."),
        icon=ft.Icon(ft.icons.WARNING),
        actions=[
            ft.TextButton("Salir", on_click=close_dlg),           
        ],
        actions_alignment=ft.MainAxisAlignment.END,
        
    )

    bs = ft.BottomSheet(
        open=False,
        on_dismiss=lambda _: print("Bottom sheet dismissed!"),
        content=ft.Container(
            ft.Column(
                [
                    ft.Icon(ft.icons.WARNING, size=40, color=ft.colors.AMBER),
                    ft.Text(value="El lote puede que tenga menos de 10 varillas. Por favor, verifique.", style=ft.TextStyle(size=20, weight=ft.FontWeight.BOLD), text_align=ft.TextAlign.CENTER),                    
                ],
                tight=True,
            ),
            padding=10,
        ),        
    )

    file_picker = ft.FilePicker(on_result=handle_load_file)

    page.overlay.append(file_picker)
    page.overlay.append(bs)
    page.banner = ft.Banner(
        
        bgcolor=ft.colors.AMBER_100,
        leading=ft.Icon(ft.icons.WARNING_AMBER_ROUNDED,
                        color=ft.colors.AMBER, size=40),
        content=ft.Text(
            value=None,
            style=ft.TextStyle(size=20, weight=ft.FontWeight.BOLD, color=ft.colors.BLACK),
        ),
        actions=[            
            ft.TextButton("Cancel", on_click=close_banner),
        ],
    )

    return ft.View(
        route="/home",
        drawer=Drawer(page=page),
        scroll=ft.ScrollMode.ADAPTIVE,
        controls=[
            ft.AppBar(
                title=ft.Text("Inicio"),
                center_title=True,                

            ),

            ft.Column(

                horizontal_alignment=ft.CrossAxisAlignment.CENTER,

                controls=[
                    ft.Row(
                        alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                        wrap=True,
                        controls=[
                            camera_holder,
                            image_holder,
                            image_process_holder,

                        ]
                    ),
                    ft.Row(
                        alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                        controls=[
                            ft.ElevatedButton(
                                "Cargar imagen", on_click=lambda _: file_picker.pick_files(allow_multiple=False, allowed_extensions=["jpg", "png", "jpeg"]), icon=ft.icons.IMAGE),
                            ft.ElevatedButton(
                                "Procesar", on_click=get_capture, icon=ft.icons.CAMERA),
                        ]
                    ),
                    #ft.Slider(value=0, min=0, max=100,  width=300, on_change=zoom_image),
                    text_varillas,
                ]
            ),

        ],

    )
