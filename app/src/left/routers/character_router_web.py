from flask import Request


def create_character_router_web(app, dependencies):
    def __init__(self):
        self.create_character = dependencies.create_character

    @app.route("/character", methods=["POST"])
    def create_character():
        print(Request.get_data)
        return {"create": "OK"}
