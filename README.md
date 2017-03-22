# py-mapzen-whosonfirst-placetypes

## Install

```
sudo pip install -r requirements.txt .
```

## Important

The specification for placetypes is derived from the [whosonfirst-placetypes](https://github.com/whosonfirst/whosonfirst-placetypes) package. For example:

```
$> /usr/local/mapzen/whosonfirst-placetypes/bin/compile.py | python -mjson.tool 
{
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
    }
    ...
}
```

The specification itself is hardcoded in [mapzen/whosonfirst/placetypes/\__init__.py](https://github.com/whosonfirst/py-mapzen-whosonfirst-placetypes/blob/master/mapzen/whosonfirst/placetypes/__init__.py). Whether or the specification can or should be loaded from a config file or equivalent has been left for another day.

## See also

* https://github.com/whosonfirst/whosonfirst-placetypes
