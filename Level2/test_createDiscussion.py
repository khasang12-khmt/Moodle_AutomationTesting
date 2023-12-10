from BaseTestSuite import BaseTestSuite
from TestRunner import TestRunner

createDiscussionTestSuite = BaseTestSuite('./input/input_CreateDiscussion.json')
TestRunner.run(createDiscussionTestSuite,"Create Discussion To Course")