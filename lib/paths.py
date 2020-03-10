from abc import ABC, abstractmethod


class AbstractPathEntry(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def register(self, app):
        pass


class URLPathEntry(AbstractPathEntry):
    def __init__(self,
                 rule,
                 endpoint,
                 view_func,
                 provide_automatic_options,
                 options):
        self.__rule = rule
        self.__endpoint = endpoint
        self.__view_func = view_func
        self.__provide_automatic_options = provide_automatic_options
        self.__options = options

    def register(self, app):
        app.add_url_rule(self.__rule,
                         self.__endpoint,
                         self.__view_func,
                         self.__provide_automatic_options,
                         **self.__options)



class BlueprintPathEntry(AbstractPathEntry):
    def __init__(self, blueprint, options):
        self.__blueprint = blueprint
        self.__options = options

    def register(self, app):
        app.register_blueprint(self.__blueprint,
                               **self.__options)


def blueprint(bp, **options):
    return BlueprintPathEntry(bp, options)


def url(rule, endpoint=None, view_func=None, provide_automatic_options=None,
        **options):
    return URLPathEntry(rule, endpoint, view_func, provide_automatic_options,
                        options)
