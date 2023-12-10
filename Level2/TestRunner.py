from BaseTestSuite import BaseTestSuite
from TestDriverController import TestDriverController

class TestRunner():
    @staticmethod    
    def run_precondition(pre_condition):
        test_items = pre_condition['test_items']
        for test_item in test_items:
            TestDriverController.perform_test(test_item)

    @staticmethod
    def test(test_suite: BaseTestSuite, test_name: str, double_checkpoint: bool = False):
        result = []
        test_data = test_suite.data
        
        pre1 = list(test_data.keys())[0] == 'precondition1'
        pre2 = list(test_data.keys())[1] == 'precondition2'
        start_scenario_idx = 2 if (pre1 and pre2) else 0
        
        for scenario in list(test_data.values())[start_scenario_idx:]:
            url = scenario['url']
            test_items = scenario['test_items']

            # Initialize setup
            TestDriverController.driver.get(url)
            TestDriverController.driver.set_window_size(784, 816)
            if test_suite.first_run:
                test_suite.first_run = False
                if start_scenario_idx:
                    TestRunner.run_precondition(list(test_data.values())[0])
            else:
                if start_scenario_idx:
                    TestRunner.run_precondition(list(test_data.values())[1])
            
            if not double_checkpoint:
                flag = False
                for test_item in test_items:
                    res = TestDriverController.perform_test(test_item)
                    if res is True: flag = True
                result.append(flag)
            else:
                flag1 = False
                flag2 = False
                for test_item in test_items:
                    res = TestDriverController.perform_test(test_item)
                    if res is True: 
                        if flag1 is True:
                            flag2 = True
                        else:
                            flag1 = True
                result.append(flag1 and flag2)
        
        fail_test_name = []
        for i in range(0, len(result)):
            if not result[i]:
                fail_test_name.append(list(test_data.keys())[i])

        fail_test_name_str = 'FAILED:\n\t'+ '\n\t'.join(name for name in fail_test_name) if len(fail_test_name) != 0 else 'Fail testcase: None'
        print(f"""
        \n- Test {test_name} (Level 2) --\nPASSED: {result.count(True)}/{len(result)}\n{fail_test_name_str}\n
        """)

    @staticmethod
    def run(test_suite, test_name: str, double_checkpoint: bool = False):
        test_suite.setup_method(None)
        result = TestRunner.test(test_suite, test_name, double_checkpoint)
        test_suite.teardown_method(None)
        return result