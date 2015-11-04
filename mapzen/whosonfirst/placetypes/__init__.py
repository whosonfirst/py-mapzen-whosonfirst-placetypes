# https://pythonhosted.org/setuptools/setuptools.html#namespace-packages
__import__('pkg_resources').declare_namespace(__name__)

# Generated from: https://github.com/whosonfirst/whosonfirst-placetypes/blob/master/bin/compile.py
# placetypes-spec-20151104.json

__SPEC__ = {"102312321": {"role": "optional", "name": "microhood", "parent": [102312319], "names": {}}, "102312323": {"role": "optional", "name": "macrohood", "parent": [102312317], "names": {}}, "102312325": {"role": "common_optional", "name": "venue", "parent": [102312327, 102312329, 102312331, 102312321, 102312319], "names": {}}, "102312327": {"role": "common_optional", "name": "building", "parent": [102312329, 102312331, 102312321, 102312319], "names": {}}, "102312329": {"role": "common_optional", "name": "address", "parent": [102312331, 102312321, 102312319], "names": {}}, "102312331": {"role": "common_optional", "name": "campus", "parent": [102312321, 102312319], "names": {}}, "404528653": {"role": "common_optional", "name": "ocean", "parent": [102312341], "names": {}}, "102312335": {"role": "common_optional", "name": "empire", "parent": [102312309], "names": {}}, "102312341": {"role": "common_optional", "name": "planet", "parent": [], "names": {}}, "102320821": {"role": "common_optional", "name": "dependency", "parent": [102312307], "names": {}}, "136057795": {"role": "common_optional", "name": "timezone", "parent": [102312307, 102312309, 102312341], "names": {}}, "404528655": {"role": "common_optional", "name": "marinearea", "parent": [102312307, 102312309, 102312341], "names": {}}, "102371933": {"role": "optional", "name": "metroarea", "parent": [], "names": {}}, "404221409": {"role": "common_optional", "name": "localadmin", "parent": [102312313, 102312311], "names": {}}, "404221411": {"role": "optional", "name": "macroregion", "parent": [102320821, 102322043, 102312307], "names": {}}, "404221413": {"role": "optional", "name": "macrocounty", "parent": [102312311], "names": {}}, "102312307": {"role": "common", "name": "country", "parent": [102312335, 102312309], "names": {}}, "102312309": {"role": "common", "name": "continent", "parent": [102312341], "names": {}}, "102312311": {"role": "common", "name": "region", "parent": [404221411, 102320821, 102322043, 102312307], "names": {}}, "102312313": {"role": "common_optional", "name": "county", "parent": [404221413, 102312311], "names": {}}, "102322043": {"role": "common_optional", "name": "disputed", "parent": [102312307], "names": {}}, "102312317": {"role": "common", "name": "locality", "parent": [404221409, 102312313, 102312311], "names": {}}, "102312319": {"role": "common", "name": "neighbourhood", "parent": [102312323, 102312317], "names": {"eng_p": ["neighbourhood", "neighborhood"]}}}


# This is mostly for efficiency of the moment so I don't have to rewrite
# all the code below (20150807/thisisaaronland)

__PLACETYPES__ = {}
__ROLES__ = {}

for id, details in __SPEC__.items():

    name = details['name']
    role = details['role']
    parents = []

    for pid in details['parent']:
        _pid = str(pid)
        _parent = __SPEC__[_pid]
        parents.append(_parent['name'])

    __PLACETYPES__[name] = {
        'id': id,
        'role': role,
        'parent': parents
    }

    names = details.get('names', {})
    __PLACETYPES__[name]['names'] = names

    for label, alts in names.items():

        if not label.endswith("_p"):
            continue

        for alt in alts:
            
            if not __PLACETYPES__.get(alt, False):
                __PLACETYPES__[alt] = __PLACETYPES__[name]

    if not __ROLES__.get(role, False):
        __ROLES__[role] = {}

    # alt names and roles?

class placetypename:
    
    def __init__(self, label, name):

        lang, kind = label.split("_")
        self.lang = lang
        self.kind = kind
        self.name = name

    def __str__(self):
        return self.name
        
    def __repr__(self):
        return self.name

class placetype:
    
    def __init__(self, pl):

        if not __PLACETYPES__.get(pl, False):
            raise Exception, "Invalid placetype, %s" % pl

        self.placetype = pl
        self.details = __PLACETYPES__[pl]

    def id(self):
        return self.details['id']

    def role(self):
        return self.details['role']

    def names(self):

        for label, names in self.details['names'].items():
            for n in names:
                yield placetypename(label, n)

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

def is_valid_role(role):

    return __ROLES__.has_key(role)

def with_role(role):
    return with_roles([role])

def with_roles(roles):

    placetypes = []

    for pt, details in __PLACETYPES__.items():

        if not details.get('role', None) in roles:
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
