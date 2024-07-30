import pytest

# Define a list of scenarios
scenarios = ["ScenarioA", "ScenarioB", "ScenarioC"]


# Parametrize a single test function to run for each scenario
@pytest.mark.parametrize("scenario", scenarios)
class TestScenarios:
    def test_case_1(self, scenario):
        assert True

    def test_case_2(self, scenario):
        assert True

    def test_case_3(self, scenario):
        assert True


# class TestScenarioA:
#     def test_case_1(self):
#         assert True

#     def test_case_2(self):
#         assert True

#     def test_case_3(self):
#         assert True


# class TestScenarioB:
#     def test_case_1(self):
#         assert True

#     def test_case_2(self):
#         assert True

#     def test_case_3(self):
#         assert True


# class TestScenarioC:
#     def test_case_1(self):
#         assert True

#     def test_case_2(self):
#         assert True

#     def test_case_3(self):
#         assert True
