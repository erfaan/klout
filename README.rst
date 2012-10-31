==================
Klout API
==================

A minimalist klout API interface. Use of this API 
requires klout *developer key*. You can get registered and
get a key at

    <http://klout.com/s/developers/v2>

====================
Quickstart
====================

This short example shows how to get a kloutId first and fetch user's score using that kloutId::

    from klout import *
    
    # Make the Klout object
    k = Klout('YOUR_KEY_HERE')

    # Get kloutId of the user by inputting a twitter screenName
    kloutId = k.identity.klout(screenName="erfaan").get('id')

    # Get klout score of the user
    score = k.user.score(kloutId=kloutId).get('score')

    print "User's klout score is: %s" % (score) 

