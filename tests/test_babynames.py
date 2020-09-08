#!/usr/bin/env python
# -*- coding: utf-8 -*-
# flake8: noqa
"""
A Test fixture for babynames.

NOTE: Students should not modify this file.
"""
__author__ = "madarp"

import sys
import os
import glob
import unittest
import subprocess
import importlib
from contextlib import redirect_stdout
from io import StringIO


# Kenzie devs: change this to 'soln.wordcount' to test solution
PKG_NAME = 'babynames'


class TestBabynames(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Performs module import and suite setup at test-runtime"""
        # check for python3
        cls.assertGreaterEqual(cls, sys.version_info[0], 3)
        # This will import the module to be tested
        cls.module = importlib.import_module(PKG_NAME)

    def get_summary_file_as_list(self, summary_file):
        """Helper function for loading a summary file as a list"""
        with open(summary_file) as sf:
            summary_list = sf.read().splitlines()
            # Remove empty strings
            summary_list = list(filter(None, summary_list))
            return summary_list

    def remove_extension_files(self, ext):
        """Removes all files in cwd with given extension"""
        for f in glob.glob('*' + ext):
            os.remove(f)

    def test_main_print(self):
        """Check if babynames.main() prints output list"""
        self.remove_extension_files('.summary')

        buffer = StringIO()
        with redirect_stdout(buffer):
            self.module.main(['baby1990.html'])
            output = buffer.getvalue().splitlines()
        self.assertIsInstance(output, list)

        # Compare captured output to list from file
        baby1990_list = self.get_summary_file_as_list(
            os.path.join('tests', 'baby1990.html.summary')
        )
        self.assertListEqual(output, baby1990_list)

        # Also check that no summary file was created
        self.assertFalse(
            glob.glob('*.summary'),
            msg='A summary file should not be created. Just printing.'
        )

    def test_main_summary(self):
        """Check if babynames.main() creates summary files"""
        # First remove any existing summary files
        self.remove_extension_files('.summary')
        cmdline = ['--summaryfile']
        cmdline.extend(glob.glob('baby*.html'))
        self.module.main(cmdline)
        files = glob.glob('*.summary')
        self.assertEqual(len(files), 10)

    def test_create_parser(self):
        """Check if parser can parse args"""
        p = self.module.create_parser()
        test_args = ['dummyfile1', 'dummyfile2', '--summaryfile']
        ns = p.parse_args(test_args)
        self.assertEqual(len(ns.files), 2)
        self.assertTrue(ns.summaryfile)

    def test_extract_names(self):
        """Checking extraction, alphabetizing, de-duping, ranking of names from all html files"""
        # Is the function callable?
        self.assertTrue(
            callable(self.module.extract_names),
            msg="The extract_names function is missing"
            )

        # Get list of only html files
        html_file_list = sorted(filter(lambda f: f.endswith('.html'), os.listdir('.')))
        # Compare each result (actual) list to expected list.
        for f in html_file_list:
            summary_file = os.path.join('tests', f + '.summary')
            expected_list = self.get_summary_file_as_list(summary_file)
            actual_list = self.module.extract_names(f)
            self.assertIsInstance(actual_list, list)
            # Remove empty strings before comparing
            actual_list = list(filter(None, actual_list))
            # This will perform element-by-element comparison.
            self.assertListEqual(actual_list, expected_list)

    def test_flake8(self):
        """Checking for PEP8/flake8 compliance"""
        result = subprocess.run(['flake8', self.module.__file__])
        self.assertEqual(result.returncode, 0)

    def test_author_string(self):
        """Checking for __author__ string"""
        self.assertNotEqual(self.module.__author__, '???')


if __name__ == '__main__':
    unittest.main()
