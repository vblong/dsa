from collections import defaultdict
from typing import List


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        accountIds = [i for i in range(len(accounts))]
        parents = defaultdict(int)
        names = [""] * len(accounts)
        for i in range(len(accounts)):
            parents[i] = i
        
        def samePerson(emailList1, emailList2):
            for email1 in emailList1:
                if email1 in emailList2:
                    return True
            for email2 in emailList2:
                if email2 in emailList1:
                    return True
            return False

        def union(x, y):
            rootX, rootY = find(x), find(y)
            parents[rootX] = rootY

        def find(x):
            while x != parents[x]:
                x = parents[x]
            return x
        
        for i in range(len(accounts) - 1):
            for j in range(i + 1, len(accounts)):
                iEmails, jEmails = accounts[i][1:], accounts[j][1:]
                if samePerson(iEmails, jEmails):
                    union(i, j)
                    names[i], names[j] = accounts[i][0], accounts[j][0]

        results = []
        mergedAccounts = defaultdict(list)
        for accId in accountIds:
            items = accounts[accId][1:]
            rootId = find(accId)
            for item in items:
                mergedAccounts[rootId].append(item)    
        
        for k, v in mergedAccounts.items():
            acc = []
            acc.append(accounts[k][0])
            acc += sorted(set(v))
            results.append(acc)
        print(mergedAccounts)
        return results
accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
# accounts = [["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe1@m.co"],["Kevin","Kevin3@m.co","Kevin5@m.co","Kevin0@m.co"],["Ethan","Ethan5@m.co","Ethan4@m.co","Ethan0@m.co"],["Hanzo","Hanzo3@m.co","Hanzo1@m.co","Hanzo0@m.co"],["Fern","Fern5@m.co","Fern1@m.co","Fern0@m.co"]] # [["Ethan","Ethan0@m.co","Ethan4@m.co","Ethan5@m.co"],["Gabe","Gabe0@m.co","Gabe1@m.co","Gabe3@m.co"],["Hanzo","Hanzo0@m.co","Hanzo1@m.co","Hanzo3@m.co"],["Kevin","Kevin0@m.co","Kevin3@m.co","Kevin5@m.co"],["Fern","Fern0@m.co","Fern1@m.co","Fern5@m.co"]]
# accounts = [
#     ["Alex","Alex5@m.co","Alex4@m.co","Alex0@m.co"],
#     ["Ethan","Ethan3@m.co","Ethan3@m.co","Ethan0@m.co"],
#     ["Kevin","Kevin4@m.co","Kevin2@m.co","Kevin2@m.co"],
#     ["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe2@m.co"],
#     ["Gabe","Gabe3@m.co","Gabe4@m.co","Gabe2@m.co"]
# ]

print(Solution().accountsMerge(accounts)) # [["John","john00@mail.com","john_newyork@mail.com","johnsmith@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]