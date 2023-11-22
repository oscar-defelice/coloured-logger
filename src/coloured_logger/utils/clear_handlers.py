def clear_handlers(logger):
    """
    Remove all handlers from a logger.
    """
    handlers = getattr(logger, "handlers", [])
    for handler in handlers:
        logger.removeHandler(handler)

    return logger
