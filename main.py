from tkinter import Tk, Button, Label, Frame
from vinos import DO_VINOS
from tkintermapview import TkinterMapView
from PIL.ImageTk import PhotoImage
from PIL import Image


class Vinos(Tk):
    def __init__(self):
        super().__init__()
        label = Label(self, text="Vinos Ibericos")
        label.pack()
        self.left_container = Frame(self, width=100, height=1200, relief="raised", borderwidth=1)
        self.left_container.pack(side="left")
        self._display_vinos_buttons()
        self.geometry("1200x1200")
        self.title("Vinos Ibericos")
        self.map = self._display_map_widget()

    def _display_vinos_buttons(self):
        for k, v in DO_VINOS.items():
            button = Button(self.left_container, text=k,
                            command=lambda x=v[0][0], y=v[0][1], color=v[1]: self._display_marker(x, y, color))
            button.pack()

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
window.mainloop()
