from app import create_app
from config import *

if __name__ == "__main__":
    app = create_app(DevelopmentConf)
    app.run()