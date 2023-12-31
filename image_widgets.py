import customtkinter as ctk
from tkinter import filedialog, Canvas
from settings import *


class ImageImport(ctk.CTkFrame):
    def __init__(self, parent, import_function):
        super().__init__(master=parent)
        self.grid(column=0, columnspan=2, row=0, sticky="nsew", padx=10, pady=10)
        self.import_function = import_function

        ctk.CTkButton(self, text="Open Image", command=self.open_dialog).pack(
            expand=True
        )

    def open_dialog(self):
        path = filedialog.askopenfile().name
        self.import_function(path)


class ImageOutput(Canvas):
    def __init__(self, parent, resize_function):
        super().__init__(
            master=parent,
            background=BACKGROUND_COLOR,
            bd=0,
            highlightthickness=0,
            relief="ridge",
        )
        self.grid(row=0, column=1, sticky="nsew")
        self.bind("<Configure>", resize_function)


class CloseOutput(ctk.CTkButton):
    def __init__(self, parent, close_func):
        super().__init__(
            master=parent,
            command=close_func,
            text="x",
            text_color=WHITE,
            fg_color="#3492DF",
            width=40,
            height=40,
            corner_radius=12,
            hover_color=CLOSE_RED,
        )
        self.place(relx=0.99, rely=0.01, anchor="ne")


class ModeSwitch(ctk.CTkButton):
    def __init__(self, parent, mode_func):
        super().__init__(
            master=parent,
            command=mode_func,
            text="Change Theme",
            text_color=WHITE,
            fg_color="#3492DF",
            width=40,
            height=40,
            corner_radius=12,
            hover_color="#66A9E0",
        )
        self.place(relx=0.93, rely=0.01, anchor="ne")
