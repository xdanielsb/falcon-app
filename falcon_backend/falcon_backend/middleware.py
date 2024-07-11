from .logger import get_logger


def LoggingMiddleware(get_response):
    """Logs info about incoming requests using Django logger."""

    def middleware(request):
        # if monitoring is enabled, log the request to logstash -> elasticsearch
        get_logger().info(f"Request: {request}")
        response = get_response(request)
        return response

    return middleware
