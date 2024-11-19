import logging
import pandas as pd
import pickle as pkl

logger = logging.getLogger("uvicorn.error")
class FastAPIHandler():

    def __init__(self):
        logger.warning('Loading model...')
        try:
            self.model = pkl.load(open('../models/model.pkl', 'rb'))
            logger.info('Model is loaded')
        except Exception as e:
            logger.error('Error loading model')

    def predict(self, item_features:dict):
        item_df = pd.DataFrame(data=item_features, index=[0])
        print(item_df)
        prediction = self.model.predict(item_df)
        print(prediction)
        return (prediction)