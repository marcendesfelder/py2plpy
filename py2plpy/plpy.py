class Plpy:
    def __init__(self):
        pass
    def execute(self, queryOrPlan, arguments=[], max_rows=-1):
        return []
    def prepare(self, query, argtypes=[]):
        return []
    def cursor(self, queryOrPlan, arguments=[]):
        return []
    def debug(self, msg, **kwargs):
        pass
    def log(self, msg, **kwargs):
        pass
    def info(self, msg, **kwargs):
        pass
    def notice(self, msg, **kwargs):
        pass
    def warning(self, msg, **kwargs):
        pass
    def error(self, msg, **kwargs):
        pass
    def fatal(self, msg, **kwargs):
        pass
    def commit(self):
        pass
    def rollback(self):
        pass

plpy = Plpy()