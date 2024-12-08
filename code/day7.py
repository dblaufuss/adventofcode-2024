data = []

with open("data\\day7.txt", "r") as f:
    for line in f.readlines():
        data.append([int(line.split(":")[0]), tuple(int(x) for x in line.split()[1:])])

class TreeNode:
    def __init__(self, val=None, left=None, middle=None, right=None):
        self.val = val
        self.left = left
        self.middle = middle
        self.right = right

def createTree(nums: list) -> TreeNode:
    queue = []
    depth = len(nums)-1

    i = 0
    root = TreeNode(nums[i])
    queue.append(root)

    while len(queue) > 0:
        size = len(queue)
        i += 1

        if i > depth:
            break
        else:
            for j in range(size):
                node = queue.pop(0)
                node.left = TreeNode(node.val*nums[i])
                node.middle = TreeNode(int(f"{node.val}{nums[i]}"))
                node.right = TreeNode(node.val+nums[i])

                queue.append(node.left)
                queue.append(node.middle)
                queue.append(node.right)

    return root

def leafNodes1(root: TreeNode) -> set:
    nodes = set()
    if not root.left and not root.right:
        nodes.add(root.val)
    else:
        nodes.update(leafNodes1(root.right))
        nodes.update(leafNodes1(root.left))
    return nodes

def leafNodes2(root: TreeNode) -> set:
    nodes = set()
    if not root.left and not root.right and not root.middle:
        nodes.add(root.val)
    else:
        nodes.update(leafNodes2(root.right))
        nodes.update(leafNodes2(root.middle))
        nodes.update(leafNodes2(root.left))
    return nodes

total1 = 0
total2 = 0

for row in data:
    print(row)
    tree = createTree(row[1])
    if row[0] in leafNodes1(tree):
        total1 += row[0]
    
    if row[0] in leafNodes2(tree):
        total2 += row[0]

print("Part 1:", total1)
print("Part 2:", total2)