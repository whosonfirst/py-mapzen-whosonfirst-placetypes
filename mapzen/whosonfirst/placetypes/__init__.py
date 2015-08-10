# https://pythonhosted.org/setuptools/setuptools.html#namespace-packages
__import__('pkg_resources').declare_namespace(__name__)

# Generated from: https://github.com/mapzen/whosonfirst-placetypes/blob/master/bin/compile.py

__SPEC__ = {
    "102312307": {
        "name": "country",
        "names": {},
        "parent": [
            102312335,
            102312309
        ],
        "role": "common"
    },
    "102312309": {
        "name": "continent",
        "names": {},
        "parent": [
            102312341
        ],
        "role": "common"
    },
    "102312311": {
        "name": "region",
        "names": {},
        "parent": [
            102312307
        ],
        "role": "common"
    },
    "102312313": {
        "name": "county",
        "names": {},
        "parent": [
            102312311
        ],
        "role": "common_optional"
    },
    "102312317": {
        "name": "locality",
        "names": {},
        "parent": [
            102312313,
            102312311
        ],
        "role": "common"
    },
    "102312319": {
        "name": "neighbourhood",
        "names": {
            "eng_p": [
                "neighbourhood",
                "neighborhood"
            ]
        },
        "parent": [
            102312323,
            102312317
        ],
        "role": "common"
    },
    "102312321": {
        "name": "microhood",
        "names": {},
        "parent": [
            102312319
        ],
        "role": "optional"
    },
    "102312323": {
        "name": "macrohood",
        "names": {},
        "parent": [
            102312317
        ],
        "role": "optional"
    },
    "102312325": {
        "name": "venue",
        "names": {},
        "parent": [
            102312327,
            102312329,
            102312331,
            102312321,
            102312319
        ],
        "role": "common_optional"
    },
    "102312327": {
        "name": "building",
        "names": {},
        "parent": [
            102312329,
            102312331,
            102312321,
            102312319
        ],
        "role": "common_optional"
    },
    "102312329": {
        "name": "address",
        "names": {},
        "parent": [
            102312331,
            102312321,
            102312319
        ],
        "role": "common_optional"
    },
    "102312331": {
        "name": "campus",
        "names": {},
        "parent": [
            102312321,
            102312319
        ],
        "role": "common_optional"
    },
    "102312335": {
        "name": "empire",
        "names": {},
        "parent": [
            102312309
        ],
        "role": "common_optional"
    },
    "102312341": {
        "name": "planet",
        "names": {},
        "parent": [],
        "role": "common_optional"
    },
    "102320821": {
        "name": "dependency",
        "names": {},
        "parent": [
            102312307
        ],
        "role": "common_optional"
    },
    "102322043": {
        "name": "disputed",
        "names": {},
        "parent": [
            102312307
        ],
        "role": "common_optional"
    },
    "102371933": {
        "name": "metroarea",
        "names": {},
        "parent": [],
        "role": "optional"
    },
    "136057795": {
        "name": "timezone",
        "names": {},
        "parent": [
            102312307,
            102312309,
            102312341
        ],
        "role": "common_optional"
    }
}

# This is mostly for efficiency of the moment so I don't have to rewrite
# all the code below (20150807/thisisaaronland)

__PLACETYPES__ = {}

for id, details in __SPEC__.items():

    name = details['name']
    role = details['role']
    parents = []

    for pid in details['parent']:
        _pid = str(pid)
        _parent = __SPEC__[_pid]
        parents.append(_parent['name'])

    __PLACETYPES__[name] = {
        'role': role,
        'parent': parents
    }

class placetype:
    
    def __init__(self, pl):

        if not __PLACETYPES__.get(pl, False):
            raise Exception, "Invalid placetype, %s" % pl

        self.placetype = pl
        self.details = __PLACETYPES__[pl]

    def parents(self):

        for p in self.details['parent']:
            yield placetype(p)

    def ancestors(self, roles=['common'], ancestors=[]):

        for p in self.parents():

            name = str(p)
            role = p.details['role']

            if not name in ancestors and role in roles:
                ancestors.append(str(p))

            p.ancestors(roles, ancestors)

        return ancestors
            
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

if __name__ == '__main__':

    pt = placetype('neighbourhood')
    print pt

    for p in pt.parents():
        print p
    
    print "--"

    for a in pt.ancestors():
        print a
