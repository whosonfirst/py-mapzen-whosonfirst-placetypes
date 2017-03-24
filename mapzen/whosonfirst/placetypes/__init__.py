import spec	# as in utils/mk-spec.py > mapzen/whosonfirst/placetypes/spec.py

# This is mostly for efficiency of the moment so I don't have to rewrite
# all the code below (20150807/thisisaaronland)

__PLACETYPES__ = {}
__ROLES__ = {}

for id, details in spec.__SPEC__.items():

    name = details['name']
    role = details['role']
    parents = []

    for pid in details['parent']:
        _pid = str(pid)
        _parent = spec.__SPEC__[_pid]
        parents.append(_parent['name'])

    __PLACETYPES__[name] = {
        'id': id,
        'role': role,
        'name': name,
        'parent': parents
    }

    __PLACETYPES__[str(id)] = {
        'id': id,
        'role': role,
        'name': name,
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

        pl = str(pl)

        if not __PLACETYPES__.get(pl, False):
            raise Exception, "Invalid placetype, %s" % pl

        self.placetype = __PLACETYPES__[pl]['name']
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

    def children(self):

        id = self.details['id']
        id = int(id)

        all = []

        for other_id, details in spec.__SPEC__.items():

            if id in details['parent']:
                all.append(details['name'])

        for pt in self.sort_children(all):
            yield placetype(pt)

    def sort_children(self, all):

        kids = []
        grandkids = []

        for p in all:
            
            pt = placetype(p)
            is_grandkid = False

            for pr in pt.parents():

                if str(pr) in all:
                    is_grandkid = True
                    break
                
            if is_grandkid:
                grandkids.append(p)
            else:
                kids.append(p)

        if len(grandkids):
            grandkids = self.sort_children(grandkids)

        kids.extend(grandkids)
        return kids

    def ancestors(self, roles=['common'], _ancestors=[]):

        for p in self.parents():

            name = str(p)
            role = p.details['role']

            if not name in _ancestors and role in roles:
                _ancestors.append(str(p))

            p.ancestors(roles, _ancestors)

        return _ancestors

    def descendents(self, roles=['common'], _descendants=[]):
        return self.descendants(roles, _descendants)

    def descendants(self, roles=['common'], _descendants=[]):

        # print "> get descendants for %s w/ %s (%s)" % (self.placetype, ",".join(roles), "|".join(_descendants))

        grandkids = []
        
        for p in self.children():

            name = str(p)
            role = p.details['role']

            if not name in _descendants and role in roles:
                _descendants.append(str(p))

                for pp in p.children():

                    name = str(pp)
                    role = pp.details['role']
                    
                    if not name in grandkids and role in roles:
                        grandkids.append(str(pp))

        for str_pt in grandkids:

            if not str_pt in _descendants:
                _descendants.append(str_pt)

            pt = placetype(str_pt)
            pt.descendants(roles, _descendants)

        return _descendants
            
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

    for id, details in spec.__SPEC__.items():

        if not details.get('role', None) in roles:
            continue
          
        pt = details['name']
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
