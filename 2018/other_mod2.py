import logging


module_logger = logging.getLogger("exampleApp.other_mod2")


def add(x, y):
    """"""
    logger = logging.getLogger("exampleApp.other_mod2.add")
    logger.info("added %s and %s to get %s" % (x, y, x+y))
    return x+y
