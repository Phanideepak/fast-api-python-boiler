from application import create_app
import uvicorn

app = create_app()


@app.get('/health')
def health_check():
    return {'status' : 'health'}

# if __name__ == 'main':
#     uvicorn.run('main:app', host='127.0.0.1', port = 11339, reload= True)
