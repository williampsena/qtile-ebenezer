from typing import NamedTuple

import ttkbootstrap as ttk
from ttkbootstrap.constants import *

from ebenezer.config.settings import AppSettings
from ebenezer.ui.settings.styles import build_fonts


class FormField(NamedTuple):
    label: str
    value: str
    type: str
    on_value_change: callable
    options: list[str] = []


class WidgetField:
    def __init__(
        self,
        settings: AppSettings,
        parent: ttk.Frame,
        form_field: FormField,
        label_width: int,
    ):
        self.settings = settings
        self.fonts = build_fonts(self.settings)
        self.parent = parent
        self.label_width = label_width
        self.type = form_field.type
        self.form_field = form_field
        self.on_value_change = form_field.on_value_change

        self._build_component()

    def _build_component(self):

        self.container = ttk.Frame(self.parent)
        self.container.pack(fill=X, expand=YES, pady=5)

        self.label = ttk.Label(
            master=self.container,
            text=self.form_field.label,
            width=self.label_width,
            font=self.fonts.bold_small,
        )

        self.label.pack(side=LEFT, padx=5)

        self.field_var = ttk.StringVar()

        if self.on_value_change:
            self.field_var.trace_add(
                "write", self._handle_value_change(self.on_value_change)
            )

        if self.type == "list":
            self.field = ttk.Combobox(
                master=self.container,
                values=self.form_field.options,
                textvariable=self.field_var,
                font=self.fonts.small,
                width=300,
                style="Form.TCombobox",
            )

            self.field.set(self.form_field.value)
        else:
            self.field = ttk.Entry(
                master=self.container,
                textvariable=self.field_var,
                font=self.fonts.small,
            )
            self.field.insert(0, self.form_field.value)

        self.field.pack(side=LEFT, padx=5, fill=X, expand=YES)

    def _handle_value_change(self, fn: callable):
        def _inner(*args):
            return fn(args, self.field_var.get())

        return _inner


def build_form(
    fields: list[FormField],
    settings: AppSettings,
    parent: ttk.Frame,
    label_width: int = 10,
) -> list[WidgetField]:
    output: list[FormField] = []

    for field in fields:
        output.append(WidgetField(settings, parent, field, label_width=label_width))

    return output
