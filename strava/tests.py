from django.test import TestCase

''' 

Something like this

def test_analysis(self):
    test_activities = other_file.test_activity_data
    analysis_service = Analysis()
    analysis = analysis_service.get_analysis(test_activities)
    expected_average = some_number
    assert_true(expected_average = analysis.average)


    with open("test.json") as jsonFile:
        jsonObject = json.load(jsonFile)
        jsonFile.close()

'''