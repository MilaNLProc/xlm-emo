#!/usr/bin/env python

"""Tests for `xlm_emo` package."""


import pytest
from xlm_emo.classifier import EmotionClassifier


def test_emotion_classifier():
    ec = EmotionClassifier()

    predictions = ec.predict(["senti testa di cazzo", "I am very happy"])

    assert predictions == ["anger", "joy"]

