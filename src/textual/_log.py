from enum import Enum, auto


class LogGroup(Enum):
    UNDEFINED = 0
    EVENT = auto()
    DEBUG = auto()
    INFO = auto()
    WARNING = auto()
    ERROR = auto()
    PRINT = auto()


class LogVerbosity(Enum):
    NORMAL = 0
    HIGH = 1


class LogSeverity(Enum):
    NORMAL = 0
    CRITICAL = 1
