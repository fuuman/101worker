config = {
    'wantdiff': False,
    'wantsfiles': True,
    'threadsafe': False,
    'behavior': {
        'creates': [['resource', 'maven']],
        'uses': [['resource', 'extractor']]
    }
}

from .program import run
from .test import test

