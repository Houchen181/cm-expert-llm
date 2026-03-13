from fastapi import FastAPI

app = FastAPI(title='CM Expert LLM API')


@app.get('/health')
def health():
    return {'ok': True}
