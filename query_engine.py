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
        group = q.get('groupedBy')  # single field for now
        groups = self.process_groupby(group, queryset)
        result[group] = groups
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

    def process_groupby(self, group, queryset):
        groups = self.index.get_group(group)
        for k, v in groups.items():
            groups[k] = len(queryset.intersection(v))
        return groups

    # def group_attr(self, queryset, group):
    #     qs = queryset
    #     res = {}
    #     for k, v in qs.items():
    #         res[k] = self.explode_set_by_group(v, group)
    #     return res
    #
    # def explode_set_by_group(self, s, group):
    #     from collections import defaultdict
    #     d = defaultdict(set)
    #     for item in s:
    #         d[getattr(item, group)].add(item)
    #     return d
