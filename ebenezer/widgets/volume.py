from libqtile import widget
from libqtile.config import Key
from libqtile.lazy import lazy

import ebenezer.commands.volume as volume_cmd
from ebenezer.config.settings import AppSettings
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


def _get_current_volume() -> int:
    output = volume_cmd.get_volume_level()

    return int(output.replace("%", "").replace("\n", "") or "0")


def _is_muted() -> bool:
    output = volume_cmd.volume_mute_status().strip()

    return output == "yes"


def _push_volume_notification(message: str):
    level = _get_current_volume()
    message = f"{message} {level}%"
    push_notification_progress(message=message, progress=level)


def _volume_up():
    @lazy.function
    def _inner(_):
        _do_volume_up()

    return _inner


def _do_volume_up():
    level = _get_current_volume()

    if level > 115:
        return

    _unmute()

    volume_cmd.volume_up()

    _push_volume_notification("󰝝 Volume")


def _volume_down():
    @lazy.function
    def _inner(_):
        _do_volume_down()

    return _inner


def _do_volume_down():
    volume_cmd.volume_down()

    _push_volume_notification("󰝞 Volume")


def _lazy_unmute():
    @lazy.function
    def _inner(qtile):
        _unmute(notify=True)

    return _inner


def _unmute(notify=False):
    volume_cmd.volume_mute_off()

    if notify:
        push_notification("Volume 󰖁", "Muted")


def _lazy_mute_toggle():
    @lazy.function
    def _inner(_):
        _mute_toggle()

    return _inner


def _mute_toggle():
    volume_cmd.volume_mute_toggle()

    if _is_muted():
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
            _volume_up(),
            desc="Up the volume",
        ),
        Key(
            [],
            "XF86AudioLowerVolume",
            _volume_down(),
            desc="Down the volume",
        ),
        Key(
            [],
            "XF86AudioMute",
            _lazy_mute_toggle(),
            desc="Toggle mute",
        ),
        # Key(
        #     [],
        #     "XF86AudioMicMute",
        #     _lazy_unmute(),
        #     desc="Toggle mute the microphone",
        # ),
        Key([], "XF86AudioPlay", lazy.spawn("playerctl play-pause"), desc="Play-pause"),
        Key([], "XF86AudioNext", lazy.spawn("playerctl next"), desc="Next song"),
        Key(
            [], "XF86AudioPrev", lazy.spawn("playerctl previous"), desc="Previous song"
        ),
    ]
