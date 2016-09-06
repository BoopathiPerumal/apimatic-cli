import shutil
import unittest
import argparse
from apimaticcli.sdk_generator import *

class TestSDKGenerator(unittest.TestCase):
    output_path = './SDKs'

    def setUp(self):
        if os.path.exists(TestSDKGenerator.output_path):
            shutil.rmtree(TestSDKGenerator.output_path)

    @unittest.skip("Enter key and then comment out this line.")
    def test_from_key(self):
        arguments = argparse.Namespace
        arguments.api_key = '<your api key>'
        arguments.platform = 'cs_portable_net_lib'
        arguments.output = TestSDKGenerator.output_path

        SDKGenerator.from_key(arguments)

        files = os.listdir(TestSDKGenerator.output_path)
        self.assertEqual(len(files), 1)
        self.assertTrue(files[0].endswith(".zip"))
        file_size = os.stat(os.path.join(TestSDKGenerator.output_path, files[0])).st_size
        self.assertGreater(file_size, 0)

    @unittest.skip("Enter credentials and then comment out this line.")
    def test_from_user_url(self):
        arguments = argparse.Namespace
        arguments.email = '<your email>'
        arguments.password = '<your password>'
        arguments.name = 'Duuuudes'
        arguments.platform = 'cs_portable_net_lib'
        arguments.output = TestSDKGenerator.output_path
        arguments.url = 'https://raw.githubusercontent.com/DudeSolutions/DudeReportApi/4e4a9feee81be01dd61b4eedc7eaf93e2a92d0b4/apiary.apib'

        SDKGenerator.from_user(arguments)

        files = os.listdir(TestSDKGenerator.output_path)
        self.assertEqual(len(files), 1)
        self.assertTrue(files[0].endswith(".zip"))
        file_size = os.stat(os.path.join(TestSDKGenerator.output_path, files[0])).st_size
        self.assertGreater(file_size, 0)

    @unittest.skip("Enter credentials and then comment out this line.")
    def test_from_user_file(self):
        arguments = argparse.Namespace
        arguments.email = '<your email>'
        arguments.password = '<your password>'
        arguments.name = 'Calculator'
        arguments.platform = 'cs_portable_net_lib'
        arguments.output = TestSDKGenerator.output_path
        arguments.file = './tests/data/calculator.json'

        SDKGenerator.from_user(arguments)

        files = os.listdir(TestSDKGenerator.output_path)
        self.assertEqual(len(files), 1)
        self.assertTrue(files[0].endswith(".zip"))
        file_size = os.stat(os.path.join(TestSDKGenerator.output_path, files[0])).st_size
        self.assertGreater(file_size, 0)    	

    def tearDown(self):
        if os.path.exists(TestSDKGenerator.output_path):
            shutil.rmtree(TestSDKGenerator.output_path)