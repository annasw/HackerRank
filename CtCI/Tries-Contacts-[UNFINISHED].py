class Node():
    def __init__(self, value = '*'):
        self.value = value
        self.children = [] # a list of child nodes, NOT letters
        self.isAWord = False
    
    def setValue(self, value):
        self.value = value
    
    # takes a child node and adds it to the list of children
    def addChild(self, childNode):
        self.children.append(childNode)
    
    # takes a letter and returns whether it has a node whose value is that letter
    def hasChild(self, letter):
        for x in self.children:
            if x.value == letter:
                return True
        return False
    
    # takes a letter and returns the node in children (assuming it exists) s.t. the return node has a value of letter.
    # if it doesn't exist (it will) just do nothing
    def getChild(self, letter):
        for x in self.children:
            if x.value==letter:
                return x
	
	# set this node to have the boolean flag indicating that it IS a word
    def setAsWord(self):
        self.isAWord = True
	
	# returns number of actual words (i.e. with isAWord flags true) including and underneath this node
    def numWords(self):
        wordCount = 0
        if self.isAWord: wordCount += 1
        if not self.children:
            return wordCount
        for child in self.children:
            wordCount += child.numWords()
        return wordCount

class Trie():
    def __init__(self):
        self.head = Node()
    
    def add(self, word):
        pointer = self.head
        # all of this just ensures that the whole word goes in
        while word:
            if pointer.hasChild(word[0]):
                pointer = pointer.getChild(word[0])
                word = word[1:]
            else:
                pointer.addChild(Node(word[0]))
                pointer = pointer.getChild(word[0])
                word = word[1:]
        pointer.setAsWord()

    # return the number of children starting with partial name
    def numPartial(self, partial):
        pointer = self.head
        while partial:
            if pointer.hasChild(partial[0]):
                pointer = pointer.getChild(partial[0])
                partial = partial[1:]
            else: # no such words exist
                return 0
        return pointer.numWords()
    
    def printTrie(self):
        pass


def main():
    trie = Trie()
    
    n = int(raw_input().strip())
    for q in range(n):
        query = raw_input().strip().split(' ')
        if query[0] == 'add':
            trie.add(query[1])
        # find and print the number of names starting with partial
        elif query[0] == 'find':
            print trie.numPartial(query[1])

if __name__=='__main__':
    main()
