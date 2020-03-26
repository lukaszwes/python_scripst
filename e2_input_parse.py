# Format following input_text
# success_ratio =  # 99+65+0+99 / 4


input_text = '''[gw0] [ 99%] PASSED utilities/test/unit_tests/test_path_resolver.py::TestObjectPathResolver::test_not_property_path 
utilities/test/unit_tests/test_path_resolver.py::TestObjectPathResolver::test_resolving_one_underscore 
[gw0] [ 65%] FAILED utilities/test/unit_tests/test_path_resolver.py::TestObjectPathResolver::test_resolving_one_underscore 
utilities/test/unit_tests/test_path_resolver.py::TestObjectPathResolver::test_resolving_without_underscore 
[gw0] [ 0%] SKIPPED utilities/test/unit_tests/test_path_resolver.py::TestObjectPathResolver::test_resolving_without_underscore 
[gw2] [ 99%] PASSED ute_apis/test/unit_tests/test_signal_handlers.py::UTESignalHanlersTestCase::test_suspend_test_instance
'''


def main():
    result = {}

    logs = input_text.split('\n')
    list_test = []
    list_passed = []
#    list_failed = []
    list_skipped = []
    list_error = []
    list_ratio = []

    for RESULT in logs:
        if 'PASSED' in RESULT:
            passed = RESULT.split('::')
            list_passed.append(passed[-2] + '--->' + passed[-1])
            list_ratio.append((((passed[0]).split('%]'))[0])[-2:])      #get % value, the same method will be used for "failed" and "skipped" log lines
        elif 'FAILED' in RESULT:
            failed = RESULT.split('::')
            #list_failed.append(failed[-2] + '--->' + failed[-1])       #list_failed is not used in our case but can be useful in future
            list_ratio.append((((failed[0]).split('%]'))[0])[-2:])
        elif 'SKIPPED' in RESULT:
            skipped = RESULT.split('::')
            list_skipped.append(skipped[-2] + '--->' + skipped[-1])
            list_ratio.append((((skipped[0]).split('%]'))[0])[-2:])
        else:
            if '::' in RESULT:                                          #additional condition due to empty element '' in logs table
                error = RESULT.split('::')
                list_error.append(error[-2] + '--->' + error[-1])

    for i in range (0 , len(list_ratio)):                               #string->intiger conversion in list_ratio
                    list_ratio[i] = int(list_ratio[i])
                    
    success_ratio = sum(list_ratio)/len(list_ratio)

    result = str({
              'success_ratio': success_ratio,
              'total_tests'  : len(list_ratio),
              'errors'  : list_error,
              'passed'  : list_passed,
              'skipped' : list_skipped
              })

    #Formatting to expected layout
    result = result.replace("'success_ratio'","\n\t 'success_ratio'")
    result = result.replace("'total_tests'","\n\t 'total_tests'")
    result = result.replace("'errors'","\n\t 'errors'")
    result = result.replace("'passed'","\n\t 'passed'")
    result = result.replace("'skipped'","\n\t 'skipped'")

    return result


if __name__ == '__main__':
    print('Result: ', main())
    # print 'Result: ', main()  # --> Python 2.7+



'''
EXAMPLE OUTPUT

>> python e2_input_parse.py


-->
Result: {
        'success_ratio': 65.75,    
        'total_tests': 4,
        'errors': ['TestObjectPathResolver--->test_resolving_one_underscore'],
        'passed': ['UTESignalHanlersTestCase--->test_suspend_test_instance', 'TestObjectPathResolver--->test_not_property_path'],
        'skipped': ['UTESignalHanlersTestCase--->test_resolving_without_underscore']
}
    




'''
