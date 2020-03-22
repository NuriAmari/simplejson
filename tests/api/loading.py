import unittest
import json as simplejson

from src.json import json


class DecodingTests(unittest.TestCase):
    def test__loads__NumberLiterals__SuccessfulLoad(self):
        self.assertEqual(json.loads("1"), simplejson.loads("1"))
        self.assertEqual(json.loads("0"), simplejson.loads("0"))
        self.assertEqual(json.loads("-1"), simplejson.loads("-1"))
        self.assertEqual(json.loads("-1.0"), simplejson.loads("-1.0"))
        self.assertEqual(json.loads("-1.25"), simplejson.loads("-1.25"))
        self.assertEqual(json.loads("-1.25e1"), simplejson.loads("-1.25e1"))
        self.assertEqual(json.loads("-1.25E1"), simplejson.loads("-1.25E1"))
        self.assertEqual(json.loads("-1.25E13"), simplejson.loads("-1.25E13"))
        self.assertEqual(json.loads("-1.25E-13"), simplejson.loads("-1.25E-13"))

    def test__loads__StringLiterals__SuccessfulLoad(self):
        self.assertEqual(json.loads('""'), simplejson.loads('""'))
        self.assertEqual(json.loads('"abc"'), simplejson.loads('"abc"'))
        self.assertEqual(json.loads('"@#$abc"'), simplejson.loads('"@#$abc"'))

    def test__loads__StringEscaping__SuccessfulLoad(self):
        # Hmmm failing...
        self.assertEqual(json.loads('"\\""'), simplejson.loads('"\\""'))
        self.assertEqual(json.loads('"\\n"'), simplejson.loads('"\\n"'))

    def test__loads__OtherLiterals__SuccessfulLoad(self):
        self.assertEqual(json.loads("false"), simplejson.loads("false"))
        self.assertEqual(json.loads("true"), simplejson.loads("true"))
        self.assertEqual(json.loads("null"), simplejson.loads("null"))

    def test__loads__Arrays__SuccessfulLoad(self):
        self.assertEqual(json.loads("[1,2,3,4,5]"), simplejson.loads("[1,2,3,4,5]"))
