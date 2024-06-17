from customtkinter import CTk, CTkButton, CTkLabel, CTkFrame  # type: ignore
from PIL.ImageTk import PhotoImage
from PIL import Image
from tkintermapview import TkinterMapView  # type: ignore

from settings import WIDTH_WINDOW, HEIGHT_WINDOW, START_X, START_Y
from vinos import DO_VINOS


class Vinos(CTk):
    def __init__(self):
        super().__init__()
        self.geometry(f"{WIDTH_WINDOW}x{HEIGHT_WINDOW}")
        self.title("Vinos Ibericos")
        CTkLabel(self, text="Vinos Ibericos").pack()
        self.left_container = CTkFrame(self, width=100, height=1200, fg_color="white")
        self.left_container.pack(side="left", padx=50)
        self._display_vinos_buttons()
        self.map = self._display_map_widget()

    def _display_vinos_buttons(self):
        red = "#f5a6a8"
        white = "#f0d795"
        for k, v in DO_VINOS.items():
            fg_button_color = white if v[1] == "Blanco" else red
            CTkButton(self.left_container, text=k,
                      command=lambda x=v[0][0], y=v[0][1], color=v[1]: self._display_marker((x, y), color),
                      fg_color=fg_button_color, text_color="black", hover_color="yellow").pack(padx=5, pady=10)

    def _display_map_widget(self):
        map_widget = TkinterMapView(self, width=1100, height=1200, corner_radius=1)
        map_widget.set_position(deg_x=START_X, deg_y=-START_Y)
        map_widget.set_zoom(5)
        map_widget.pack()
        return map_widget

    def _display_marker(self, coord: tuple[float], color: str):
        photo_image = PhotoImage(
            image=Image.open("assets/blanco.png") if color == "Blanco" else Image.open("assets/tinto.png"))
        self.map.set_marker(*coord, icon=photo_image)


if __name__ == "__main__":
    window = Vinos()
    window.configure(fg_color="#e6deca")
    window.mainloop()
