"""
日志类。通过读取配置文件，定义日志级别、日志文件名、日志格式等。
一般直接把logger import进去
from utils.log import logger
logger.info('test log')
"""
import os
import logging
from logging.handlers import TimedRotatingFileHandler
from config.config import LOG_PATH, configs


class Logger(object):
    def __init__(self, logger_name='framework'):
        self.logger = logging.getLogger(logger_name)
        logging.root.setLevel(logging.NOTSET)
        log_configs = configs['log']
        self.log_file_name = log_configs['file_name'] if log_configs['file_name'] else 'test.log'  # 日志文件
        self.backup_count = log_configs['backup'] if log_configs['backup'] else 5  # 保留的日志数量

        # 日志输出级别
        self.console_output_level = log_configs['console_level'] if log_configs['console_level'] else 'WARNING'
        self.file_output_level = log_configs['file_level'] if log_configs else 'DEBUG'

        # 日志输出格式

        pattern = log_configs['pattern'] if log_configs['pattern'] else '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        self.formatter = logging.Formatter(pattern)

    def get_logger(self):
        """在logger中添加日志句柄并返回，如果logger已有句柄，则直接返回
        我们这里添加两个句柄，一个输出日志到控制台，另一个输出到日志文件。
        两个句柄的日志级别不同，在配置文件中可设置。
        """
        if not self.logger.handlers:  # 避免重复日志
            console_handler = logging.StreamHandler() # 用于控制台打印的handler
            console_handler.setFormatter(self.formatter)
            console_handler.setLevel(self.console_output_level)
            self.logger.addHandler(console_handler)

            # 每天重新创建一个日志文件，最多保留backup_count份
            file_handler = TimedRotatingFileHandler(filename=os.path.join(LOG_PATH, self.log_file_name),
                                                    when='D',
                                                    interval=1,
                                                    backupCount=self.backup_count,
                                                    delay=True,
                                                    encoding='utf-8'
                                                    )
            file_handler.setFormatter(self.formatter)
            file_handler.setLevel(self.file_output_level)
            self.logger.addHandler(file_handler)
        return self.logger

logger = Logger().get_logger()
