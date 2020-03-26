import re

import pytest

import infstruments.classify as cla

class Test_CharStatsClassifier:
    def test_instantiation(self):
        training = ["aaaba", "bbaaa", "1222"]
        target = [1, 1, 2]
        clfier = cla.CharStatsClassifier(training, target)
        assert isinstance(clfier, cla.CharStatsClassifier)

    def test_classify(self):
        training = ["aaaba", "bbaaa", "1222"]
        target = ['ab', 'ab', '12']
        clfier = cla.CharStatsClassifier(training, target)
        assert clfier.classify_s("aaaba") == 'ab'
        assert clfier.classify_s("a1aba") == 'ab'
        assert clfier.classify_s("21aba") == 'ab'
        assert clfier.classify_s("212ba") == '12'
        assert clfier.classify_s("21211") == '12'

    def test_classify_preproc(self):
        def _preproc(s):
            s = re.sub(r'\d', "#", s)
            s = re.sub(r'\w', "a", s)
            return s

        training = ["aaaaa", "b2b3a4a1", "1222"]
        target = ['aa', 'a1', '11']
        clfier = cla.CharStatsClassifier(
                    training, target, preproc=_preproc)
        assert clfier.classify_s("aaaba")   == 'aa'
        assert clfier.classify_s("a1aba")   == 'aa'
        assert clfier.classify_s("212aaba") == 'a1'
        assert clfier.classify_s("212baa")  == 'a1'
        assert clfier.classify_s("a21211")  == '11'
        assert clfier.classify_s("211")     == '11'
