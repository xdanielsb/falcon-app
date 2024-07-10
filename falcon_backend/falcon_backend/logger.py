import json_log_formatter
import logging
import logstash

from django.utils.timezone import now

logger = logging.getLogger("Backend logger")
logger.setLevel(logging.DEBUG)
logger.addHandler(logstash.TCPLogstashHandler("0.0.0.0", 5959, version=1))
logger.addHandler(logstash.TCPLogstashHandler("logstash", 5959, version=1))


def get_logger() -> logging.Logger:
    return logger


class CustomisedJSONFormatter(json_log_formatter.JSONFormatter):
    def json_record(self, message: str, extra: dict, record: logging.LogRecord):
        extra["name"] = record.name
        extra["filename"] = record.filename
        extra["funcName"] = record.funcName
        extra["msecs"] = record.msecs
        if record.exc_info:
            extra["exc_info"] = self.formatException(record.exc_info)

        return {
            "message": message,
            "timestamp": now(),
            "level": record.levelname,
            "context": extra,
        }
