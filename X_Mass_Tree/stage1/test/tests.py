from hstest import StageTest, CheckResult, dynamic_test, TestedProgram
from hstest.stage_test import List
from random import randint


class XMassTreeTest1(StageTest):

    @staticmethod
    def output_len_stage1(out, high):
        out_len = len(out.splitlines())
        if out_len != int(high):
            return f"Wrong tree high. Expected {high}, founded {out_len}."

    @staticmethod
    def output_stars_stage1(out, high):
        out_stars = out.count("*")
        exp_stars = sum([2 * n + 1 for n in range(int(high))])
        if out_stars != exp_stars:
            return f"Wrong number of '*'. Expected {exp_stars}, founded {out_stars}."
        return

    @staticmethod
    def output_pos_stage1(out, high):
        out = out.splitlines()
        out_pos = [n.index("*") for n in out]
        exp_pos = [int(high - n - 1) for n in range(high)]
        for i, value in enumerate(out_pos):
            if value != exp_pos[i]:
                return f"Wrong position of '*' in line {i}. Expected {exp_pos[i]}, founded {value}."
        return

    @dynamic_test
    def test1(self):
        high = str(randint(3, 30))
        # high = '3'
        main = TestedProgram()
        main.start()
        output = main.execute(high)
        check = self.output_stars_stage1(output, high)
        if check:
            return CheckResult.wrong(check)
        check = self.output_len_stage1(output, high)
        if check:
            return CheckResult.wrong(check)
        check = self.output_pos_stage1(output, int(high))
        if check:
            return CheckResult.wrong(check)

#    if len(reply) == 0:
#        return CheckResult.wrong("No output was printed!")

        #reply = float(reply)
        #tolerance = 0.1

        # Getting the student's results from the reply

        #if tolerance:
        #    if not (abs((reply - true_data) / true_data) < tolerance):
        #        return CheckResult.wrong('Incorrect value.')

        return CheckResult.correct()
