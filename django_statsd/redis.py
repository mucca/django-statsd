# from __future__ import absolute_import
# from django_statsd.utils import get_timer
# import django_statsd


# try:
#     import redis

#     class StatsdRedis(redis.Redis):
#         def execute_command(self, func_name, *args, **kwargs):
#             timer = get_timer('totals.redis.%s' % func_name.lower())
#             timer.start()
#             with django_statsd.with_('redis.%s' % func_name.lower()):
#                 result = origRedis.execute_command(self, func_name, *args,
#                                                    **kwargs)
#             timer.stop()
#             return result

#     origRedis = None
#     # NOTE issubclass is true if both are the same class
#     if not issubclass(redis.Redis, StatsdRedis):
#         origRedis = redis.Redis
#         redis.Redis = StatsdRedis
# except ImportError:
#     pass

