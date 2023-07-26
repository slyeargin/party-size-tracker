def init_routes(app):
    @app.get('/')
    def home():
        return "Hello World"