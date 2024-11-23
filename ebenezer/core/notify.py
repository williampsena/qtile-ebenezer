"""
notify.py
---------

This module provides functions to send desktop notifications using `notify-send`.

Functions:
    push_notification(title: str, message: str):
        Sends a notification with a title and message.

    push_notification_progress(message: str, progress: int):
        Sends a notification with a message and progress indicator.

    push_notification_no_history(title: str, message: str):
        Sends a notification with a title and message without adding it to the notification history.
"""

from ebenezer.core.command import run_shell_command

TEMPLATE_NOTIFY = 'notify-send -r 999 --urgency=low  "$message"'
TEMPLATE_WITH_TITLE = 'notify-send -r 999 --urgency=low  "$title" "$message"'
TEMPLATE_NO_HISTORY = 'notify-send --urgency=low "$title" "$message"'


def push_notification(title: str, message: str):
    """
    Sends a notification with a title and message.

    Args:
        title (str): The title of the notification.
        message (str): The message of the notification.

    Returns:
        subprocess.CompletedProcess: The completed process after running the command.
    """
    return run_shell_command(TEMPLATE_WITH_TITLE, title=title, message=message)


def push_notification_progress(message: str, progress: int):
    """
    Sends a notification with a message and progress indicator.

    Args:
        message (str): The message of the notification.
        progress (int): The progress value to be displayed.

    Returns:
        subprocess.CompletedProcess: The completed process after running the command.
    """
    return run_shell_command(
        f"{TEMPLATE_NOTIFY} -h int:value:$progress",
        message=message,
        progress=str(progress),
    )


def push_notification_no_history(title: str, message: str):
    """
    Sends a notification with a title and message without adding it to the notification history.

    Args:
        title (str): The title of the notification.
        message (str): The message of the notification.

    Returns:
        subprocess.CompletedProcess: The completed process after running the command.
    """
    return run_shell_command(
        f"{TEMPLATE_NO_HISTORY}",
        title=title,
        message=message,
    )
