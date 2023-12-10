from BaseTestSuite import BaseTestSuite


class TestRunner():
    @staticmethod
    def test(test_suite: BaseTestSuite, test_name: str):
        test_list = []
        # Get all attributes of the instance (including methods)
        all_attributes = dir(test_suite)
        # Filter and run methods starting with "test"
        for attr in all_attributes:
            if attr.startswith("test") and callable(getattr(test_suite, attr)):
                # Call the method
                test_list.append(getattr(test_suite, attr))
            
        result = []
        for test in test_list:
            result.append(test())
        fail_test_name = []
        for i in range(0, len(result)):
            if not result[i]:
                fail_test_name.append(test_list[i].__name__)

        fail_test_name_str = 'FAILED:\n\t'+ '\n\t'.join(name for name in fail_test_name) if len(fail_test_name) != 0 else 'Fail testcase: None'
        print(f"""
        \n- Test {test_name} (Level 0)--\nPASSED: {result.count(True)}/{len(result)}\n{fail_test_name_str}\n
        """)

    @staticmethod
    def run(test_suite, test_name):
        test_suite.setup_method(None)
        result = TestRunner.test(test_suite, test_name)
        test_suite.teardown_method(None)
        return result