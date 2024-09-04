#!/usr/bin/env python3
""" caching system
    """

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ caching system:

    Args:
        LIFOCache ([class]): [basic caching]
    """

    def put(self, key, item):
        """ Add an item in the cache
        """
        if not (key is None or item is None):
            self.cache_data[key] = item
            temp_list = [x for x in self.cache_data.keys()]
            if len(self.cache_data.keys()) > self.MAX_ITEMS:
                if temp_list.count(key) > 1:
                    pop = key
                else:
                    pop = temp_list[-2]
                self.cache_data.pop(pop)
                print(f"DISCARD: {pop}")

    def get(self, key):
        """ Get an item by key
        """
        return self.cache_data.get(key)
