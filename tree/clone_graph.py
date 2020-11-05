class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        clonea = Node(node.val, [])

        queue = [(node, clonea)]
        maps = {node.val: clonea}

        #bfs
        while queue:
            nod, clon = queue.pop(0)
            for n in nod.neighbors:
                #check to make sure we are not working on a node again.
                if n.val not in maps:
                    #clone the node
                    newclone = Node(n.val, [])
                    # add neighbors to the cloned nodes' neighbors
                    clon.neighbors.append(newclone)
                    #add node being looped through to queue
                    queue.append((n, newclone))
                    #map clone to value
                    maps[n.val] = newclone
                else:
                    # node already created, just add neighbors
                    clon.neighbors.append(maps[n.val])

        return clonea
