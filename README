==================
Klout API
==================
.. image:: https://secure.travis-ci.org/erfaan/klout.png?branch=master
   :target: https://travis-ci.org/erfaan/klout

A minimalist klout API interface. Use of this API 
requires klout *developer key*. You can get registered and
get a key at

    <http://klout.com/s/developers/v2>

Complete documentation is available at: 
	
	<https://klout.readthedocs.org/en/latest/>

==============================
Design Philosoph
==============================

See `Design Philosophy <https://github.com/erfaan/klout/blob/master/docs/design-philosophy.rst>`_

====================
Quickstart
====================
Install the PyPi package::
    
    pip install Klout

This short example shows how to get a kloutId first and fetch user's score using that kloutId::

    from klout import *
    
    # Make the Klout object
    k = Klout('YOUR_KEY_HERE')

    # Get kloutId of the user by inputting a twitter screenName
    kloutId = k.identity.klout(screenName="erfaan").get('id')

    # Get klout score of the user
    score = k.user.score(kloutId=kloutId).get('score')

    print "User's klout score is: %s" % (score) 

    # By default all communication is not secure (HTTP). An optional secure parameter
    # can be sepcified for secure (HTTPS) communication
    k = Klout('YOUR_KEY_HERE', secure=True)

    # Optionally a timeout parameter (seconds) can also be sent with all calls
    score = k.user.score(kloutId=kloutId, timeout=5).get('score')

==================
License
==================
MIT License. See LICENSE.txt
Copyright (c) 2012 Irfan Ahmad