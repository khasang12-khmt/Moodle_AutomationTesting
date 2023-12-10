from BaseTestSuite import BaseTestSuite
from TestRunner import TestRunner

responsiveTestSuite = BaseTestSuite('./input/input_Responsive.json')
TestRunner.run(responsiveTestSuite,"Responsive", True)
