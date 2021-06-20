import logging

#logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG,
                    format="%(asctime)s - %(levelname)s - %(message)s")


# 1
logging.debug('Debug!')
logging.info('Info!')
logging.warning('Warning!')  # this will be printed
logging.error('Error!')  # this will be printed
logging.critical('Critical!')  # this will be printed

###
print("###")
###

try:
    a = 0/0
except Exception as e:
    logging.error(e, exc_info=True)
    # exc_info -> error info
