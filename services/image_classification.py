from fastai.vision.all import *
import requests
import io
import services.learner
import pathlib


def classificate(image_file_url):
    byte_file = io.BytesIO()

    if os.name == 'nt':
        pathlib.PosixPath = pathlib.WindowsPath
    
    path = Path(os.getcwd())

    path = os.path.join(path, 'model.pkl')

    learn_inf = services.learner.Learner.instance(path)

    byte_file.write(requests.get(image_file_url).content)

    img = PILImage.create(byte_file)

    pred,_,_ = learn_inf.predict(img)

    del byte_file

    return pred
    