#
# Copyright (c) 2001 Bizar Software Pty Ltd (http://www.bizarsoftware.com.au/)
# This module is free software, and you may redistribute it and/or modify
# under the same terms as Python, so long as this copyright message and
# disclaimer are retained in their original form.
#
# IN NO EVENT SHALL BIZAR SOFTWARE PTY LTD BE LIABLE TO ANY PARTY FOR
# DIRECT, INDIRECT, SPECIAL, INCIDENTAL, OR CONSEQUENTIAL DAMAGES ARISING
# OUT OF THE USE OF THIS CODE, EVEN IF THE AUTHOR HAS BEEN ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
#
# BIZAR SOFTWARE PTY LTD SPECIFICALLY DISCLAIMS ANY WARRANTIES, INCLUDING,
# BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE.  THE CODE PROVIDED HEREUNDER IS ON AN "AS IS"
# BASIS, AND THERE IS NO OBLIGATION WHATSOEVER TO PROVIDE MAINTENANCE,
# SUPPORT, UPDATES, ENHANCEMENTS, OR MODIFICATIONS.
# 
# $Id: test_anydbm.py,v 1.3 2004-03-18 01:58:46 richard Exp $ 

import unittest, os, shutil, time

from db_test_base import DBTest, ROTest, SchemaTest, ClassicInitTest, config

class anydbmOpener:
    from roundup.backends import anydbm as module

    def nuke_database(self):
        shutil.rmtree(config.DATABASE)

class anydbmDBTest(anydbmOpener, DBTest):
    pass

class anydbmROTest(anydbmOpener, ROTest):
    pass

class anydbmSchemaTest(anydbmOpener, SchemaTest):
    pass

class anydbmClassicInitTest(ClassicInitTest):
    backend = 'anydbm'

from session_common import DBMTest
class anydbmSessionTest(anydbmOpener, DBMTest):
    pass

def test_suite():
    suite = unittest.TestSuite()
    print 'Including anydbm tests'
    suite.addTest(unittest.makeSuite(anydbmDBTest))
    suite.addTest(unittest.makeSuite(anydbmROTest))
    suite.addTest(unittest.makeSuite(anydbmSchemaTest))
    suite.addTest(unittest.makeSuite(anydbmClassicInitTest))
    suite.addTest(unittest.makeSuite(anydbmSessionTest))
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    unittest.main(testRunner=runner)


# vim: set filetype=python ts=4 sw=4 et si
