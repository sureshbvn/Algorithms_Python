__author__ = 'sureshbvn'
__author__ = 'sureshbvn'
class TreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    def get_left(self):
        return self.left
    def set_left(self,left):
        self.left=left
    def get_right(self):
        return self.right
    def set_righ(self,right):
        self.right=right
    def get_data(self):
        return self.data

def check_equal_trees(Tree1,Tree2):

    if(Tree1==Tree2==None):
        return True
    if(Tree1==None or Tree2==None):
        return False
    else:
        return(Tree1.get_data()==Tree2.get_data() and (check_equal_trees(Tree1.get_left(),Tree2.get_left())) and (check_equal_trees(Tree1.get_right(),Tree2.get_right())))

    return False

if __name__ =="__main__":
    Tree1=TreeNode(1)
    Tree2=TreeNode(1)



    node11=TreeNode(2)
    node21=TreeNode(2)

    node12=TreeNode(3)
    node22=TreeNode(3)

    Tree1.set_left(node11)
    Tree1.set_righ(node12)

    Tree2.set_left(node21)
    Tree2.set_righ(node22)

    a=check_equal_trees(Tree1,Tree2)


    print a

