from aiohttp import web

routes = web.RouteTableDef()

@routes.get("/")
async def home(request):
    return web.Response(text="Premium Bot Running")

async def start_webserver():

    app = web.Application()
    app.add_routes(routes)

    runner = web.AppRunner(app)

    await runner.setup()

    port = 8000

    site = web.TCPSite(
        runner,
        "0.0.0.0",
        port
    )

    await site.start()

    print(f"Web Server Started : {port}")
