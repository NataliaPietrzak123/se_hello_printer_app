import unittest
import json
from hello_world import app
from hello_world.formater import SUPPORTED


class FlaskrTestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_outputs(self):
        rv = self.app.get('/outputs')
        ','.join(SUPPORTED) in rv.data

    def test_msg_with_output(self):
        rv = self.app.get('/?output=json')
        j = json.loads(rv.data)
        self.assertEquals(j['imie'], "Natalia")
        self.assertEquals(j['msg'], "Hello World!")

    def test_msg_with_output_xml(self):
        rv = self.app.get('/?output=xml')
        self.assertEquals('<greetings>\n<name>Justyna</name>\n' +
                          '<msg>Hello World!</msg>\n</greetings>', rv.data)
