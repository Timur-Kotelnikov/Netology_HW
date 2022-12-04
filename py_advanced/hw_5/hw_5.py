import time
import logging
import logging.handlers

nested_list = [['a', 'b', 'c'], ['d', 'e', 'f', 'h', False], [1, 2, None]]


def outer_decorator(path):
    full_path = path + 'logs.txt'

    def inner_decorator(function_to_decorate):
        logger = logging.getLogger(name='timur.main')
        logger.setLevel('DEBUG')

        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(level='DEBUG')

        file_handler = logging.handlers.RotatingFileHandler(filename=full_path, maxBytes=1000000, backupCount=1000)
        file_handler.setLevel(level='DEBUG')

        logger.addHandler(hdlr=stream_handler)
        logger.addHandler(hdlr=file_handler)

        def inner(*args, **kwargs):
            function_to_decorate(*args, **kwargs)
            logger.debug(msg=f'Message level is {logging.getLevelName(logger.level)}. Time = {time.asctime()}, function name = {function_to_decorate.__name__}, arguments = {args, kwargs}, value = {function_to_decorate(*args, **kwargs)}')
            return function_to_decorate(*args, **kwargs)
        return inner
    return inner_decorator


@outer_decorator('')
def make_list_flat(some_list):
    return list(sub_sub for sub in some_list for sub_sub in sub)


print(make_list_flat(nested_list))
