from .logger import get_logger


def LoggingMiddleware(get_response):
    def middleware(request):
        get_logger().info(f"Request: {request}")
        response = get_response(request)
        return response

    return middleware
