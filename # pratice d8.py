# pratice d8


# 1

# import logging

# logging.basicConfig(
#     level=logging.INFO,
#     format ="%(asctime)s %(levelname)s %(message)s",
# )

# logging.debug("debug message")
# logging.info("info message")
# logging.warning("warning message")
# logging.error("error message")



# 2

import logging

logging.basicConfig(
    filename="run.log",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
)


logging.info("pipeline started")
logging.warning("1 row rejected")
logging.error("something failed")