from hstest import StageTest, TestCase, CheckResult
from hstest.stage_test import List

class XMassTreeTest4(StageTest):

#    def generate(self) -> List[TestCase]:
#        return [TestCase(time_limit=1000000)]#
    def check(self, reply: str):

        if len(reply) == 0:
            return CheckResult.wrong("No output was printed!")

        #reply = float(reply)
        #tolerance = 0.1

        # Getting the student's results from the reply

        #if tolerance:
        #    if not (abs((reply - true_data) / true_data) < tolerance):
        #        return CheckResult.wrong('Incorrect value.')

        return CheckResult.correct()
