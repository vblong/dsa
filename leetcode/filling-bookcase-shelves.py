class Solution:
    def minHeightShelves(self, books, shelfWidth: int) -> int:
        n = len(books)
        memo = [[0 for j in range(shelfWidth + 1)] for i in range(n)]
        print(memo)
        def rec(i, width, height):
            nonlocal memo
            if i >= n:
                return height

            if memo[i][width] != 0:
                return memo[i][width]

            # new row
            memo[i][width] = height + rec(i + 1, books[i][0], books[i][1])
            # put in current row
            if width + books[i][0] <= shelfWidth:
                op2 = rec(i + 1, width + books[i][0], max(height, books[i][1]))
                memo[i][width] = min(memo[i][width], op2)
            return memo[i][width]

        return rec(0, books, 0)
        # dp = {}
        # # bestHeight = 1e9
        # def rec(i, totalHeight, currentWidth, currentMaxHeight, bestHeight):
        #     # nonlocal bestHeight
        #     print('at book',i, 'totalHeight = ', totalHeight, 'currentWidth = ', currentWidth, 'currentMaxHeight =', currentMaxHeight)
        #     if i == n:
        #         bestHeight = min(bestHeight, totalHeight)
        #         print('--- new conclusion', bestHeight)
        #         return bestHeight
        #     cBook = books[i]
        #     # if (i, shelfWidth - currentWidth) in dp:
        #     #     print('found memo', (i, shelfWidth - currentWidth), '=', dp[(i, shelfWidth - currentWidth)])
        #     #     return dp[(i, shelfWidth - currentWidth)]            
        #     # put in new row
        #     op2 = rec(i + 1, totalHeight + cBook[1], cBook[0], cBook[1], bestHeight)
        #     if currentWidth + cBook[0] <= shelfWidth:
        #         # put in current row
        #         op1 = rec(i + 1, max(totalHeight, totalHeight - currentMaxHeight + cBook[1]), currentWidth + cBook[0], max(currentMaxHeight, cBook[1]), bestHeight)
        #         best = min(op1, op2)
        #         dp[(i, shelfWidth - currentWidth)] = best                
        #         return min(op1, op2)
        #     dp[(i, shelfWidth - currentWidth)] = op2
        #     return op2
        # h = rec(1, books[0][1], books[0][0], books[0][1], 1e9)
        # for k, v in dp.items():
        #     print(k, v)
        # return h

# books = [[11,83],[170,4],[93,80],[155,163],[134,118],[75,14],[122,192],[123,154],[187,29],[160,64],[170,152],[113,179],[60,102],[28,187],[59,95],[187,97],[49,193],[67,126],[75,45],[130,160],[4,102],[116,171],[43,170],[96,188],[54,15],[167,183],[58,158],[59,55],[148,183],[89,95],[90,113],[51,49],[91,28],[172,103],[173,3],[131,78],[11,199],[77,200],[58,65],[77,30],[157,58],[18,194],[101,148],[22,197],[76,181],[21,176],[50,45],[80,174],[116,198],[138,9],[58,125],[163,102],[133,175],[21,39],[141,156],[34,185],[14,113],[11,34],[35,184],[16,132],[78,147],[85,170],[32,149],[46,94],[196,3],[155,90],[9,114],[117,119],[17,157],[94,178],[53,55],[103,142],[70,121],[9,141],[16,170],[92,137],[157,30],[94,82],[144,149],[128,160],[8,147],[153,198],[12,22],[140,68],[64,172],[86,63],[66,158],[23,15],[120,99],[27,165],[79,174],[46,19],[60,98],[160,172],[128,184],[63,172],[135,54],[40,4],[102,171],[29,125],[81,9],[111,197],[16,90],[22,150],[168,126],[187,61],[47,190],[54,110],[106,102],[55,47],[117,134],[33,107],[2,10],[18,62],[109,188],[113,37],[59,159],[120,175],[17,147],[112,195],[177,53],[148,173],[29,105],[196,32],[123,51],[29,19],[161,178],[148,2],[70,124],[126,9],[105,87],[41,121],[147,10],[78,167],[91,197],[22,98],[73,33],[148,194],[166,64],[33,138],[139,158],[160,19],[140,27],[103,109],[88,16],[99,181],[2,140],[50,188],[200,77],[73,84],[159,130],[115,199],[152,79],[1,172],[124,136],[117,138],[158,86],[193,150],[56,57],[150,133],[52,186],[21,145],[127,97],[108,110],[174,44],[199,169],[139,200],[66,48],[52,190],[27,86],[142,191],[191,79],[126,114],[125,100],[176,95],[104,79],[146,189],[144,78],[52,106],[74,74],[163,128],[34,181],[20,178],[15,107],[105,8],[66,142],[39,126],[95,59],[164,69],[138,18],[110,145],[128,200],[149,150],[149,93],[145,140],[90,170],[81,127],[57,151],[167,127],[95,89]]
# books = [[1,1],[2,3],[2,3],[1,1], [1,1],[1,1],[1,2]]
books = [[1,3],[2,4],[3,2]]
a = Solution().minHeightShelves(books, 6)
print(a)