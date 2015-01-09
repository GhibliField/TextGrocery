import uuid
import os
import shutil

from converter import GroceryTextConverter
from .learner import *


class GroceryTextModel(object):
    def __init__(self, text_converter=None, model=None):
        if isinstance(text_converter, GroceryTextConverter):
            self.text_converter = text_converter
        self.svm_model = model
        self._hashcode = str(uuid.uuid4())

    def __str__(self):
        return 'TextModel instance ({0}, {1})'.format(self.text_converter, self.svm_model)

    def get_labels(self):
        return [self.text_converter.get_class_name(k) for k in self.svm_model.get_labels()]

    def load(self, model_name):
        try:
            with open(model_name + '/id', 'r') as fin:
                self._hashcode = fin.readline().strip()
        except IOError:
            raise ValueError("The given model is invalid.")
        self.text_converter = GroceryTextConverter().load(model_name + '/converter')
        self.svm_model = LearnerModel(model_name + '/learner')

    def save(self, model_name, force=False):
        if self.svm_model is None:
            raise Exception('This model can not be saved because svm model is not given.')
        if os.path.exists(model_name) and force:
            shutil.rmtree(model_name)
        try:
            os.mkdir(model_name)
        except OSError as e:
            raise OSError(e, 'Please use force option to overwrite the existing files.')
        self.text_converter.save(model_name + '/converter')
        self.svm_model.save(model_name + '/learner', force)

        with open(model_name + '/id', 'w') as fout:
            fout.write(self._hashcode)

    def predict_text(self, text):
        if self.svm_model is None:
            raise Exception('This model is not usable because svm model is not given')
        if not isinstance(text, str):
            raise TypeError('The argument should be plain text')
        text = self.text_converter.to_svm(text)
        y, dec = predict_one(text, self.svm_model)
        y = self.text_converter.get_class_name(int(y))
        labels = [self.text_converter.get_class_name(k) for k in
                  self.svm_model.label[:self.svm_model.nr_class]]
        return GroceryPredictResult(predicted_y=y, dec_values=dec[:self.svm_model.nr_class], labels=labels)


class GroceryPredictResult(object):
    def __init__(self, predicted_y=None, dec_values=None, labels=None):
        self.predicted_y = predicted_y
        self.dec_values = dec_values
        self.labels = labels