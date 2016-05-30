import json
from .helper import find_url_for_id, contact_maven

def run(context, c):
    # Get Filepath of the actual file.
    f = c['file']

    # Get language from derived resource .lang.json
    lang = context.get_derived_resource(f, 'lang')

    # Just take care of java files
    if lang == 'Java':
        # Read array of imports from the extractor resource.
        imported_modules = context.get_derived_resource(f, 'extractor')['imports']

        # Define empty dictionary as output variable.
        maven_resource = {}
        
	# For every imported module do ...
        for module in imported_modules:
            # Create an empty dict .
            maven_resource[module] = {}
            
            # Contact Maven and get an array of JSON objects as result.
            # One JSON objects corresponds with one search result.
            api_results = contact_maven(module)['response']['docs']

            # For every search result do ...
            for index, api_result in enumerate(api_results):
                # Save ID and URL in the dict for this module.
                maven_resource[module]['ID'] = api_result['id']
                maven_resource[module]['URL'] = find_url_for_id(api_result['id'])
	
        # Write resource file.	
        context.write_derived_resource(f, maven_resource, 'maven')
            



        
