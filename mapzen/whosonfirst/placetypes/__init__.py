# https://pythonhosted.org/setuptools/setuptools.html#namespace-packages
__import__('pkg_resources').declare_namespace(__name__)

__PLACETYPES__ = {
    'microhood': { 'role': 'optional', 'parent': [ 'neighbourhood'] },
    'neighbourhood': { 'role': 'common', 'parent': [ 'locality' ] },
    'locality': { 'role': 'common', 'parent': [ 'county', 'region' ] },
    'county': { 'role': 'common', 'parent': [ 'region' ], },
    'region': { 'role': 'common', 'parent': [ 'country' ] },
    'country': { 'role': 'common', 'parent': [ 'continent' ] },
    'continent': { 'role': 'common', 'parent': [ ] },
}

class placetype:
    
    def __init__(self, pl):
        
        if not __PLACETYPES__.get(pl, False):
            raise Exception, "Invalid placetype"

        self.placetype = pl
        self.details = __PLACETYPES__[pl]

def is_valid_placetype(pt, role=None):

    if not __PLACETYPES__.get(pt, False):
        return False

    if role and __PLACETYPES__[pt].get('role', None) != role:
        return False

    return True

def common():
    return with_role('common')

def optional():
    return with_role('optional')

def with_role(role):

    placetypes = []

    for pt, details in __PLACETYPES__.items():

        if details.get('role', None) != role:
            continue
            
        placetypes.append(pt)

    return placetypes
