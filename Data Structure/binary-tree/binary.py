class TreeNode:
    def __init__(self,val):
        self.val = val
        self.nodesRight = None
        self.nodesLeft = None

    #         R
    #        / \
    #       A   B
    #      / \ / \
    #     C  D E  F
    #    /
    #   G 

root = TreeNode('R')
nodeA = TreeNode('A')
nodeB = TreeNode('B')
nodeC = TreeNode('C')
nodeD = TreeNode('D')
nodeE = TreeNode('E')
nodeF = TreeNode('F')
nodeG = TreeNode('G')

root.nodesLeft = nodeA
root.nodesRight = nodeB

nodeA.nodesLeft = nodeC
nodeA.nodesRight = nodeD

nodeB.nodesLeft = nodeE
nodeB.nodesRight = nodeF

nodeC.nodesLeft = nodeG

print(root.nodesRight.nodesRight.val) #F
print(root.nodesLeft.nodesLeft.nodesLeft.val) 