import flet as ft
import base64
import numpy as np
import cv2

num_camera = 2

class Camera(ft.UserControl):

    def __init__(self, cap=cv2.VideoCapture(num_camera)):
        super().__init__()
        self.cap = cap
        self.image = None
        self.image_base64 = None
        self.width = 350
        self.height = 300
    
    def did_mount(self):
        self.update_timer()
    
    def get_cap(self):
        return self.cap
    
    def update_timer(self):
        
        while True:
            ret, frame = self.cap.read()
            self.image = frame
            if ret:
                frame = cv2.resize(frame, (self.width, self.height))                
                _, buffer = cv2.imencode('.jpg', frame)
                self.image_base64 = base64.b64encode(buffer)
                self.img.src_base64 = self.image_base64.decode('utf-8')
                self.update()
            else:
                print("Error al leer la cámara")

            self.update()

    def get_image_from_frame(self):
        return self.image        
        
    def build(self):
        self.img = ft.Image(
            src="assets/white_image.png",
            border_radius=ft.border_radius.all(20)
        )
        return self.img
