"""Module to collect all tests for the logger module."""

import pytest
from src.coloured_logger.logger import ColouredLogger, ColouredFormatter, formatter_message
import logging


def test_formatter_message_with_color():
    formatted_message = formatter_message("$BOLDHello$RESET", use_color=True)
    assert formatted_message == "\033[1mHello\033[0m"

def test_formatter_message_without_color():
    formatted_message = formatter_message("$BOLDHello$RESET", use_color=False)
    assert formatted_message == "Hello"

def test_coloured_logger_creation(caplog):
    caplog.set_level(logging.INFO)
    logger = ColouredLogger("test_logger")

    # Ensure the logger has a stream handler
    assert any(isinstance(handler, logging.StreamHandler) for handler in logger.handlers)

    # Ensure the formatter is a ColouredFormatter instance
    formatter = logger.handlers[0].formatter
    assert isinstance(formatter, ColouredFormatter)

def test_coloured_formatter_format():
    record = logging.LogRecord('test_logger', logging.INFO, '/path/to/source.py', 42, 'Test message', (), None, 'format')
    formatter = ColouredFormatter(ColouredLogger.FORMAT, use_color=True)

    # Ensure the log message is formatted with colours
    formatted_message = formatter.format(record)
    
    expected_message = (
        "\033[1m[test_logger             ]\033[0m[\033[1;32mINFO             \033[0m]  Test message (\033[1m/path/to/source.py\033[0m:42)"
    )
    assert formatted_message[55:67] == expected_message[66:78]
    assert formatted_message.split("[")[3] == expected_message.split("[")[5].replace(" ", "")
