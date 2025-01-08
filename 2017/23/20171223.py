from collections import Counter, defaultdict
import sys


program = []
profile = Counter()


class Registers(defaultdict):
    def __init__(self, default_factory=None, *args, **kwargs):
        super().__init__(default_factory, *args, **kwargs)

    def r_value(self, key):
        return self.get(key) if key in "abcdefgh" else int(key)


class Program:
    def __init__(self, program: list[list[str]], debug: bool = False):
        self.program = program
        self.IP = 0
        self.registers = Registers(int)
        if debug:
            self.registers["a"] = 1
        self.invocations = 0

    def run(self):
        profile = Counter()

        try:
            while self.IP < len(self.program):
                profile[self.IP] += 1
                print(
                    f"IP = {self.IP}, instruction = {self.program[self.IP]}, registers = {self.registers}"
                )
                match self.program[self.IP]:
                    case "set", x, y:
                        self.registers[x] = self.registers.r_value(y)
                        self.IP += 1
                    case "sub", x, y:
                        self.registers[x] -= self.registers.r_value(y)
                        self.IP += 1
                    case "mul", x, y:
                        self.registers[x] *= self.registers.r_value(y)
                        self.invocations += 1
                        self.IP += 1
                    case "jnz", x, y:
                        if self.registers.r_value(x) != 0:
                            self.IP += self.registers.r_value(y)
                        else:
                            self.IP += 1
                    case _:
                        print(f"No match for {self.program[self.IP]}")
                        self.IP += 1
        except KeyboardInterrupt:
            print(profile)
        print(profile)


with open(sys.argv[1], "r") as file:
    for line in file:
        program.append(line.strip().split())


P = Program(program)
P.run()
print(f"Part 1: mul was invoked {P.invocations} times.")

P = Program(program, debug=True)
P.run()
print(f"Part 2: The value in register h is {P.registers["h"]}")
