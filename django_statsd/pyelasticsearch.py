# from __future__ import absolute_import
# from django_statsd.utils import get_timer
# import django_statsd

# try:
#     import pyelasticsearch

#     class StatsdElasticSearch(pyelasticsearch.ElasticSearch):
#         def search(self, *args, **kwargs):
#             timer = get_timer('totals.pyelasticsearch')
#             timer.start()
#             with django_statsd.with_('pyelasticsearch.search'):
#                 result = origElasticSearch.search(self, *args, **kwargs)
#             timer.stop()
#             return result

#     origElasticSearch = None
#     if not issubclass(pyelasticsearch.ElasticSearch, StatsdElasticSearch):
#         origElasticSearch = pyelasticsearch.ElasticSearch
#         pyelasticsearch.ElasticSearch = StatsdElasticSearch
# except ImportError:
#     pass
