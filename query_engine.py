class QueryEngine:
    VALID_KEYS = ['filter', 'groupedBy']

    def __init__(self, interface):
        self.interface = interface
        self.index = self.interface.index

    def is_valid(self, q):
        for key in q:
            if key not in self.VALID_KEYS:
                return False
        return True

    def query(self, q):
        """
        1. Apply filters to queryset
        2. Apply groupby to queryset
        :param q: query as a dict
        :return: {totolCounts: <int>, groups: {<str>: <int>}}
        """
        if not self.is_valid(q):
            raise Exception('Invalid Query')
        result = {'totalCount': 0}
        queryset = self.process_filters(q)
        result['totalCount'] = len(queryset)
        if groups := q.get('groupedBy'):
            result['groups'] = self.process_groupby(queryset, groups)
        return result

    def process_filters(self, q):
        filters = q.get('filter', {})
        queryset = None
        for k, v in filters.items():
            if not queryset:
                queryset = self.index.filter(k, v)
            else:
                queryset = queryset.intersection(self.index.filter(k, v))
        return queryset

    def process_groupby(self, queryset, groups):
        return self.group_attr(queryset, groups)

    def group_attr(self, queryset, groups, pos=0):
        res = {}
        if pos == len(groups):
            return len(queryset)
        group = groups[pos]
        inner_group = self.explode_set_by_group(queryset, group)
        for k, v in inner_group.items():
            res[k] = self.group_attr(v, groups, pos+1)
        return res

    def explode_set_by_group(self, s, group):
        from collections import defaultdict
        d = defaultdict(set)
        for item in s:
            d[getattr(self.interface.inventory.inventory[item], group, None)].add(item)
        return d
