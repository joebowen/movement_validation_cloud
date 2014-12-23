from django.test import TestCase

class SimpleTest(TestCase):
    def test_Aspects(self):
        response = self.client.get('/Aspects/')
        self.assertEqual(response.status_code, 200)

        response = self.client.get('/Aspects/0/')
        self.assertEqual(response.status_code, 200)

    def test_Bodyparts(self):
        response = self.client.get('/Bodyparts/')
        self.assertEqual(response.status_code, 200)

        response = self.client.get('/Bodyparts/0/')
        self.assertEqual(response.status_code, 200)

    def test_Categories(self):
        response = self.client.get('/Categories/')
        self.assertEqual(response.status_code, 200)

        response = self.client.get('/Categories/0/')
        self.assertEqual(response.status_code, 200)

    def test_Computervisionalgorithms(self):
        response = self.client.get('/Computervisionalgorithms/')
        self.assertEqual(response.status_code, 200)

        response = self.client.get('/Computervisionalgorithms/0/')
        self.assertEqual(response.status_code, 200)

    def test_Directions(self):
        response = self.client.get('/Directions/')
        self.assertEqual(response.status_code, 200)

        response = self.client.get('/Directions/0/')
        self.assertEqual(response.status_code, 200)

    def test_Experimenters(self):
        response = self.client.get('/Experimenters/')
        self.assertEqual(response.status_code, 200)
        
        response = self.client.get('/Experimenters/0/')
        self.assertEqual(response.status_code, 200)

    def test_Featuresperplatewireframes(self):
        response = self.client.get('/Featuresperplatewireframes/')
        self.assertEqual(response.status_code, 200)
        
        response = self.client.get('/Featuresperplatewireframes/0/')
        self.assertEqual(response.status_code, 200)

    def test_Featuresperwormwireframes(self):
        response = self.client.get('/Featuresperwormwireframes/')
        self.assertEqual(response.status_code, 200)
        
        response = self.client.get('/Featuresperwormwireframes/0/')
        self.assertEqual(response.status_code, 200)

    def test_Histogramsperplatewireframes(self):
        response = self.client.get('/Histogramsperplatewireframes/')
        self.assertEqual(response.status_code, 200)
        
        response = self.client.get('/Histogramsperplatewireframes/0/')
        self.assertEqual(response.status_code, 200)

    def test_Histogramsperwormwireframes(self):
        response = self.client.get('/Histogramsperwormwireframes/')
        self.assertEqual(response.status_code, 200)
        
        response = self.client.get('/Histogramsperwormwireframes/0/')
        self.assertEqual(response.status_code, 200)

    def test_Labs(self):
        response = self.client.get('/Labs/')
        self.assertEqual(response.status_code, 200)
        
        response = self.client.get('/Labs/0/')
        self.assertEqual(response.status_code, 200)

    def test_Measurementsperwormwireframes(self):
        response = self.client.get('/Measurementsperwormwireframes/')
        self.assertEqual(response.status_code, 200)
        
        response = self.client.get('/Measurementsperwormwireframes/0/')
        self.assertEqual(response.status_code, 200)

    def test_Plates(self):
        response = self.client.get('/Plates/')
        self.assertEqual(response.status_code, 200)
        
        response = self.client.get('/Plates/0/')
        self.assertEqual(response.status_code, 200)

    def test_Platefeatures(self):
        response = self.client.get('/Platefeatures/')
        self.assertEqual(response.status_code, 200)
        
        response = self.client.get('/Platefeatures/0/')
        self.assertEqual(response.status_code, 200)

    def test_Platerawvideos(self):
        response = self.client.get('/Platerawvideos/')
        self.assertEqual(response.status_code, 200)
        
        response = self.client.get('/Platerawvideos/0/')
        self.assertEqual(response.status_code, 200)

    def test_Signs(self):
        response = self.client.get('/Signs/')
        self.assertEqual(response.status_code, 200)
        
        response = self.client.get('/Signs/0/')
        self.assertEqual(response.status_code, 200)

    def test_Videoattributes(self):
        response = self.client.get('/Videoattributes/')
        self.assertEqual(response.status_code, 200)
        
        response = self.client.get('/Videoattributes/0/')
        self.assertEqual(response.status_code, 200)

    def test_Worms(self):
        response = self.client.get('/Worms/')
        self.assertEqual(response.status_code, 200)
        
        response = self.client.get('/Worms/0/')
        self.assertEqual(response.status_code, 200)

    def test_Wormfeatures(self):
        response = self.client.get('/Wormfeatures/')
        self.assertEqual(response.status_code, 200)
        
        response = self.client.get('/Wormfeatures/0/')
        self.assertEqual(response.status_code, 200)

    def test_Worminteractions(self):
        response = self.client.get('/Worminteractions/')
        self.assertEqual(response.status_code, 200)
        
        response = self.client.get('/Worminteractions/0/')
        self.assertEqual(response.status_code, 200)

    def test_Wormlists(self):
        response = self.client.get('/Wormlists/')
        self.assertEqual(response.status_code, 200)
        
        response = self.client.get('/Wormlists/0/')
        self.assertEqual(response.status_code, 200)

    def test_Wormmeasurements(self):
        response = self.client.get('/Wormmeasurements/')
        self.assertEqual(response.status_code, 200)
        
        response = self.client.get('/Wormmeasurements/0/')
        self.assertEqual(response.status_code, 200)

    def test_Wormwireframevideos(self):
        response = self.client.get('/Wormwireframevideos/')
        self.assertEqual(response.status_code, 200)
        
        response = self.client.get('/Wormwireframevideos/0/')
        self.assertEqual(response.status_code, 200)

