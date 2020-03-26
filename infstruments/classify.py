import collections as co
import itertools
import logging

from sklearn.neighbors import KNeighborsClassifier

class CharStatsClassifier:
    """ Classify strings based on character frequencies."""

    def __init__(self, training, target,
                 preproc=(lambda s:s), n_neighbors=1, debuglog=False):
        """ Setup classifier based on `training` data and `target` values.

        `training`: A sequence of _n_ strings serve as training examples.

        `target`: A sequence of _n_ classification target values,
            corresponding to the `training` examples.

        `n_neighbors`: Num of neighbors considered in the nearest
            neighbours classification.

        `preproc`: Preprocess strings before calculating the
            character frequencies. The frequencies for a string `s` will be
            based on `preproc(s)`.

        `debuglog`:
            If `True` verbose debug output will be written to the log.
        """
        self.debuglog = debuglog
        self.preproc = preproc
        training_pre = [preproc(s) for s in training ]
        self.chars = list(set(itertools.chain.from_iterable(training_pre)))
        self.chars.sort()   # sorted list of all characters (after preproc)
        training_stats = [self._char_stats(s) for s in training_pre]
        if debuglog:
            for tr, pr, st in zip(training, training_pre, training_stats):
                logging.debug("TR: %s" % tr)
                logging.debug("    %s %s" % (pr, st))
        X = training_stats
        y = target
        self.neigh = KNeighborsClassifier(n_neighbors=n_neighbors)
        self.neigh.fit(X, y)

    def _char_stats(self, s):
        """ Calculate character statistics.

            The statistics is returned as a list of occurrence frequencies
            for each character in the oreder in self.chars.

            Frequency values are proportions between 0.0 and 1.0.
            """

        if not s:
            raise ValueError("Got zero-length string for char frequency!")
        logging.debug("_char_stats: %s" % s)
        cnts = co.defaultdict(float, co.Counter(s))
        total = sum(cnts.values())
        stats = []
        for c in self.chars:
            stats.append(cnts[c]/float(total))
        return stats

    def classify_s (self, s):
        """ Classify a string `s` based on its character frequencies.

        `preproc` is applied before the classification (cf. __init__).

        Returns the classification result.
        """
        pre = self.preproc(s)
        stats = self._char_stats(pre)
        result = self.neigh.predict([stats])[0]
        if self.debuglog:
            logging.debug("CL: %s %s" % (result, s))
            logging.debug("    %s %s %s" % (result, pre, stats))
        return result
