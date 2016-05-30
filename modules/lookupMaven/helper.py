"""
Module with help methods.

Developer:
"""
from .maven import MavenApi

def find_url_for_id(maven_id):
    """
    Finds the Repo-URL for a given Maven Repository-ID. 
    """
    return 'http://mvnrepository.com/artifact/' + maven_id.replace(':', '/')

def contact_maven(module):
    """
    Get repository information for a java module from maven 
    @params: module -- module name as String

    """
    api = MavenApi(module)
    return api.send_request()

