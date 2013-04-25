====================
Design Philosophy
====================

This API wrapper tries to generalize the API calls. First we must find out the 
generalization in API URL structure.

--------------------------
Klout API URL Structure
--------------------------

Klout's API URL structure is RESTful with a little cutomization. Almost all 
API URLs can be generalized in a way.

<protocol>://<domain>/<version>/<resource>.<format>/<input_name>/<input_value>/<action>?<query_string>

* <protocol>: http or https
* <domain>: api.klout.com
* <version>: v2 for the new API
* <resource>: Currently there are only 2 resources *identity* and *user*
* <format>: Klout no longer supports *XML*. Only *json* is supported.
* <input_name>: (Optional) Name of the field to query. Required only when the input field is not *Primary Key*.
  Poissble values for *identity* resource are:

  * tw - Twitter
  * klout - (Written as ks in official Klout API documentation but it doesn't work)
  * gp - Google+
  * twitter (when using twitter screenName as input)
* <input_value>: Valule of the <input_name> specified. Can be twitter id, google plus id or klout id.
* <action>: Name of the action to be performed.
* <query_string>: Must contain a key obtained from <http://klout.com/s/developers/v2>. MUST also contain
  *screenName* when <input_name> is twitter

.. NOTE:: 
   <input_name> MUST be skipped when query a resource with *Primary Key*
   e.g. when call user resource with *kloutId*, the *<input_name>* should be skipped.

.. NOTE:: 
   <input_value> MUST be skipped when <input_name> is *twitter*
   The value should be passed in <query_string> instead.

.. NOTE:: 
   <action> MUST be skipped when expected result is *Primary Key*
   e.g. when call identity resource and expected result is *kloutId*

-----------------------------
Designing python functions
-----------------------------

After generalizing the API URLs, next step is to make a generalized pythonic function calls:

Here is what I propose::

  k = Klout(key='xxxxxxxxxxxxxxxxxxxxxxxx')
  k.<resource>.<action>(<input_name>=<input_value>)

--------------------------------------------------
Klout API URL to Python Function mapping examples
--------------------------------------------------
Here are all possible combinations of the URLs. Lets try to map them to our generalized structure defined above:

* http://api.klout.com/v2/identity.json/gp/112975106809988327760?key=xxxxxxxxxxxxxxxxxxxxxxxx

  * protocol: http
  * domain: api.klout.com
  * version: v2
  * resource: identity
  * format: json
  * input_name: gp - Google+
  * input_value: 112975106809988327760 - Google+ Id
  * action: Empty - We need kloutId as output
  * query_string: key=xxxxxxxxxxxxxxxxxxxxxxxx

  Code Example::

    k = Klout(key='xxxxxxxxxxxxxxxxxxxxxxxx')
    k.identity.klout(gp='112975106809988327760') 
    # Note that we replaced the empty action with klout as we want to be consistent

* http://api.klout.com/v2/identity.json/tw/11158872?key=xxxxxxxxxxxxxxxxxxxxxxxx

  * protocol: http
  * domain: api.klout.com
  * version: v2
  * resource: identity
  * format: json
  * input_name: tw - Twitter
  * input_value: 11158872 - Twitter Id
  * action: Empty - We need kloutId as output
  * query_string: key=xxxxxxxxxxxxxxxxxxxxxxxx

  Code Example::

    k = Klout(key='xxxxxxxxxxxxxxxxxxxxxxxx')
    k.identity.klout(tw='11158872') 
    # Note that we replaced the empty action with klout as we want to be consistent

* http://api.klout.com/v2/identity.json/twitter?key=xxxxxxxxxxxxxxxxxxxxxxxx&screenName=erfaan

  * protocol: http
  * domain: api.klout.com
  * version: v2
  * resource: identity
  * format: json
  * input_name: twitter
  * input_value: Empty - We want to query using twitter screenName
  * action: Empty - We need kloutId as output
  * query_string: key=xxxxxxxxxxxxxxxxxxxxxxxx&screenName=erfaan - screenName is only required in this case

  Code Example::

    k = Klout(key='xxxxxxxxxxxxxxxxxxxxxxxx')
    k.identity.klout(screenName='erfaan') 
    # Note that we replaced the empty action with klout as we want to be consistent
    # Also the input parameters query string are used as function parameters. (again consistency)

* http://api.klout.com/v2/identity.json/klout/11747/gp?key=xxxxxxxxxxxxxxxxxxxxxxxx

  * protocol: http
  * domain: api.klout.com
  * version: v2
  * resource: identity
  * format: json
  * input_name: klout
  * input_value: 11747
  * action: gp - Google+
  * query_string: key=xxxxxxxxxxxxxxxxxxxxxxxx

  Code Example::

    k = Klout(key='xxxxxxxxxxxxxxxxxxxxxxxx')
    k.identity.gp(klout='11747') 

* http://api.klout.com/v2/identity.json/klout/11747/tw?key=xxxxxxxxxxxxxxxxxxxxxxxx

  * protocol: http
  * domain: api.klout.com
  * version: v2
  * resource: identity
  * format: json
  * input_name: klout
  * input_value: 11747
  * action: tw - Twitter
  * query_string: key=xxxxxxxxxxxxxxxxxxxxxxxx

  Code Example::

    k = Klout(key='xxxxxxxxxxxxxxxxxxxxxxxx')
    k.identity.tw(klout='11747') 

* https://api.klout.com/v2/user.json/11747/score?key=xxxxxxxxxxxxxxxxxxxxxxxx

  * protocol: https
  * domain: api.klout.com
  * version: v2
  * resource: user
  * format: json
  * input_name: Empty - We are inputting kloutId
  * input_value: 11747
  * action: score
  * query_string: key=xxxxxxxxxxxxxxxxxxxxxxxx

  Code Example::

    k = Klout(key='xxxxxxxxxxxxxxxxxxxxxxxx')
    k.user.scrore(kloutId='11747') 

* https://api.klout.com/v2/user.json/11747/influence?key=xxxxxxxxxxxxxxxxxxxxxxxx

  * protocol: https
  * domain: api.klout.com
  * version: v2
  * resource: user
  * format: json
  * input_name: Empty - We are inputting kloutId
  * input_value: 11747
  * action: influence
  * query_string: key=xxxxxxxxxxxxxxxxxxxxxxxx

  Code Example::

    k = Klout(key='xxxxxxxxxxxxxxxxxxxxxxxx')
    k.user.influence(kloutId='11747') 

* https://api.klout.com/v2/user.json/11747/topics?key=xxxxxxxxxxxxxxxxxxxxxxxx

  * protocol: https
  * domain: api.klout.com
  * version: v2
  * resource: user
  * format: json
  * input_name: Empty - We are inputting kloutId
  * input_value: 11747
  * action: topics
  * query_string: key=xxxxxxxxxxxxxxxxxxxxxxxx

  Code Example::

    k = Klout(key='xxxxxxxxxxxxxxxxxxxxxxxx')
    k.user.topics(kloutId='11747') 

