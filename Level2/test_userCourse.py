from BaseTestSuite import BaseTestSuite
from TestRunner import TestRunner

userCourseTestSuite = BaseTestSuite('./input/input_UserCourse.json')
TestRunner.run(userCourseTestSuite,"Add User To Course")