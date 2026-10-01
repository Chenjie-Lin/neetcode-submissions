class Twitter:

    def __init__(self):
        self.tweetMap = defaultdict(list)
        self.followMap = defaultdict(set)
        self.count = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append((self.count, tweetId))
        self.count += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        maxHeap = []
        maxHeap.extend(self.tweetMap[userId][-10:])
        for follow in self.followMap[userId]:
            maxHeap.extend(self.tweetMap[follow][-10:])
        top = heapq.nlargest(10, maxHeap)
        res = []
        for x in top:
            res.append(x[1])
        return res
        


    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
