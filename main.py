from application import create_app
import uvicorn

app = create_app()

@app.get('/')
def index():
    return 'Hello'

# if __name__ == 'main':
#     uvicorn.run(app, host='127.0.0.1', port = 12338)
