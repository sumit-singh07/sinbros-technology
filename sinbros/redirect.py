from django.shortcuts import redirect


class PHPRedirectMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        if ".php" in request.get_raw_uri():
            return redirect(to="http://www.sinbros.com")

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response