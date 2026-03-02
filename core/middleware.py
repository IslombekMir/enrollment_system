import json
from datetime import datetime
from pathlib import Path

from django.utils.deprecation import MiddlewareMixin


class DebugRequestLoggingMiddleware(MiddlewareMixin):
    """
    Lightweight request/response logger for the AI debug session.

    Writes NDJSON lines to the debug log file so we can understand
    what view is being hit during the logout flow and with which user state.
    """

    LOG_PATH = Path(
        "/Users/imirsalimov/Documents/Coding/WIUT/Distributed Systems and Cloud Computing/CW/enrollment_system/.cursor/debug-e23492.log"
    )

    def process_response(self, request, response):
        """
        Log after the response is generated so we can see both
        routing information and the final status code.
        """

        # region agent log
        try:
            payload = {
                "sessionId": "e23492",
                "runId": "pre-fix-logout-investigation",
                "hypothesisId": "H1-H4",
                "location": "core/middleware.py:DebugRequestLoggingMiddleware.process_response",
                "message": "Request/response snapshot",
                "data": {
                    "path": request.path,
                    "method": request.method,
                    "view_name": getattr(
                        getattr(request, "resolver_match", None), "view_name", None
                    ),
                    "user_authenticated": getattr(
                        getattr(request, "user", None), "is_authenticated", None
                    ),
                    "status_code": getattr(response, "status_code", None),
                },
                "timestamp": int(datetime.utcnow().timestamp() * 1000),
            }

            self.LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
            with self.LOG_PATH.open("a", encoding="utf-8") as f:
                f.write(json.dumps(payload) + "\n")
        except Exception:
            # Never let logging break the request cycle
            pass
        # endregion

        return response

