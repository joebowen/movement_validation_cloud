from django.test import TestCase
from django.db.models import get_app, get_models

class SimpleTest(TestCase):
    def get_urls(raw_urls, urlbase=''):
        '''Recursively builds a list of all the urls in the current project and the name of their associated view'''
        from operator import itemgetter
        nice_urls = []
        app = get_app('Openworm')
        for model in get_models(app):
            nice_urls.append({"pattern": model().get_subclass_name()})
        nice_urls = sorted(nice_urls, key=itemgetter('pattern')) #sort alphabetically
        return nice_urls

    def test_dashboard(self):
        from Openworm.urls import urlpatterns #this import should be inside the function to avoid an import loop
        nice_urls = self.get_urls(urlpatterns)

        for url in nice_urls:
            response = self.client.get('/dashboard/'+url['pattern']+'/')
            self.assertEqual(response.status_code, 200)

    def test_api(self):
        from Openworm.urls import urlpatterns #this import should be inside the function to avoid an import loop
        nice_urls = self.get_urls(urlpatterns)

        for url in nice_urls:
            response = self.client.get('/api/'+url['pattern']+'/')
            self.assertEqual(response.status_code, 200)

            response = self.client.get('/api/'+url['pattern']+'/0/')
            self.assertEqual(response.status_code, 200)