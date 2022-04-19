from transformers import Trainer
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import pandas as pd
from datasets import Dataset
import numpy as np
from typing import List
from xlm_emo.dataset import prepare_dataset

class EmotionClassifier:

        def __init__(self, model="t"):
            if model == "t":
                self.tokenizer = AutoTokenizer.from_pretrained("MilaNLProc/xlm-emo-t")
                self.model = AutoModelForSequenceClassification.from_pretrained("MilaNLProc/xlm-emo-t")
            else:
                raise Exception("Not Yet Implemented")

        def predict(self, text: List):

            df = pd.DataFrame({"texts": text})

            train_dataset = Dataset.from_pandas(df)
            train_dataset = prepare_dataset(train_dataset, self.tokenizer)

            trainer = Trainer(model=self.model)

            local_results = np.argmax(trainer.predict(train_dataset)[0], axis=1)

            mapper = {0: "anger", 1: "fear", 2: "joy", 3: "sadness"}

            return [mapper[k] for k in local_results]
