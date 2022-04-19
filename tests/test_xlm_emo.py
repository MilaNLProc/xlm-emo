#!/usr/bin/env python

"""Tests for `xlm_emo` package."""


import unittest
from xlm_emo.classifier import EmotionClassifier


class TestXlm_emo(unittest.TestCase):
    """Tests for `xlm_emo` package."""

    ec = EmotionClassifier()

    predictions = ec.predict(["senti testa di cazzo", "I am very happy"])

    assert predictions == ["anger", "joy"]

