class Tree:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def PrintTree(self, root):
        print(root.data)

        if root.left is not None:
            self.PrintTree(root.left)

        if root.right is not None:
            self.PrintTree(root.right)

    def printPath(self, path):
        result = ""
        for element in path:
            result += element + " -> "

        print(result[:len(result)-4])

    def find(self, root, looking, path=[]):
        path.append(root.data)

        if root.data == looking:
            self.printPath(path)
            return

        if root.left is not None:
            self.find(root.left, looking, path)

        if root.right is not None:
            self.find(root.right, looking, path)


t = Tree("Computer")
t.left = Tree("Pictures")
t.right = Tree("Documents")
t.left.left = Tree("Photo")
# t.PrintTree(t)

t.find(t, "Photo")
