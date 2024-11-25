from ebenezer.config.settings import AppSettings as AppSettings
from libqtile import widget

class FontIconTaskList(widget.TaskList):
    markup: bool
    def get_taskname(self, window): ...

def build_task_list_widget(settings: AppSettings, kwargs: dict): ...
