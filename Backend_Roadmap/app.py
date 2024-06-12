from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

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


@app.route("/")
def index():

    return render_template("index.html")

@app.route("/buildtree")
def buildTree(name,parent,root):
    pass



if __name__ == "__main__":
    app.run(debug=True, port= 9000)