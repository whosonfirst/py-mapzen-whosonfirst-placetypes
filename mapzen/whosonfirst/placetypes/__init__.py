# https://pythonhosted.org/setuptools/setuptools.html#namespace-packages
__import__('pkg_resources').declare_namespace(__name__)

# sudo make me a generic JSON blob other languages can use the same spec?
# (20150715/thisisaaronland)

# SUDO PLEASE TO UPDATE TO USE https://github.com/mapzen/whosonfirst-placetypes
# WHATEVER THAT MEANS IN PRACTICAL TERMS (20150721/thisisaaronland)

__PLACETYPES__ = {

    'venue': {
        'role': 'common_optional',
        'parent': [ 'building', 'address', 'campus', 'microhood', 'neighbourhood' ]
    },

    'building': {
        'role': 'common_optional',
        'parent': [ 'address', 'campus', 'microhood', 'neighbourhood' ]
    },

    'address': {
        'role': 'common_optional',
        'parent': [ 'campus', 'microhood', 'neighbourhood' ]
    },
    
    'campus': {
        'role': 'common_optional',
        'parent': [ 'microhood', 'neighbourhood' ]
    },

    'microhood': {
        'role': 'optional',
        'parent': [ 'neighbourhood']
    },

    'neighbourhood': {
        'role': 'common',
        'parent': [ 'macrohood', 'locality' ]
    },

    'macrohood': {
        'role': 'optional',
        'parent': [ 'locality']
    },

    'locality': {
        'role': 'common',
        'parent': [ 'county', 'region' ]
    },

    # 'metro': {},

    'county': {
        'role': 'common_optional',
        'parent': [ 'region' ]
    },

    'region': {
        'role': 'common',
        'parent': [ 'country' ]
    },

    'country': {
        'role': 'common',
        'parent': [ 'empire', 'continent' ]
    },

    'empire': {
        'role': 'common_optional',
        'parent': [ 'continent' ]
    },

    'continent': {
        'role': 'common',
        'parent': [ 'planet' ]
    },

    'planet': {
        'role': 'common_optional',
        'parent': []
    }
}

class placetype:
    
    def __init__(self, pl):
        
        if not __PLACETYPES__.get(pl, False):
            raise Exception, "Invalid placetype"

        self.placetype = pl
        self.details = __PLACETYPES__[pl]

    def parents(self):

        for p in self.details['parent']:
            yield placetype(p)

    def __str__(self):
        return self.placetype

    def __repl__(self):
        return self.placetype

def is_valid_placetype(pt, role=None):

    if not __PLACETYPES__.get(pt, False):
        return False

    if role and __PLACETYPES__[pt].get('role', None) != role:
        return False

    return True

def common():
    return with_role('common')

def common_optional():
    return with_role('common_optional')

def optional():
    return with_role('optional')

# allow multiple roles?

def with_role(role):

    placetypes = []

    for pt, details in __PLACETYPES__.items():

        if details.get('role', None) != role:
            continue
            
        placetypes.append(pt)

    return placetypes
