from ansible import utils, errors
import httplib2

class LookupModule(object):

    def __init__(self, basedir=None, **kwargs):
        self.basedir = basedir

    def run(self, terms, inject=None, **kwargs):
        terms = utils.listify_lookup_plugin_terms(terms, self.basedir, inject)
        ret = []

        h = httplib2.Http()

        for term in terms:
            url = 'https://github.com/' + term + '.keys'
            response, content = h.request(url, method='GET')
            ret.append(content)

        return ret
