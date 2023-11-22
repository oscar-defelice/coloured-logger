"""Module that contains the definition of a customised logger class."""
# TODO: Move this into a separate package

import logging

from src.coloured_logger.logger_config import COLOURS, RESET_SEQ, COLOR_SEQ, BOLD_SEQ


def formatter_message(message, use_color=True):
    if use_color:
        message = message.replace("$RESET", RESET_SEQ).replace("$BOLD", BOLD_SEQ)
    else:
        message = message.replace("$RESET", "").replace("$BOLD", "")
    return message


class ColouredFormatter(logging.Formatter):
    def __init__(self, msg, use_color=True, colours=COLOURS):
        logging.Formatter.__init__(self, msg)
        self.use_color = use_color
        self.colours = colours

    def format(self, record):
        levelname = record.levelname
        if self.use_color and levelname in self.colours:
            levelname_color = (
                COLOR_SEQ % (30 + self.colours[levelname]) + levelname + RESET_SEQ
            )
            record.levelname = levelname_color
        return logging.Formatter.format(self, record)


# Custom logger class with multiple destinations (console, file, etc.)
class ColouredLogger(logging.Logger):
    """ColouredLogger Object to log messages with colours."""

    FORMAT = "[$BOLD%(name)-20s$RESET][%(levelname)-18s]  %(message)s ($BOLD%(filename)s$RESET:%(lineno)d)"

    def __init__(self, name: str, colours: dict = COLOURS):
        logging.Logger.__init__(self, name, logging.DEBUG)

        self.colours = colours
        self.colour_format = formatter_message(message=self.FORMAT, use_color=True)
        colour_formatter = ColouredFormatter(self.colour_format, use_color=True, colours=self.colours)

        console = logging.StreamHandler()
        console.setFormatter(colour_formatter)

        self.addHandler(console)
        return
