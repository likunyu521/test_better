import os

configs = {
    'URL': 'http://www.baidu.com',
    'ip': '127.0.0.1',
    'port': 8080,
    'log': {
        'file_name': 'test.log',
        'backup': 5,
        'console_level': 'WARNING',
        'file_level': 'DEBUG',
        'pattern': '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    }
}

BASE_PATH = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]
a = os.path.dirname(os.path.abspath(__file__))
CONFIG_FILE = os.path.join(BASE_PATH, 'config')
DATA_PATH = os.path.join(BASE_PATH, 'data')
DRIVER_PATH = os.path.join(BASE_PATH, 'drivers')
LOG_PATH = os.path.join(BASE_PATH, 'log')
REPORT_PATH = os.path.join(BASE_PATH, 'report')

# print(DATA_PATH)