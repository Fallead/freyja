# -*- coding: utf-8 -*- 
import logging


def skip_illegal_level(start_level, end_level):
    def validate_level(record):

        if start_level in logging._levelNames and \
            end_level in logging._levelNames and \
                start_level <= record.levelno <= end_level:
            return True
        else:
            return False
        
    return validate_level


def get_level(level):
    def validate_level(record):
        if level in logging._levelNames and level == record.levelno:
            return True
        else:
            return False
    return validate_level

