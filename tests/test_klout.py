"""
Unit tests for Klout API
"""
from __future__ import with_statement
import time
import unittest2

from klout import Klout, KloutHTTPError


class KloutBaseTest(unittest2.TestCase):
    """
    Base test that setups the Klout key
    """
    def setUp(self):
        with open('key') as key_file:
            self.key = key_file.readline().strip()


class TestKlout(unittest2.TestCase):
    """
    Tests declaring Klout object
    """
    def test_klout(self):
        """
        Tests that key is required parameter
        """
        with self.assertRaises(TypeError):
            Klout()  # pylint: disable=no-value-for-parameter


class TestKloutIdentity(KloutBaseTest):
    """
    Test fetching Klout identity
    """
    def test_identity_by_twitter_id(self):
        """
        Tests that Klout entity can be fetched via Twitter id
        """
        k = Klout(self.key)
        result = k.identity.klout(tw=11158872)
        self.assertIn('id', result)
        self.assertIn('network', result)

        result = k.identity.klout(tw='11158872')
        self.assertIn('id', result)
        self.assertIn('network', result)
        time.sleep(1)

    def test_identity_by_google_plus(self):
        """
        Tests that Klout entity can be fetched via Google Plus id
        """
        k = Klout(self.key)
        result = k.identity.klout(gp=112975106809988327760)
        self.assertIn('id', result)
        self.assertIn('network', result)

        result = k.identity.klout(gp='112975106809988327760')
        self.assertIn('id', result)
        self.assertIn('network', result)
        time.sleep(1)

    def test_identity_by_twitter_name(self):
        """
        Tests that Klout entity can be fetched via twitter screen name
        """
        k = Klout(self.key)
        result = k.identity.klout(screenName='erfaan')
        self.assertIn('id', result)
        self.assertIn('network', result)
        time.sleep(1)

    def test_google_plus_by_identity(self):
        """
        Tests that Google Plus identidy can be fetched via Klout
        """
        k = Klout(self.key)
        result = k.identity.gp(klout=11747)
        self.assertIn('id', result)
        self.assertIn('network', result)

        result = k.identity.gp(klout='11747')
        self.assertIn('id', result)
        self.assertIn('network', result)
        time.sleep(1)

    def test_twitter_id_by_identity(self):
        """
        Tests that Twitter identidy can be fetched via Klout
        """
        k = Klout(self.key)
        result = k.identity.tw(klout=11747)
        self.assertIn('id', result)
        self.assertIn('network', result)

        result = k.identity.tw(klout='11747')
        self.assertIn('id', result)
        self.assertIn('network', result)
        time.sleep(1)


class TestKloutUser(KloutBaseTest):
    """
    Tests fetching different Klout entities like Score, Influence and
    user topics
    """
    def test_user_score(self):
        """
        Tests that Klout score of a user is always between 0 and 100
        """
        k = Klout(self.key)
        result = k.user.score(kloutId=11747)
        self.assertIn('score', result)
        self.assertLess(result['score'], 100.0)
        self.assertGreater(result['score'], 0.0)

        result = k.user.score(kloutId='11747')
        self.assertIn('score', result)
        self.assertLess(result['score'], 100.0)
        self.assertGreater(result['score'], 0.0)
        time.sleep(1)

    def test_user_influence(self):
        """
        Tests that the Klout influence contains influencers and influencees
        """
        k = Klout(self.key)
        result = k.user.influence(kloutId=11747)
        self.assertIn('myInfluencers', result)
        self.assertIn('myInfluencees', result)

        result = k.user.influence(kloutId='11747')
        self.assertIn('myInfluencers', result)
        self.assertIn('myInfluencees', result)
        time.sleep(1)

    def test_user_topics(self):
        """
        Tests fetching user topics
        """
        klout = Klout(self.key)
        result = klout.user.topics(kloutId=11747)
        self.assertIsInstance(result, list)
        for topic in result:
            for key in ['displayName', 'displayType', 'id',
                        'imageUrl', 'name', 'slug']:
                self.assertIn(key, topic.keys())

        result = klout.user.topics(kloutId='11747')
        self.assertIsInstance(result, list)
        for topic in result:
            for key in ['displayName', 'displayType', 'id',
                        'imageUrl', 'name', 'slug']:
                self.assertIn(key, topic.keys())
        time.sleep(1)


class TestTimeout(KloutBaseTest):
    """
    Test HTTP Connection timeout
    """

    def test_timeout(self):
        """
        Tests that a Http Connection timeout raises an exception
        """
        k = Klout(self.key)
        result = k.user.score(kloutId=11747, timeout=60)
        self.assertIn('score', result)

        with self.assertRaises(KloutHTTPError):
            result = k.user.score(kloutId=11747, timeout=0.001)
        time.sleep(1)


class TestSecure(KloutBaseTest):
    """
    Tests passing secure flag with API requests
    """
    def test_secure(self):
        """
        Tests that passing secure flag will return user's score
        """
        k = Klout(self.key, secure=True)
        result = k.user.score(kloutId=11747)
        self.assertIn('score', result)
        time.sleep(1)


if __name__ == '__main__':
    unittest2.main()
