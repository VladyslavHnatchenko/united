import logging


"""Logging from multiple modules(as well as formatting)"""
import other_mod2


def main():
    """The main entry point of the application"""

    logger = logging.getLogger("exampleApp")
    logger.setLevel(logging.INFO)

    # create the logging file handler
    fh = logging.FileHandler("new_snake.log")

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)

    # add handler to logger object
    logger.addHandler(fh)

    logger.info("Program started")
    result = other_mod2.add(7, 8)
    logger.info("Done!")


if __name__ == "__main__":
    main()

# import other_mod
#
#
# def main():
#     """The main entry point of the application"""
#
#     logging.basicConfig(filename="mySnake.log", level=logging.INFO)
#     logging.info("Program started")
#     result = other_mod.add(7, 8)
#     logging.info("Done!")
#
#
# if __name__ == "__main__":
#     main()

"""Create sample logger"""
# logging.basicConfig(filename="sample.log", level=logging.INFO)
# log = logging.getLogger("ex")
#
# try:
#     raise RuntimeError
# except RuntimeError:
#     log.exception("Error!")

# logging.basicConfig(filename="sample.log", level=logging.INFO)
# logging.debug("This's a debug message")
# logging.info("Informational message")
# logging.error("An error has happened!")
