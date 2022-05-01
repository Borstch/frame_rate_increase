LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "default": {
            "()": "uvicorn.logging.DefaultFormatter",
            "fmt": "%(levelname)s \t %(asctime)s - %(name)s - %(message)s",
            "datefmt": "%d/%m/%Y %H:%M:%S",
        }
    },
    "handlers": {
        "default": {
            "formatter": "default",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stderr",
        }
    },
    "loggers": {
        "": {"handlers": ["default"], "level": "DEBUG"},
        "uvicorn.error": {"level": "INFO"},
    },
}

APP_TITLE = "Frame Rate Increaser"
API_DESCR = "REST API for increasing video frame rate"
APP_VERSION = "0.1"

APP_WORKERS = 1
MAX_MESSAGE_LENGTH = 100

DEBUG = True
ACCESS_LOG = False
LOG_LEVEL = "debug"
