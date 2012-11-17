from __future__ import with_statement
import doctest
import socket
import unittest2

try:
    import urllib.error as urllib_error
except ImportError:
    import urllib2 as urllib_error

from klout import *


class TestKlout(unittest2.TestCase):
    def test_klout(self):
        with self.assertRaises(TypeError):
            k = Klout()


class TestKloutIdentity(unittest2.TestCase):

    def setUp(self):
        f = open('key')
        self.key= f.readline().strip()
        f.close()

    def test_identityByTwitterId(self):
        k = Klout(self.key)
        result = k.identity.klout(tw=11158872)
        self.assertIn('id', result)
        self.assertIn('network', result)
        
        result = k.identity.klout(tw='11158872')
        self.assertIn('id', result)
        self.assertIn('network', result)
        
    def test_identityByGooglePlusId(self):
        k = Klout(self.key)
        result = k.identity.klout(gp=112975106809988327760)
        self.assertIn('id', result)
        self.assertIn('network', result)
        
        result = k.identity.klout(gp='112975106809988327760')
        self.assertIn('id', result)
        self.assertIn('network', result)

    def test_identityByTwitterScreenName(self):
        k = Klout(self.key)
        result = k.identity.klout(screenName='erfaan')
        self.assertIn('id', result)
        self.assertIn('network', result)

    def test_googlePlusIdByIdentity(self):
        k = Klout(self.key)
        result = k.identity.gp(klout=11747)
        self.assertIn('id', result)
        self.assertIn('network', result)

        result = k.identity.gp(klout='11747')
        self.assertIn('id', result)
        self.assertIn('network', result)

    def test_twitterIdByIdentity(self):
        k = Klout(self.key)
        result = k.identity.tw(klout=11747)
        self.assertIn('id', result)
        self.assertIn('network', result)

        result = k.identity.tw(klout='11747')
        self.assertIn('id', result)
        self.assertIn('network', result)


class TestKloutUser(unittest2.TestCase):

    def setUp(self):
        f = open('key')
        self.key= f.readline().strip()
        f.close()

    def test_userScore(self):
        k = Klout(self.key)
        result = k.user.score(kloutId=11747)
        self.assertIn('score', result)
        self.assertLess(result['score'], 100.0)
        self.assertGreater(result['score'], 0.0)

        result = k.user.score(kloutId='11747')
        self.assertIn('score', result)
        self.assertLess(result['score'], 100.0)
        self.assertGreater(result['score'], 0.0)

    def test_userInfluence(self):
        k = Klout(self.key)
        result = k.user.influence(kloutId=11747)
        self.assertIn('myInfluencers', result)
        self.assertIn('myInfluencees', result)

        result = k.user.influence(kloutId='11747')
        self.assertIn('myInfluencers', result)
        self.assertIn('myInfluencees', result)

    def test_userTopics(self):
        klout = Klout(self.key)
        result = klout.user.topics(kloutId=11747)
        self.assertIsInstance(result, list)
        for topic in result:
            for k, v in topic.items():
                self.assertIn(k, ['imageUrl', 'slug', 'displayName', 'id', 'name', 'topicType'])

        result = klout.user.topics(kloutId='11747')
        self.assertIsInstance(result, list)
        for topic in result:
            for k, v in topic.items():
                self.assertIn(k, ['displayName', 'imageUrl', 'slug', 'id', 'name', 'topicType'])


class TestTimeout(unittest2.TestCase):
    
    def setUp(self):
        f = open('key')
        self.key= f.readline().strip()
        f.close()
    
    def test_timeout(self):
        k = Klout(self.key)
        result = k.user.score(kloutId=11747, timeout=60)
        self.assertIn('score', result)
        
        with self.assertRaises(urllib_error.URLError) as er:
            result = k.user.score(kloutId=11747, timeout=0.001)
        self.assertIsInstance(er.exception.reason, socket.timeout)


class TestSecure(unittest2.TestCase):
    
    def setUp(self):
        f = open('key')
        self.key= f.readline().strip()
        f.close()
    
    def test_secure(self):
        k = Klout(self.key, secure=True)
        result = k.user.score(kloutId=11747)
        self.assertIn('score', result)
        

if __name__ == '__main__':
    unittest2.main()