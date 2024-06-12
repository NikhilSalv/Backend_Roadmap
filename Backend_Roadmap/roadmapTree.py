class Tree:
    def __init__(self, root):
        self.root = root
        self.children = []
        self.parent = None

    def insert_child(self,child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        p = self.parent
        level = 0
        while p:
            level += 1
            p = p.parent
        return level

    def print_tree(self):
        spaces = " "*self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + self.root)
        if self.children:
            for child in self.children:
                child.print_tree()



def build_tree():
    tree = Tree("Back-End Developer")

    security = Tree("security")
    security.insert_child(Tree("sql_Injection"))
    security.insert_child(Tree("csrf"))
    security.insert_child(Tree("authentication"))
    security.insert_child(Tree("authorization"))
    security.insert_child(Tree("xss"))


    database = Tree("dabatase")
    database.insert_child(Tree("ACID"))
    database.insert_child(Tree("normalisation"))
    database.insert_child(Tree("ORM"))

    performance = Tree("performance")
    performance.insert_child(Tree("load_balancing"))
    performance.insert_child(Tree("caching"))


    tree.insert_child(security)
    tree.insert_child(database)
    tree.insert_child(performance)

    print(security.children[0].get_level())
    # print(cellphones.children[2].root)


    return tree

if __name__ == "__main__":
    tree = build_tree()
    tree.print_tree()

    pass