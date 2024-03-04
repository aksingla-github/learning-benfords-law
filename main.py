from fastapi import FastAPI

app = FastAPI()

texts = {
    '1': 'Hey, I am text number 1!',
    '2': 'Hi, I am concerned about Global Warming!',
    '3': 'I am concerned about traffic rules and safety!'
}

@app.get("/")
async def root():
    return {'message': 'I have my Get operation running!'}


@app.get("/text/{text_id}")
async def get_text(text_id: str):
    return {'message': texts[text_id]}