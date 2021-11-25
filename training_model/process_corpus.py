from tensorflow import keras
from utils import preprocess_text
from keras.preprocessing.sequence import pad_sequences
import tensorflow as tf
import numpy as np
import pickle

model = keras.models.load_model('cnn_model1')

max_sequence_length = 50

with open('tokenizer.pickle', 'rb') as handle:
    tokenizer = pickle.load(handle)

text = [
    "Partido complicado pero no perdido. Saldremos de esta 💪 Que la fe sea lo ultimo que se pierda 🙌",
    "@manuval68 @Minsa_Peru @Agencia_Andina @noticias_tvperu @RadioNacionalFM @DiarioElPeruano ASI ES!!!!!!!!!!!!!!!!!!!! MALDITAS FUJUIRRAATAAAAAASSSS!!!!!!!!!!!!!!!! #FujimoristasEnemigosDelPeru!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!",
    "@Minsa_Peru @Agencia_Andina @noticias_tvperu @RadioNacionalFM @DiarioElPeruano Cuidence por favor !!!!!!!!! distanciamiento fisico ! ❤️❤️❤️❤️🙏🤍💪 tomen distancia 🥺",
    "@rparrawong @Minsa_Peru Tienen el numero de contagios de hoy y fallecidos por regiones please?? 🙁",
    "Partido complicado pero no perdido. Saldremos de esta 💪 Que la fe sea lo ultimo que se pierda 🙌",
    "El chino es un buen puto, me cae bien",
    "@pcmperu @nlcr5_ @presidenciaperu @PeruPaisDigital @MTC_GobPeru @Minsa_Peru @EsSaludPeru @elcomercio_peru @larepublica_pe @RPPNoticias @canalN_ @exitosape Otra cojudez de este gobierno incompetente"
]

text = [preprocess_text(t) for t in text]
text = tokenizer.texts_to_sequences(text)
text = pad_sequences(text, maxlen = max_sequence_length)

predictions = model.predict(text)
for p in predictions:
    p = [round(num,5) for num in p]
    print(p)