'''This problem was asked by Google.
Difficulty: Medium

Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, 
and deserialize(s), which deserializes the string back into the tree.

For example, given the following Node class

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
The following test should pass:

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == "left.left"'''


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def serialize(root):
    #put nodes into string form 
    result_list = []

    def dfs(node):
        if not node:
            result_list.append('#') #add null marker to list
            return

        result_list.append(str(node.val)) #add node value to list
        #recursively process left and right subtrees
        dfs(node.left)
        dfs(node.right)
    
    #traverse the tree
    dfs(root)

    return ",".join(result_list)

def deserialize(s):

    tokens = s.split(",")
    tokens_iter = iter(tokens)

    def dfs():
        #Recursive function to build the tree

        #get the next token from the iterator
        val = next(tokens_iter)
            
        if val == '#':
            return None
        
        #Create a new Node with the current token as its value
        node = Node(val)

        #Recursively build the left child
        node.left = dfs()

        #recursively build the right child
        node.right = dfs()

        return node

#start reconstruction process and return the root node
    return dfs()

#test solution:
def main():
    node = Node('root', Node('left', Node('left.left')), Node('right'))

    # Test the round-trip: serialize then deserialize
    serialized_str = serialize(node)
    print("Serialized string:", serialized_str)

    deserialized_node = deserialize(serialized_str)

    # The assertion: check if the deserialized tree has the correct structure
    try:
        assert deserialized_node.left.left.val == "left.left"
        print("✅ Test PASSED!")
    except AssertionError:
        print("❌ Test FAILED!")
    except AttributeError as e:
        # This will catch errors if .left or .left.left is None
        print(f"❌ Test FAILED with error: {e}")
main()


#NOTES:
# This was a healthy reminder of the functionality of classes and recursive functions. 
# Classes and recursive functions are such an incredibly powerful set of tools.
# I was trying to deconstruct the process of a recursive function but if I
#   just understood how they work this question would be a lot easier for me.
# This solution was pretty much derrived from AI but I will not forget what i learned here

