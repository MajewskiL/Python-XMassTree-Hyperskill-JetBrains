from hstest import StageTest, TestCase, CheckResult
from hstest.stage_test import List

#  !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#  Programa działać tak, że jak jest para liczb, to rysyje drzewo,
#  a jak lista to rysuje kartkę. Pozowli to sprawdzić, czy nie namieszali
#  nic od stage3. Kartal będzie sprawdzana czy zgadza się wymiar, czy jest napis
#  w opowiedniej linii, a reszta jako funkcja hashująca. Czyli testy mogą wypluć
#  że któraś choinka źle się rysuje, że jest niepoprawna wielkość kartki,
#  że napis jest nie w tym miejscu co trzeba i że ułożenie choinek jest złe.

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
