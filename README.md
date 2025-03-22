# Qtile Ebenezer 🪨

This project offers a range of widgets and behaviors, from Desktop to Qtile Tiling Window Manager.


# The name

This theme was named Ebenezer 🪨, which meaning "stone of helper.".

> The quote is from I Samuel 7. After defeating the Philistines, Samuel raises his Ebenezer, declaring that God defeated the enemies on this spot. As a result, "hither by thy help I come." So I hope this stone helps you in your environment and, more importantly, in your life. 🙏🏿

![Ebenezer](images/ebenezer.webp)
**By: DALL·E**


## Installation

### For Arch users

I developed an AUR package to install this package. I have no experience with AUR packages, so if you discover anything wrong, please contact me at issues.

#### Option 1: Using yay

```shell
yay -Syu python-qtile-ebenezer
```

#### Option 2: Using pamac (Manjaro)

```shell
pamac update
pamac install python-qtile-ebenezer
```

### PIP

You can install directly as a typical method using pip.

> However, this is not the greatest method because you risk breaking the OS by installing packages worldwide using Pip.

```shell
pip install qtile-ebenezer
```

### Using

Some tests to run at repl 'python':

```python
from ebenezer.core.files import resolve_file_path
resolve_file_path("$home")
# '/home/your_home'
```


# The Ebenezer CLI

A CLI tool for backlight, wallpaper, volume control and other helpers.

## Usage

```shell
ebenezer backlight --help
ebenezer volume --help
ebenezer wallpaper --help
```

# Documentation

You may access library documentation generated with Sphinx [here](https://qtile-ebenezer.readthedocs.io/en/latest/).

Thank you for the Read The Docs open source support. ❤️

# Inspirations ✨

- [JhoalfercoQtileDotfiles](https://github.com/JhonatanFerrer/JhoalfercoQtileDotfiles) by Jhonatan Ferrer
- [dotfiles](https://gitlab.com/dwt1/dotfiles) by DistroTube
- [shinrai-dotfiles](https://github.com/neo-fetch/shinrai-dotfiles) by neo-fetch
- [rofi](https://github.com/adi1090x/rofi?tab=readme-ov-file) by adi1090x
- [rofi-presets](https://github.com/SapuSeven/rofi-presets) by SapuSeven
- [qtile-multiple-screens](https://sohanglal.github.io/Qtile---make-workspaces-span-across-screens)