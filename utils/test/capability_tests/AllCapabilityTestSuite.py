# coding: utf-8
'''
-----------------------------------------------------------------------------
Copyright 2015 Esri
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

  http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
-----------------------------------------------------------------------------

==================================================
AllCapabilityTestSuite.py
--------------------------------------------------
requirments:
* ArcGIS Desktop 10.X+ or ArcGIS Pro 1.X+
* Python 2.7 or Python 3.4
author: ArcGIS Solutions
company: Esri
==================================================
description:
This test suite collects all of the capability toolbox test suites:
* HelicopterLandingZoneToolsTestSuite.py
* ERGToolsTestSuite.py
* PointOfOriginToolsTestSuite.py

==================================================
history:
10/23/2015 - MF - placeholder
==================================================
'''

import unittest
import HelicopterLandingZoneToolsTestSuite
#import PointOfOriginToolsTestSuite
#import ERGToolsTestSuite

class AllCapabilityTestSuite():
    ''' This class is a test suite collecting all of the capability toolbox test suites '''

    def capabilityTestSuite(self, testSuite, logger, platform):
        ''' This pulls together all of the toolbox test suites in this folder '''
        print("   AllCapabilityTestSuite.capabilityTestSuite")
        logger.info("Capability Tests...")
        hlz = HelicopterLandingZoneToolsTestSuite.HelicopterLandingZoneTestSuite
        hlz.runHLZTestSuite(hlz, testSuite, logger, platform)

        #TODO: Add PointOfOriginTestSuite
        #TODO: Add ERGToolsTestSuite
        return testSuite
