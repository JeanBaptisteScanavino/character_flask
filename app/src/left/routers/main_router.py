from .character_router_web import create_character_router_web


def create_main_router(app, dependencies):
    create_character_router_web(app, dependencies)

    @app.route("/")
    def hello_world():
        return "<p>Hello, World test</p>"
