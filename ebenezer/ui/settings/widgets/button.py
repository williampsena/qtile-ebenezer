import ttkbootstrap as ttk


def build_button(
    parent_frame: ttk.Frame, text: str, bootstyle: str = None, command: callable = None
) -> ttk.Button:
    button = ttk.Button(
        parent_frame,
        text=text,
        bootstyle=bootstyle or "transparent",
    )

    if command:
        button.configure(command=command)

    return button
