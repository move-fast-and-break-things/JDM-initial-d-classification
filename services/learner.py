from fastai.vision.all import load_learner


class Learner:
    _instance = None

    def __init__(self):
        raise RuntimeError('Call instance() instead')

    @classmethod
    def instance(cls, path):
        if cls._instance is None:
            learn_inf = load_learner(path)
            cls._instance = learn_inf
        return cls._instance
