from ttkbootstrap.constants import *
import ttkbootstrap as ttk
from _typeshed import Incomplete
from ebenezer.config.settings import AppSettings as AppSettings
from ebenezer.ui.settings.styles import build_fonts as build_fonts
from typing import NamedTuple

class FormField(NamedTuple):
    label: str
    value: str
    type: str
    on_value_change: callable
    options: list[str] = ...

class WidgetField:
    settings: Incomplete
    fonts: Incomplete
    parent: Incomplete
    label_width: Incomplete
    type: Incomplete
    form_field: Incomplete
    on_value_change: Incomplete
    def __init__(self, settings: AppSettings, parent: ttk.Frame, form_field: FormField, label_width: int) -> None: ...

def build_form(fields: list[FormField], settings: AppSettings, parent: ttk.Frame, label_width: int = 10) -> list[WidgetField]: ...
