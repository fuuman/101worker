"""
Implementation of the MavenApi Class. 

Developer: Marius & Marco
"""

import urllib.request
import json

class MavenApi(object):
    """
    An instance of Maven_Api is able to connect the Maven Central Repositories.
    
    URL           -- Maven REST API
    LIMIT         -- Number of returned search results
    RETURN_FORMAT -- Result format [ XML | JSON ]
    """
    URL = 'https://search.maven.org/solrsearch/select?'
    REPO = 'http://mvnrepository.com/artifact/'
    LIMIT = 1
    RETURN_FORMAT = 'json'
 
    def __init__(self, search_for, limit=None, return_format=None):
        """ 
        Contructor
        
        @params: 
        search_for      -- Module name that should be searched
        rows [optional] -- see LIMIT
        wt [optional]   -- see RETURN_FORMAT
        """
        # Set default values
        if limit == None:
            limit = self.LIMIT
        if return_format == None:
            return_format = self.RETURN_FORMAT

        # Build URL.
        self.URL += ''.join([
            'q=fc:', search_for, 
            '&rows=', str(limit),
            '&wt=', return_format])

    def send_request(self):
        """ 
        Open the URL of the instance. 

        Returns the response as JSON Object. 
        """
        return json.loads(urllib.request.urlopen(self.URL).read().decode('utf-8'))


