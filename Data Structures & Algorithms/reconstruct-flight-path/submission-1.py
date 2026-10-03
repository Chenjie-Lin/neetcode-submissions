class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)

        for depart, destination in tickets:
            adj[depart].append(destination)

        for key in adj:
            adj[key].sort(reverse = True)

        n = len(adj)

        if n == 0:
            return []

        currPath = ["JFK"]

        circuit = []

        while len(currPath) > 0:
            currNode = currPath[-1]


            if len(adj[currNode]) > 0:


                nextNode = adj[currNode].pop()

                currPath.append(nextNode)


            else:

                circuit.append(currPath.pop())

        circuit.reverse()

        return circuit