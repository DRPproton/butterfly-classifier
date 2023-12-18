import tflite_runtime.interpreter as tflite
from keras_image_helper import create_preprocessor

interpreter = tflite.Interpreter(model_path='butterfly-model.tflite')
interpreter.allocate_tensors()

input_idx = interpreter.get_input_details()[0]['index']
output_idx = interpreter.get_output_details()[0]['index']

classes = ['ADONIS',
 'AFRICAN GIANT SWALLOWTAIL',
 'AMERICAN SNOOT',
 'AN 88',
 'APPOLLO',
 'ATALA',
 'BANDED ORANGE HELICONIAN',
 'BANDED PEACOCK',
 'BECKERS WHITE',
 'BLACK HAIRSTREAK',
 'BLUE MORPHO',
 'BLUE SPOTTED CROW',
 'BROWN SIPROETA',
 'CABBAGE WHITE',
 'CAIRNS BIRDWING',
 'CHECQUERED SKIPPER',
 'CHESTNUT',
 'CLEOPATRA',
 'CLODIUS PARNASSIAN',
 'CLOUDED SULPHUR',
 'COMMON BANDED AWL',
 'COMMON WOOD-NYMPH',
 'COPPER TAIL',
 'CRECENT',
 'CRIMSON PATCH',
 'DANAID EGGFLY',
 'EASTERN COMA',
 'EASTERN DAPPLE WHITE',
 'EASTERN PINE ELFIN',
 'ELBOWED PIERROT',
 'GOLD BANDED',
 'GREAT EGGFLY',
 'GREAT JAY',
 'GREEN CELLED CATTLEHEART',
 'GREY HAIRSTREAK',
 'INDRA SWALLOW',
 'IPHICLUS SISTER',
 'JULIA',
 'LARGE MARBLE',
 'MALACHITE',
 'MANGROVE SKIPPER',
 'MESTRA',
 'METALMARK',
 'MILBERTS TORTOISESHELL',
 'MONARCH',
 'MOURNING CLOAK',
 'ORANGE OAKLEAF',
 'ORANGE TIP',
 'ORCHARD SWALLOW',
 'PAINTED LADY',
 'PAPER KITE',
 'PEACOCK',
 'PINE WHITE',
 'PIPEVINE SWALLOW',
 'POPINJAY',
 'PURPLE HAIRSTREAK',
 'PURPLISH COPPER',
 'QUESTION MARK',
 'RED ADMIRAL',
 'RED CRACKER',
 'RED POSTMAN',
 'RED SPOTTED PURPLE',
 'SCARCE SWALLOW',
 'SILVER SPOT SKIPPER',
 'SLEEPY ORANGE',
 'SOOTYWING',
 'SOUTHERN DOGFACE',
 'STRAITED QUEEN',
 'TROPICAL LEAFWING',
 'TWO BARRED FLASHER',
 'ULYSES',
 'VICEROY',
 'WOOD SATYR',
 'YELLOW SWALLOW TAIL',
 'ZEBRA LONG WING']

# url = "https://i2.wp.com/www.dorsetbutterflies.com/wordpress/wp-content/uploads/2018/08/Adonis-Blue-James-Gould-2017-crop.jpg?fit=2103%2C1402&ssl=1"

def predict(url):
    preprocessor = create_preprocessor('resnet50', target_size=(224, 224))
    X = preprocessor.from_url(url)


    interpreter.set_tensor(input_idx, X)
    interpreter.invoke()
    tflite_new_pred = interpreter.get_tensor(output_idx)

    tflite_result = dict(zip(classes, tflite_new_pred[0]))

    return max(tflite_result, key=tflite_result.get)


def lambda_handler(event, context):
    url = event['url']
    pred = predict(url)
    result = {
        'prediction': pred
    }

    return result