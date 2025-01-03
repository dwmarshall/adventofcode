from collections import defaultdict, deque
import sys

program = []


class Registers(defaultdict):
    def __init__(self, default_factory=None, *args, **kwargs):
        super().__init__(default_factory, *args, **kwargs)

    def r_value(self, key):
        return self.get(key) if key in self else int(key)


class Program:
    def __init__(self, id: int, program: list[list[str]]):
        self.id = id
        self.program = program
        self.q = deque()
        self.IP = 0
        self.registers = Registers(int)
        self.registers["p"] = id
        self.total_sends = 0
        self.last_sound = None

    def receive(self, message: int):
        self.q.append(message)

    def run(self, other: "Program" = None):
        while self.IP < len(self.program):
            # print(f"IP = {IP}, instruction = {p[IP]}, registers = {registers}")
            match self.program[self.IP]:
                case "snd", x:
                    if other is not None:
                        other.receive(self.registers.r_value(x))
                    self.last_sound = self.registers.r_value(x)
                    self.total_sends += 1
                    self.IP += 1
                case "set", x, y:
                    self.registers[x] = self.registers.r_value(y)
                    self.IP += 1
                case "add", x, y:
                    self.registers[x] += self.registers.r_value(y)
                    self.IP += 1
                case "mul", x, y:
                    self.registers[x] *= self.registers.r_value(y)
                    self.IP += 1
                case "mod", x, y:
                    self.registers[x] %= self.registers.r_value(y)
                    self.IP += 1
                case "rcv", x:
                    if other is None:
                        if self.registers.r_value(x) != 0:
                            return
                    elif self.q:
                        self.registers[x] = self.q.popleft()
                        self.IP += 1
                    else:
                        return
                case "jgz", x, y:
                    if self.registers.r_value(x) > 0:
                        self.IP += self.registers.r_value(y)
                    else:
                        self.IP += 1
                case _:
                    print(f"No match for {self.program[self.IP]}")
                    self.IP += 1


with open(sys.argv[1], "r") as file:
    for line in file:
        program.append(line.strip().split())


Px = Program(0, program)
Px.run(None)
print(f"Part 1: The last frequency played was {Px.last_sound}")

P0 = Program(0, program)
P1 = Program(1, program)

while True:
    P0.run(P1)
    P1.run(P0)
    if not (P0.q or P1.q):
        break

print(f"Part 2: P1 sent {P1.total_sends} messages.")
