"""importing unittest"""
import unittest
from app import app

class FlaskTestCase(unittest.TestCase):
    """testing class"""
    def test_index_page_loads(self):
        """making sure we set up Flask the correct way"""
        sampletest = app.test_client(self)
        response = sampletest.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_index_page(self):
        """make sure the homepage loads with correct content"""
        sampletest = app.test_client(self).get('/', content_type='html/text')
        self.assertTrue(b'Welcome' in sampletest.data)

    def test_successful_registration(self):
        """to make sure registration passes"""
        sampletest = app.test_client(self)
        response = sampletest.post('/index', data=dict(name="kariser",
                                                        username="kariser",
                                                        password="karis123", 
                                                        confirm_password="karis123"),
                                   follow_redirects=True)
        self.assertTrue('Bucket' in response.data)

    def test_login_passes(self):
        """ensuring that login passes as expected"""
        sampletest = app.test_client(self)
        response = sampletest.post('/login', data=dict(username="username",
                                                       password="password"),
                                   follow_redirects=True)
        self.assertTrue('Bucket' in response.data)

    def test_bucketlist_creation(self):
        """ensure bucketlist creation works correctly"""
        sampletest = app.test_client(self)
        response = sampletest.post('/bucketlist', data=dict(bucketlist="Another one"),
                                   follow_redirects=True)
        self.assertFalse(b'Another one' in response.data)


    def test_delete_bucketlist(self):
        """ensuring deletion of a bucketlist works"""
        sampletest = app.test_client(self)
        response = sampletest.post('/deletebucketlist', data=dict(item='1'),
                                   follow_redirects=True)
        self.assertFalse("SomeItem" in response.data)

    def test_delete_bucketlist_item(self):
        """making sure items get deleted from a bucketlist"""
        sampletest = app.test_client(self)
        response = sampletest.post('/deletebucketlistitems', data=dict(item='1'),
                                   follow_redirects=True)
        self.assertFalse('SomeItem' in response.data)


if __name__ == '__main__':
    unittest.main()
