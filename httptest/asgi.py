from hypercorn.middleware import AsyncioWSGIMiddleware
import httptest.wsgi as wsgi_app

asyncio_app = AsyncioWSGIMiddleware(wsgi_app.application)
