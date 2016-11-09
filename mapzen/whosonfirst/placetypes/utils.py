import mapzen.whosonfirst.placetypes
import logging

# options is assumed to be a optparse.OptionParser thingy

def placetypes_from_options(options, **kwargs):

    ignore_flag = kwargs.get('ignore_flag', 'ignore')
    ignore = optstring_to_list(options, ignore_flag)

    for pt in placetypes_from_flags_unfiltered(options, **kwargs):

        if not pt in ignore:
            yield pt

def placetypes_from_flags_unfiltered(options, **kwargs):

    placetypes_flag = kwargs.get('placetypes_flag', 'placetypes')
    roles_flag = kwargs.get('roles_flag', 'roles')

    placetypes = optstring_to_list(options, placetypes_flag)

    if len(placetypes):

        for pt in placetypes:
            pt = pt.strip()

            if not mapzen.whosonfirst.placetypes.is_valid_placetype(pt):
                logging.warning("%s is not a valid placetype, skipping")
                continue

            yield pt

    # elif options.roles:

    else:

        for pt in mapzen.whosonfirst.placetypes.with_roles(['common', 'common_optional', 'optional']):
            yield pt

def optstring_to_list(options, flag):

    str_value = options.ensure_value(flag, "")
    list_values = []

    if str_value != "":
        list_values = str_value.split(",")

    return list_values

