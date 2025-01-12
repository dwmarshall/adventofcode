import sys


class Node:
    def __init__(self, input: list[int]):
        child_quantity = input[0]
        metadata_quantity = input[1]

        self.children = []
        self.metadata = []
        self.length = 2
        for _ in range(child_quantity):
            child = Node(input[self.length :])
            self.length += child.length
            self.children.append(child)
        for _ in range(metadata_quantity):
            self.metadata.append(input[self.length])
            self.length += 1

    def metadata_sum(self) -> int:
        m_sum = 0
        if self.children:
            m_sum = sum(x.metadata_sum() for x in self.children)
        if self.metadata:
            m_sum += sum(self.metadata)
        return m_sum

    def value(self) -> int:
        result = 0
        if self.children:
            for i in self.metadata:
                if i <= len(self.children):
                    result += self.children[i - 1].value()
        elif self.metadata:
            result = sum(self.metadata)
        return result


with open(sys.argv[1], "r") as file:
    input = list(map(int, file.read().split()))

top_node = Node(input)

print(f"Part 1: The metadata sum is {top_node.metadata_sum()}")
print(f"Part 2: The value of the root node is {top_node.value()}")
