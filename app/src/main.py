from core.domain.interfaces.ICharacterRepository import ICharacterRepository
from flask import Flask
from left.routers.main_router import create_main_router

app = Flask(__name__)
dependencies = {"create_character": [ICharacterRepository]}
create_main_router(app, dependencies)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8000)
