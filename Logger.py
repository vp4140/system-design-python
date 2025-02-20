import time
from enum import Enum
from threading import Lock, Thread


# Log Levels
class LogLevel(Enum):
    DEBUG = 1
    INFO = 2
    WARNING = 3
    ERROR = 4
    FATAL = 5


# Log Message Class
class LogMessage:
    def __init__(self, message, log_level):
        self.time_stamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())  # Better timestamp format
        self.message = message
        self.log_level = log_level

    def __str__(self):
        return f"{self.time_stamp} [{self.log_level.name}] {self.message}"


# LogAppender Interface
class LogAppender:
    def append(self, log_message):
        raise NotImplementedError


# Console Appender
class ConsoleAppender(LogAppender):
    def append(self, log_message):
        print(str(log_message))


# Logger Configuration
class LogConfig:
    def __init__(self, level=LogLevel.DEBUG, appenders=None):
        self.level = level
        self.appenders = appenders if appenders else [ConsoleAppender()]


# Logger Singleton Class
class Logger:
    _instance = None
    _lock = Lock()

    def __new__(cls):
        if not cls._instance:
            with cls._lock:
                if not cls._instance:
                    cls._instance = super(Logger, cls).__new__(cls)
                    cls._instance.config = LogConfig()  # Default Config
        return cls._instance

    def set_config(self, config):
        self.config = config

    def log(self, level, message):
        if level.value >= self.config.level.value:
            log_message = LogMessage(message, level)
            for appender in self.config.appenders:
                appender.append(log_message)

    # Convenience Methods
    def debug(self, message):
        self.log(LogLevel.DEBUG, message)

    def info(self, message):
        self.log(LogLevel.INFO, message)

    def warning(self, message):
        self.log(LogLevel.WARNING, message)

    def error(self, message):
        self.log(LogLevel.ERROR, message)

    def fatal(self, message):
        self.log(LogLevel.FATAL, message)


# Logging Example
class LoggingExample:
    @staticmethod
    def demonstrate():
        logger = Logger()

        # Default Console Logging
        logger.debug("This is a DEBUG message")
        logger.info("This is an INFO message")

        # Changing Configuration to only show WARNING and above
        config = LogConfig(level=LogLevel.WARNING)
        logger.set_config(config)

        logger.warning("This is a WARNING message")
        logger.error("This is an ERROR message")

        # Logging from Multiple Threads
        def log_from_thread(id):
            logger.info(f"Thread {id} logging INFO")

        threads = [Thread(target=log_from_thread, args=(i,)) for i in range(3)]
        for t in threads:
            t.start()
        for t in threads:
            t.join()


# Run Example
if __name__ == "__main__":
    LoggingExample.demonstrate()
