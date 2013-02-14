from __future__ import absolute_import
import django_statsd

try:
    import pyelasticsearch

    class StatsdElasticSearch(pyelasticsearch.ElasticSearch):
        def search(self, *args, **kwargs):
            with django_statsd.with_('pyelasticsearch.search'):
                return origElasticSearch.search(self, *args, **kwargs)

    origElasticSearch = None
    if not issubclass(pyelasticsearch.ElasticSearch, StatsdElasticSearch):
        origElasticSearch = pyelasticsearch.ElasticSearch
        pyelasticsearch.ElasticSearch = StatsdElasticSearch
except ImportError:
    pass
