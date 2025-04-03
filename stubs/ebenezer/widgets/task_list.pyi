from libqtile import widget

from ebenezer.config.settings import AppSettings as AppSettings

class FontIconTaskList(widget.TaskList):
    markup: bool
    def get_taskname(self, window): ...

def build_task_list_widget(settings: AppSettings, kwargs: dict): ...
