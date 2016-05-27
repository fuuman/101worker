from .maven import MavenApi
import json

def run(context, c):
    # Get Filepath
    f = c['file']

    # Get language from derived resource .lang.json
    lang = context.get_derived_resource(f, 'lang')

    # Just take care of java files
    if lang == 'Java':
        # Read array of imports from the extractor resource
        imported_modules = context.get_derived_resource(f, 'extractor')['imports']

        # Define empty dictionary as output variable.
        maven_resource = {}
        results = []
        for module in imported_modules:
            maven_resource[module] = []
            api_results = contact_maven(module)['response']['docs']
            for api_result in api_results:
                maven_resource[module].append(api_result)
        context.write_derived_resource(f, maven_resource, 'maven')
            

def contact_maven(module):
    """
    Get repository information for a java module from maven 
    @params: module -- module name as String

    """
    api = MavenApi(module)
    return api.send_request()

        
