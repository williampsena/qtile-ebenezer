from libqtile import widget
from libqtile.config import Key
from libqtile.lazy import lazy

from ebenezer.config.settings import AppSettings
from ebenezer.core.command import run_shell_command, run_shell_command_stdout
from ebenezer.core.notify import push_notification, push_notification_progress
from ebenezer.widgets.helpers.args import build_widget_args


def build_volume_widget(settings: AppSettings, kwargs: dict):
    """
    Build a volume widget with the given settings and additional arguments.

    Args:
        settings (AppSettings): The application settings containing fonts, colors, and commands.
        kwargs (dict): Additional arguments to customize the widget.

    Returns:
        widget.Volume: A configured volume widget instance.
    """
    default_args = {
        "font": settings.fonts.font_icon,
        "fontsize": settings.fonts.font_icon_size,
        "foreground": settings.colors.fg_normal,
        "background": settings.colors.bg_topbar_arrow,
        "padding": 5,
        "emoji": True,
        "emoji_list": ["󰝟", "󰕿", "󰖀", "󰕾"],
        "limit_max_volume": True,
        "step": 5,
        "mouse_callbacks": {"Button1": lazy.spawn(settings.commands.get("mixer"))},
    }

    args = build_widget_args(settings, default_args, kwargs)

    return widget.Volume(**args)


def _get_current_volume(settings: AppSettings):
    volume_level = settings.commands.get("volume_level")

    if volume_level is None:
        return None

    output = run_shell_command_stdout(volume_level)

    return output.stdout.replace("%", "").replace("\n", "")


def _is_muted(settings: AppSettings):
    cmd = settings.commands.get("mute_status")

    if cmd is None:
        return False

    output = run_shell_command_stdout(cmd)

    return output.stdout.strip() == "yes"


def _push_volume_notification(settings: AppSettings, message: str):
    level = _get_current_volume(settings) or "0"
    message = f"{message} {level}%"
    push_notification_progress(message=message, progress=int(level))


def _volume_up(settings: AppSettings):
    volume_cmd = settings.commands.get("volume_up")

    @lazy.function
    def inner(qtile):
        _do_volume_up(volume_cmd, settings)

    return inner


def _do_volume_up(volume_cmd: str | None, settings: AppSettings):
    level = int(_get_current_volume(settings) or "0")

    if level > 115:
        return

    _unmute(settings)

    if volume_cmd:
        run_shell_command(volume_cmd)

    _push_volume_notification(settings, "󰝝 Volume")


def _volume_down(settings: AppSettings):
    volume_cmd = settings.commands.get("volume_down")

    @lazy.function
    def inner(qtile):
        _do_volume_down(volume_cmd, settings)

    return inner


def _do_volume_down(volume_cmd: str, settings: AppSettings):
    if volume_cmd:
        run_shell_command(volume_cmd)

    _push_volume_notification(settings, "󰝞 Volume")


def _lazy_unmute(settings: AppSettings):
    @lazy.function
    def inner(qtile):
        _unmute(settings, notify=True)

    return inner


def _unmute(settings: AppSettings, notify=False):
    volume_cmd = settings.commands.get("mute_off")

    if volume_cmd:
        run_shell_command(volume_cmd)

    if notify:
        push_notification("Volume 󰖁", "Muted")


def _lazy_mute_toggle(settings: AppSettings):
    @lazy.function
    def inner(qtile):
        _mute_toggle(settings)

    return inner


def _mute_toggle(settings: AppSettings):
    volume_cmd = settings.commands.get("mute")

    if volume_cmd:
        run_shell_command(volume_cmd)

    if _is_muted(settings):
        push_notification("Volume ", "Muted")
    else:
        push_notification("Volume  󰕾", "On")


def setup_volume_keys(settings: AppSettings):
    """
    Sets up key bindings for volume and media control.

    Args:
        settings (AppSettings): The application settings object.

    Returns:
        list: A list of Key objects for volume and media control.

    Key Bindings:
        - XF86AudioRaiseVolume: Increase the volume.
        - XF86AudioLowerVolume: Decrease the volume.
        - XF86AudioMute: Toggle mute.
        - XF86AudioMicMute: Toggle mute for the microphone.
        - XF86AudioPlay: Play or pause the media player.
        - XF86AudioNext: Skip to the next song.
        - XF86AudioPrev: Go back to the previous song.
    """
    return [
        Key(
            [],
            "XF86AudioRaiseVolume",
            _volume_up(settings),
            desc="Up the volume",
        ),
        Key(
            [],
            "XF86AudioLowerVolume",
            _volume_down(settings),
            desc="Down the volume",
        ),
        Key(
            [],
            "XF86AudioMute",
            _lazy_mute_toggle(settings),
            desc="Toggle mute",
        ),
        Key(
            [],
            "XF86AudioMicMute",
            _lazy_unmute(settings),
            desc="Toggle mute the microphone",
        ),
        Key([], "XF86AudioPlay", lazy.spawn("playerctl play-pause"), desc="Play-pause"),
        Key([], "XF86AudioNext", lazy.spawn("playerctl next"), desc="Next song"),
        Key(
            [], "XF86AudioPrev", lazy.spawn("playerctl previous"), desc="Previous song"
        ),
    ]
