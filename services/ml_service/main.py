import random
from fastapi import FastAPI
from api_handler import FastAPIHandler

app = FastAPI()
app.handler = FastAPIHandler()

@app.get('/')
def root_dir():
    return({'Hello': 'world'})

@app.post('/api/prediction')
def make_prediction(flat_id: int, item_features: dict):
    prediction = app.handler.predict(item_features)[0]
    print('prediction', prediction)
    print('prediction', type(prediction))



    return ({
             'price': str(prediction),
             'flat_id': flat_id
            })