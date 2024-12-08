data = []

with open("data\\day7_test.txt", "r") as f:
    for line in f.readlines():
        data.append([int(line.split(":")[0]), tuple(int(x) for x in line.split()[1:])])

class TreeNode:
    def __init__(self, val=None, left=None, middle=None, right=None):
        self.val = val
        self.left = left
        self.middle = middle
        self.right = right

def createTree(nums: list, target: int) -> TreeNode:
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
                if node.val*nums[i] <= target:
                    node.left = TreeNode(node.val*nums[i])
                    queue.append(node.left)

                if int(f"{node.val}{nums[i]}") <= target:
                    node.middle = TreeNode(int(f"{node.val}{nums[i]}"))
                    queue.append(node.middle)

                if node.val+nums[i] <= target:
                    node.right = TreeNode(node.val+nums[i])
                    queue.append(node.right)

    return root

def leafNodes1(root: TreeNode) -> list:
    nodes = []
    if not root.left and not root.right:
        nodes.append(root.val)
    if root.left:
        nodes.extend(leafNodes1(root.left))
    if root.right:
        nodes.extend(leafNodes1(root.right))
    return nodes

def leafNodes2(root: TreeNode) -> list:
    nodes = []
    if not root.left and not root.right and not root.middle:
        nodes.append(root.val)
    if root.left:
        nodes.extend(leafNodes2(root.left))
    if root.middle:
        nodes.extend(leafNodes2(root.middle))
    if root.right:
        nodes.extend(leafNodes2(root.right))
    return nodes

total1 = 0
total2 = 0

for row in data:
    print(row)
    tree = createTree(row[1], row[0])
    if row[0] in leafNodes1(tree):
        total1 += row[0]
    
    if row[0] in leafNodes2(tree):
        total2 += row[0]

print("Part 1:", total1)
print("Part 2:", total2)