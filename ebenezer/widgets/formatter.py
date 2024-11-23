def burn_text(text, position="left") -> str:
    """
    Adds a fire emoji to the given text.

    Parameters:
    text (str): The text to which the fire emoji will be added.
    position (str, optional): The position where the fire emoji will be added.
                              It can be either "left" or "right". Defaults to "left".

    Returns:
    str: The text with the fire emoji added at the specified position.
    """
    if position == "left":
        return f"🔥 {text}"

    return f"{text} 🔥"
