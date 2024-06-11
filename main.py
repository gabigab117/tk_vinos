from customtkinter import CTk, CTkButton, CTkLabel, CTkFrame
from vinos import DO_VINOS
from tkintermapview import TkinterMapView
from PIL.ImageTk import PhotoImage
from PIL import Image


class Vinos(CTk):
    def __init__(self):
        super().__init__()
        label = CTkLabel(self, text="Vinos Ibericos")
        label.pack()
        self.left_container = CTkFrame(self, width=100, height=1200, fg_color="white")
        self.left_container.pack(side="left", padx=50)
        self._display_vinos_buttons()
        self.geometry("1200x1200")
        self.title("Vinos Ibericos")
        self.map = self._display_map_widget()

    def _display_vinos_buttons(self):
        red = "#f5a6a8"
        white = "#f0d795"
        for k, v in DO_VINOS.items():
            fg_button_color = white if v[1] == "Blanco" else red
            button = CTkButton(self.left_container, text=k,
                               command=lambda x=v[0][0], y=v[0][1], color=v[1]: self._display_marker(x, y, color),
                               fg_color=fg_button_color, text_color="black", hover_color="yellow")
            button.pack(padx=5, pady=10)

    def _display_map_widget(self):
        map_widget = TkinterMapView(self, width=1100, height=1200, corner_radius=1)
        map_widget.set_position(deg_x=41.4129785, deg_y=-4.9597533)
        map_widget.set_zoom(5)
        map_widget.pack()
        return map_widget

    def _display_marker(self, x, y, color):
        icon = Image.open("blanco.jpg") if color == "Blanco" else Image.open("tinto.jpg")
        photo_image = PhotoImage(image=icon)
        marker = self.map.set_marker(x, y, icon=photo_image)
        return marker


window = Vinos()
window.configure(fg_color="#e6deca")
window.mainloop()
