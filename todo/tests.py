from django.test import TestCase

# Create your tests here.
class SampleTestCase(TestCase):
    def test_sample1(self):
        self.assetEqual(1 + 2, 3)