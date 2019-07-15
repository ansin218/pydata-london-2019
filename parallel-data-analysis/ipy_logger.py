import logging

def create_logger(process_name):
    LOG_FMT = '%(asctime)s %(name)-12s %(levelname)-8s %(message)s'
    
    logger = logging.getLogger(process_name)
    
    fh = logging.FileHandler(f'log/{process_name}.log')
    fh.setLevel(logging.DEBUG)

    formatter = logging.Formatter(LOG_FMT)
    fh.setFormatter(formatter)

    logger.addHandler(fh)
    logger.setLevel(logging.DEBUG)
    
    return logger
