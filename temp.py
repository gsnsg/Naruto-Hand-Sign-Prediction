from keras.models import load_model

# model = load_model('best_model_96_test.h5')
# model.summary()


labels_dict = {'bird': 0,
               'boar': 1,
               'dog': 2,
               'dragon': 3,
               'hare': 4,
               'horse': 5,
               'monkey': 6,
               'ox': 7,
               'ram': 8,
               'rat': 9,
               'snake': 10,
               'tiger': 11,
               'zero': 12
               }


rev = {v: k for k, v in labels_dict.items()}
print(rev)
