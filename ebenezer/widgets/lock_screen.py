import random
import re
import subprocess
from pathlib import Path
from string import Template
from typing import Callable, List

import requests
from libqtile import widget
from libqtile.log_utils import logger
from PIL import Image, ImageDraw, ImageFont

from ebenezer.config.settings import AppSettings
from ebenezer.core.notify import push_notification_no_history
from ebenezer.core.requests import request_retry

OUTPUT_FILE = "/tmp/i3lock.png"
QUOTE_OUTPUT_FILE = "/tmp/quote.png"


def _is_i3lock_running():
    try:
        subprocess.check_output(["pgrep", "i3lock"])
        return True
    except subprocess.CalledProcessError:
        return False


def _remove_emojis(text):
    emoji_pattern = re.compile(
        "["  # Start of character class
        "\U0001F600-\U0001F64F"  # emoticons
        "\U0001F300-\U0001F5FF"  # symbols & pictographs
        "\U0001F680-\U0001F6FF"  # transport & map symbols
        "\U0001F700-\U0001F77F"  # alchemical symbols
        "\U0001F780-\U0001F7FF"  # Geometric Shapes Extended
        "\U0001F800-\U0001F8FF"  # Supplemental Arrows-C
        "\U0001F900-\U0001F9FF"  # Supplemental Symbols and Pictographs
        "\U0001FA00-\U0001FA6F"  # Chess Symbols
        "\U00002700-\U000027BF"  # Dingbats
        "\u2600-\u26FF"  # Misc symbols
        "\u2700-\u27BF"  # Dingbats
        "\u2B50"  # Star
        "]+",
        flags=re.UNICODE,
    )

    return emoji_pattern.sub(r"", text)


def _get_joke_from_icanhazdadjoke(settings: AppSettings) -> Callable[[], str]:
    def do_request():
        headers = {"Accept": "application/json"}
        return requests.get(settings.lock_screen.icanhazdad_joke_url, headers=headers)

    def inner():
        response = request_retry(do_request)

        if response.status_code == requests.codes.ok:
            return _remove_emojis(response.json()["joke"])
        else:
            return "Something went wrong: {}".format(response.status_code)

    return inner


def _get_joke_from_reddit(settings: AppSettings) -> Callable[[], str]:
    def do_request():
        headers = {"Accept": "application/json"}
        return requests.get(
            settings.lock_screen.reddit_joke_url, headers=headers
        ).json()

    def inner():
        data = request_retry(do_request)

        jokes = data.get("data").get("children") or []
        joke = random.choice(jokes)
        data = joke.get("data")

        punchline = re.sub("&amp;#x200B;", "", _remove_emojis(data.get("selftext")))

        return f"{_remove_emojis(data.get("title"))}\n{punchline}"

    return inner


def _load_joke_providers(settings: AppSettings):
    return {
        "reddit": _get_joke_from_reddit(settings),
        "icanhazdad": _get_joke_from_icanhazdadjoke(settings),
    }


def _get_joke(settings: AppSettings) -> str:
    joke_providers = _load_joke_providers(settings)
    joke_providers_selected = [
        key for key in settings.lock_screen.joke_providers if key in joke_providers
    ]
    random.shuffle(joke_providers_selected)

    for joke_provider_key in joke_providers_selected:
        try:
            return joke_providers[joke_provider_key]()
        except Exception as e:
            # logger.warning(
            #     f"error while trying to fetch jokes from {joke_provider_key}",
            #     e,
            #     exc_info=True,
            # )
            next

    return "No jokes!"


def _remove_output_files():
    for raw_filepath in [OUTPUT_FILE, QUOTE_OUTPUT_FILE]:
        file_path = Path(raw_filepath)

        if file_path.exists():
            file_path.unlink()


def _build_joke_image(settings: AppSettings, joke: str, width: int, height: int):
    img = Image.new(
        "RGB", (width, height), color=settings.colors.lock_screen_quote_foreground_color
    )
    draw = ImageDraw.Draw(img)

    font = ImageFont.truetype(
        settings.lock_screen.quote_font_path, settings.lock_screen.quote_font_size
    )

    bbox = draw.textbbox((0, 0), joke, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]

    position = ((width - text_width) // 2, ((height - text_height) // 2) * 0.2)

    draw.text(
        position,
        joke,
        font=font,
        fill=settings.colors.lock_screen_quote_text_color,
    )

    img.save(QUOTE_OUTPUT_FILE)


def _build_background(settings: AppSettings, output_file: str):
    background = Image.open(output_file)
    width, height = background.size

    joke = _get_joke(settings)
    _build_joke_image(settings, joke=joke, width=width, height=height)

    overlay = Image.open(QUOTE_OUTPUT_FILE)

    background = background.convert("RGBA")
    overlay = overlay.convert("RGBA")

    new_img = Image.blend(background, overlay, 0.5)
    new_img.save(OUTPUT_FILE, "PNG")


def _run_command(commands: List[List[str]]):
    for cmd in commands:
        command = subprocess.Popen(cmd)
        command.wait()


def _prepare_lock_screen(settings: AppSettings):
    _remove_output_files()

    _run_command(
        [
            ["scrot", OUTPUT_FILE],
            [
                "magick",
                "convert",
                "-blur",
                settings.lock_screen.blurtype,
                OUTPUT_FILE,
                OUTPUT_FILE,
            ],
        ]
    )

    _build_background(settings, OUTPUT_FILE)


def lock_screen(settings: AppSettings):
    if _is_i3lock_running():
        logger.warning("i3lock already running")
        return

    push_notification_no_history("󰌾 Locking screen in seconds...", "")
    _prepare_lock_screen(settings)
    run_i3_lock(settings)


def run_i3_lock(settings: AppSettings):
    """
    Executes the i3lock command with the specified settings.
    This function constructs a command to run i3lock with various options
    based on the provided settings. It customizes the lock screen appearance
    including fonts, colors, and sizes.
    Args:
        settings (AppSettings): An instance of AppSettings containing the
                                configuration for the lock screen.
    Raises:
        KeyError: If any required setting is missing from the settings object.
        subprocess.CalledProcessError: If the i3lock command fails to execute.
    Example:
        settings = AppSettings(
            lock_screen=LockScreenSettings(
                font="Arial",
                font_size=24,
                blurtype="5x5"
            ),
            colors=ColorSettings(
                lock_screen_blank_color="000000",
                lock_screen_clear_color="ffffff",
                lock_screen_default_color="888888",
                lock_screen_key_color="ff0000",
                lock_screen_text_color="00ff00",
                lock_screen_wrong_color="ff0000",
                lock_screen_verifying_color="0000ff"
        run_i3_lock(settings)
    """
    cmd_template = Template(
        """
    i3lock
    --nofork
    -i
    $image
    --time-font=$font
    --date-font=$font
    --verif-font=$font
    --wrong-font=$font
    --wrong-font=$font
    --time-size=$font_size
    --date-size=$font_size_medium
    --verif-size=$font_size_medium
    --wrong-size=$font_size_medium
    --wrong-size=$font_size_medium
    --radius=150
    --ring-width=10
    --insidever-color=$clear
    --ringver-color=$verifying
    --insidewrong-color=$wrong
    --ringwrong-color=$default
    --inside-color=$clear
    --ring-color=$default
    --line-color=$blank
    --separator-color=$default
    --verif-color=$text
    --wrong-color=$text
    --time-color=$text
    --date-color=$text
    --layout-color=$text
    --keyhl-color=$key
    --bshl-color=$wrong
    --indicator
    --clock
    --time-str=%H:%M
    """
    )

    cmd_options = cmd_template.substitute(
        image=OUTPUT_FILE,
        font=settings.lock_screen.font,
        font_size=settings.lock_screen.font_size,
        font_size_medium=int(settings.lock_screen.font_size / 1.8),
        blurtype=settings.lock_screen.blurtype,
        blank=settings.colors.lock_screen_blank_color,
        clear=settings.colors.lock_screen_clear_color,
        default=settings.colors.lock_screen_default_color,
        key=settings.colors.lock_screen_key_color,
        text=settings.colors.lock_screen_text_color,
        wrong=settings.colors.lock_screen_wrong_color,
        verifying=settings.colors.lock_screen_verifying_color,
    ).strip()

    cmd_options = re.sub(r"\s+", " ", cmd_options)

    _run_command([cmd_options.split(" ")])


def _click_lock_screen(settings: AppSettings):
    def inner():
        try:
            lock_screen(settings)
        except Exception as e:
            logger.warning(
                "error while trying to run lock screen widget", e, exc_info=True
            )

    return inner


def build_lock_screen_widget(settings: AppSettings):
    """
    Build a lock screen widget for the Qtile window manager.

    Args:
        settings (AppSettings): The application settings containing fonts and colors.

    Returns:
        widget.TextBox: A TextBox widget configured for the lock screen.
    """
    return widget.TextBox(
        " ",
        font=settings.fonts.font_icon,
        fontsize=settings.fonts.font_icon_size,
        padding=2,
        foreground=settings.colors.fg_normal,
        mouse_callbacks={"Button1": _click_lock_screen(settings)},
    )
