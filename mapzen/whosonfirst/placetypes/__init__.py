# https://pythonhosted.org/setuptools/setuptools.html#namespace-packages
__import__('pkg_resources').declare_namespace(__name__)

__PLACETYPES__ = {
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

def common():
    return with_role('common')

def with_role(role):

    placetypes = []

    for pt, details in __PLACETYPES__.items():

        if details.get('role', None) != role:
            continue
            
        placetypes.append(pt)

    return placetypes
