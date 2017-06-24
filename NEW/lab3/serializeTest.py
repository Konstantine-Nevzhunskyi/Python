""" Unit test for Serialize module """

from io import StringIO, BytesIO
import unittest
import pickle
import json
import yaml
from model import Model

class TestSerializeMethods(unittest.TestCase):
    """ Testing Serialize module """

    def setUp(self):
        m = Model("source")
        self.data = [m]
        self.output = None

    def test_pickle(self):
        """ test serialization with pickle """
        output = pickle.dumps(self.data)
        self.output = BytesIO(output)
        extr_data = pickle.load(self.output)
        self.assertEqual(self.data, extr_data)


    def test_yaml(self):
        """ test serialization with yaml """
        output = yaml.dump(self.data)
        self.output = StringIO(output)
        extr_data = yaml.load(self.output)
        self.assertEqual(self.data, extr_data)


    #def test_json(self):
    #    """ test serialization with json """
    #    output = json.dumps(self.data, default=jns.js_default)
    #    self.output = StringIO(output)
    #    users, books = json.load(self.output, 'json')
    #    self.assertEqual(self.data, [users, books])

    def tearDown(self):
        self.output.close()


if __name__ == "__main__":
    unittest.main()

