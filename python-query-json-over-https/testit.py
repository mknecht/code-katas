#!/usr/bin/env python
import argparse
import os.path
import unittest
import subprocess
import sys


_URL = "https://www.reviewboard.org/api/store/categories/"
scriptname = None


class ReferenceTests(unittest.TestCase):
    def test_chaining(self):
        result = self._get_result_for_query('links.self.method')
        self.assertEqual(result, "u'GET'\n")

    def test_with_index(self):
        result = self._get_result_for_query('store_categories[0].name')
        self.assertEqual(result, "u'Extensions'\n")

    def _get_result_for_query(self, query):
        global scriptname
        global _URL
        cmd = [
            "python",
            scriptname,
            _URL,
            query,
        ]
        return subprocess.check_output(
            cmd,
        )


def getargs():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--solution",
        default="solution.py",
        help="Filename of the script to test",
    )
    return parser.parse_args()


def set_scriptname(given):
    global scriptname
    scriptname = given
    if not os.path.exists(given):
        raise ValueError("{} does not exist. Start coding! :)".format(given))


def main(args):
    set_scriptname(args.solution)
    unittest.main(argv=[sys.argv[0]])
    return 0


if __name__ == '__main__':
    sys.exit(main(getargs()))
