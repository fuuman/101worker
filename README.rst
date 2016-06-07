.. image:: http://userpages.uni-koblenz.de/~mschanz/lookupMaven.png
   :align: center
   :target: https://github.com/fuuman/101worker/tree/master/modules/lookupMaven
   :alt: lookupMaven Logo

This new module was created to automatically find the Maven IDs/URLs
which are corresponding to Java imports in 101repos.

Structure
---------

The module was splitted into five single python files.

init.py
~~~~~~~

This file will be called by the ``run_module`` binary. It has to contain
a ``config`` dictionary and the methods ``run(context, c)`` and
``test``. We defined here only ``config`` and outsourced the other to
program.py and test.py.

program.py
~~~~~~~~~~

In this file the "main method" of the module ``run(context, c)`` is
implemented. It gets the needed resource ``.extractor.json``, run the
actual logic of the module and write a new derived resource
``.maven.json``

First we save us the filepath and programming language from the ``context`` and ``c`` in local variables.
Then we only continue, if the observed file is written in Java.

If yes, we read the imported modules from the ``extractor`` resource and iterate over that array. For each imported module we contact the ``MavenApi`` and append the requested result to out new JSON object ``maven_resource``. If we are finished, we write our JSON object into a new resource, the ``.maven.json``.

maven.py
~~~~~~~~

The class ``MavenApi`` is defined.

.. code:: python

    class MavenApi(object):
        """
        An instance of Maven_Api is able to fetch information from the Maven Central Repositories API.
        
        URL           -- Maven REST API
        LIMIT         -- Number of returned search results
        RETURN_FORMAT -- Result format [ XML | JSON ]
        """

An instance provides you the possibility to send a HTTP GET request to
that URL. The return value of this method will be an JSON or XML object
(default: JSON).

helper.py
~~~~~~~~~

Some little help methods used in ``run(context, c)``.

test.py
~~~~~~~

Not implemented. We tested our module manually. 
For that we configure seperate Java contributions in our 101worker config. 
Tested Contributions:
.. code:: bash
    contributions/javaParser
	contributions/javaTree
	contributions/javaRmi

For example:

In the ``.extractor.json`` resource our module found the import-array
.. code:: json
	{import: ["org.softlang.company.features.recognizer", "java.io"]}

Due to that input our module write the following derived resource ``.maven.json``:

.. code:: json
    {
        "org.softlang.company.features.recognizer": {},
        "java.io": {
            "URL": "http://mvnrepository.com/artifact/org.apache.flink/flink-jdbc/1.0.3-hadoop1",
            "ID": "org.apache.flink:flink-jdbc:1.0.3-hadoop1"
        }
    }

The first import is a self-writen module by the author of that repository. So there is no ID/URL on Maven for that. For ``Java.io`` we get a senseful response of course.


Maven API
---------

We used the REST API of maven.org which definition can be found under
https://search.maven.org/#api. The functionalitiy of the API is simple.
There is no need for any authorization. You just have to send a HTTP GET
and the answer will be the requested data in your requested format.

How to request?
~~~~~~~~~~~~~~~

We've used the URL for searching by fully-qualified classname in
Advanced Search.

HTTP GET to
``http://search.maven.org/solrsearch/select?q=fc:MODULE_SEARCHED&rows=NUMBER_OF_RESULTS&wt=FORMAT``

.. code:: bash
    MODULE_SEARCHED     - String containing the imported module name (e.g. "Java.io")
    NUMBER_OF_RESULTS   - Integer
    FORMAT              - Output format ( XML | JSON )

What response did we get?
~~~~~~~~~~~~~~~~~~~~~~~~~

Sample API response:

.. code:: json

    {
        "responseHeader": {
            "status": 0,
            "QTime": 73,
            "params": {
                "fl": "id,g,a,v,p,ec,timestamp,tags",
                "sort": "score desc,timestamp desc,g asc,a asc,v desc",
                "hl.snippets": "3",
                "indent": "off",
                "q": "fc:java.awt.color",
                "hl.fl": "fch",
                "wt": "json",
                "hl": "true",
                "rows": "2",
                "version": "2.2"
            }
        },
        "response": {
            "numFound": 22,
            "start": 0,
            "docs": [
                {
                    "id": "com.dragome:dragome-js-jre:0.96-beta2",
                    "g": "com.dragome",
                    "a": "dragome-js-jre",
                    "v": "0.96-beta2",
                    "p": "jar",
                    "timestamp": 1434753379000,
                    "tags": [
                        "module",
                        "dragome"
                    ],
                    "ec": [
                        "-sources.jar",
                        "-javadoc.jar",
                        ".jar",
                        ".pom"
                    ]
                },
                {
                    "id": "com.dragome:dragome-js-jre:0.95.5-beta1",
                    "g": "com.dragome",
                    "a": "dragome-js-jre",
                    "v": "0.95.5-beta1",
                    "p": "jar",
                    "timestamp": 1423106297000,
                    "tags": [
                        "module",
                        "dragome"
                    ],
                    "ec": [
                        "-sources.jar",
                        "-javadoc.jar",
                        ".jar",
                        ".pom"
                    ]
                }
            ]
        },
        "highlighting": {
            "com.dragome:dragome-js-jre:0.96-beta2": {
                "fch": [
                    "<em>java</em>.<em>awt</em>.<em>Color</em>"
                ]
            },
            "com.dragome:dragome-js-jre:0.95.5-beta1": {
                "fch": [
                    "<em>java</em>.<em>awt</em>.<em>Color</em>"
                ]
            }
        }
    }

We just need the ID of the repository. The URL will be derived from the
ID. For a sample output read the testing part please.


Developers
----------

-  Marco Schanz
-  Isabelle Kuhlmann
-  Diana Richter
-  Marius Beckmann
-  Frank Schaust
-  André-Gilbert Thomas
