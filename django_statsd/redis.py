from __future__ import absolute_import
import django_statsd

try:
    import redis

    class StatsdRedis(redis.Redis):
        def execute_command(self, func_name, *args, **kwargs):
            django_statsd.start('totals.redis.%s' % func_name.lower())
            with django_statsd.with_('redis.%s' % func_name.lower()):
                result = origRedis.execute_command(self, func_name, *args,
                                                   **kwargs)
            django_statsd.stop('totals.redis.%s' % func_name.lower())
            return result

    origRedis = None
    # NOTE issubclass is true if both are the same class
    if not issubclass(redis.Redis, StatsdRedis):
        origRedis = redis.Redis
        redis.Redis = StatsdRedis
except ImportError:
    pass

