![pypi](https://img.shields.io/pypi/v/coloured-logger.svg)
![python](https://img.shields.io/pypi/pyversions/coloured-logger.svg)
![license](https://img.shields.io/github/license/oscar-defelice/coloured-logger.svg)
![last-commit](https://img.shields.io/github/last-commit/oscar-defelice/coloured-logger/develop)
![docs](https://readthedocs.org/projects/coloured-logger/badge/?version=latest)
[![patreon](https://img.shields.io/badge/Patreon-brown.svg?logo=patreon)](https://www.patreon.com/oscardefelice)
[![follow](https://img.shields.io/twitter/follow/oscardefelice.svg?style=social)](https://twitter.com/OscardeFelice)
[![linkedin](https://img.shields.io/badge/LinkedIn-0077B5?&logo=linkedin&logoColor=white)](https://linkedin.com/in/oscar-de-felice)

# ColouredLogger

<!-- markdownlint-disable MD033 -->
<div align="center">
    <img src="images/logo.png" width="800px">
</div>
<!-- markdownlint-enable MD033 -->

`coloured-logger` is a Python package that provides a customised logger with coloured output and the ability to set verbosity levels dynamically.

## Installation

You can install My Coloured Logger using pip:

```bash
pip install coloured-logger
```

## Usage

As all the good loggers you simply use it as the standard logger

```python
from coloured_logger import Logger

logger = Logger(__name__) # Or any other name you want

logger.info("This is an informational message.")
logger.debug("This debug message won't be displayed.")
```

Colour scheme is customisable by user using the [ANSI escape codes](https://gist.github.com/fnky/458719343aabd01cfb17a3a4f7296797) for colours.
These are typically defined in terms of foreground and background colours, and each color has an associated numeric code. Here is a common mapping:

### Colour codes

Most terminals support 8 and 16 colours, as well as 256 (8-bit) colours. These colours are set by the user, but have commonly defined meanings.

#### 8-16 Colours

| Colour Name | Foreground Colour Code | Background Colour Code |
| :--------- | :-------------------- | :-------------------- |
| Black      | `30`                  | `40`                  |
| Red        | `31`                  | `41`                  |
| Green      | `32`                  | `42`                  |
| Yellow     | `33`                  | `43`                  |
| Blue       | `34`                  | `44`                  |
| Magenta    | `35`                  | `45`                  |
| Cyan       | `36`                  | `46`                  |
| White      | `37`                  | `47`                  |
| Default    | `39`                  | `49`                  |
| Reset      | `0`                   | `0`                   |

> **Note:** the _Reset_ colour is the reset code that resets _all_ colours and text effects, Use _Default_ colour to reset colours only.

Most terminals, apart from the basic set of 8 colors, also support the "bright" or "bold" colours. These have their own set of codes, mirroring the normal colours, but with an additional `;1` in their codes:

```sh
# Set style to bold, red foreground.
\x1b[1;31mHello
# Set style to dimmed white foreground with red background.
\x1b[2;37;41mWorld
```

### A simplified configuration

The user can simply define a python dictionary in order to change logger colours with a simplified colour scheme.

#### Configure logger colours

In order to configure the logger colours, the user can use the following code

```python
from coloured_logger import Logger

my_custom_colours = {
    "WARNING": 4,  # Yellow background with blue text
    "INFO": 2,     # Green text
    "DEBUG": 6,    # Cyan text
    "CRITICAL": 1, # Red text
    "ERROR": 5     # Magenta text
}

# This can change the logger level
logger_level = "DEBUG"

logger = Logger(__name__, my_custom_colours, logger_level)
```
