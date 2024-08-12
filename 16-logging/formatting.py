import sys, logging

def get_logging_level() -> str:
    # Access command-line arguments
    args = sys.argv
    print(args)
    return args[1]


def log(level: str) -> None:

    levels = {
        'debug': logging.DEBUG,
        'info': logging.INFO,
        'warning': logging.WARNING,
        'error': logging.ERROR,
        'critical': logging.CRITICAL
    }

    if level not in levels:
        print(f"Invalid logging level: {level}. Defaulting to 'info'.")
        level = 'info'
        
    logging.basicConfig(
        level=levels[level],
        format="%(asctime)s %(levelname)s %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    logging.debug("This is a debug message.")
    logging.info("This is an info message.")
    logging.warning("This is a warning message.")
    logging.error("This is an error message.")
    logging.critical("This is a critical message.")


if __name__ == "__main__":
    level =  get_logging_level()
    log(level)

