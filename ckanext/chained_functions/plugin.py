# -*- coding: utf-8 -*-
import ckan.plugins as p
from ckan.plugins.toolkit import (auth_allow_anonymous_access,
                                  chained_auth_function,
                                  chained_action,
                                  side_effect_free,
                                  chained_helper
                                  )


class ChainedFunctionsPlugin(p.SingletonPlugin):
    p.implements(p.IAuthFunctions)
    p.implements(p.IActions)
    p.implements(p.ITemplateHelpers)

    def get_auth_functions(self):
        return {
            "user_show": user_show
        }

    def get_actions(self):
        return {
            "package_search": package_search
        }

    def get_helpers(self):
        return {
            "ckan_version": ckan_version
        }


@chained_auth_function
@auth_allow_anonymous_access
def user_show(next_auth, context, data_dict=None):
    return next_auth(context, data_dict)


@chained_action
@side_effect_free
def package_search(original_action, context, data_dict):
    return original_action(context, data_dict)


@chained_helper
def ckan_version(next_func, **kw):
    return next_func(**kw)


setattr(ckan_version, "some_attribute", "some_value")
