from PIL.ImageTk import PhotoImage
from PIL import Image

from customtkinter import CTk, CTkButton, CTkLabel, CTkFrame  # type: ignore
from tkintermapview import TkinterMapView  # type: ignore

from settings import WIDTH_WINDOW, HEIGHT_WINDOW, START_X, START_Y, RED_BUTTON, WHITE_BUTTON, TITLE, \
    WIDTH_LEFT_CONTAINER, HEIGHT_LEFT_CONTAINER, FG_COLOR_LEFT_CONTAINER
from vinos import DO_VINOS


class Vinos(CTk):
    def __init__(self) -> None:
        super().__init__()
        self._display_window(WIDTH_WINDOW, HEIGHT_WINDOW, TITLE)
        self._display_left_container(WIDTH_LEFT_CONTAINER, HEIGHT_LEFT_CONTAINER, FG_COLOR_LEFT_CONTAINER)
        self._display_vinos_buttons()
        self.map = self._display_map_widget()

    def _display_window(self, width: str, height: str, title: str) -> None:
        self.geometry(f"{width}x{height}")
        self.title(title)
        CTkLabel(self, text=TITLE).pack()

    def _display_left_container(self, width: int, height: int, fg_color: str) -> None:
        self.left_container = CTkFrame(self, width=width, height=height, fg_color=fg_color)
        self.left_container.pack(side="left", padx=50)

    def _display_vinos_buttons(self) -> None:
        for k, v in DO_VINOS.items():
            fg_button_color = WHITE_BUTTON if v[1] == "Blanco" else RED_BUTTON
            CTkButton(self.left_container, text=k, command=lambda data=v: self._display_marker(data),
                      fg_color=fg_button_color, text_color="black", hover_color="yellow").pack(padx=5, pady=10)

    def _display_map_widget(self) -> TkinterMapView:
        map_widget = TkinterMapView(self, width=1100, height=1200, corner_radius=1)
        map_widget.set_position(deg_x=START_X, deg_y=-START_Y)
        map_widget.set_zoom(6)
        map_widget.pack()
        return map_widget

    def _display_marker(self, data: tuple) -> None:
        photo_image = PhotoImage(image=Image.open(f"assets/{data[1]}.png"))
        self.map.set_marker(data[0][0], data[0][1], icon=photo_image)


if __name__ == "__main__":
    window = Vinos()
    window.configure(fg_color="#e6deca")
    window.mainloop()
