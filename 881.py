class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        ans = 0


        while people != [] and people[-1] == limit:
            ans += 1
            people.pop()
        
        if people == []:
            return ans
        if len(people) == 1:
            return ans + 1

        other = []
        half_way = limit // 2 

        while people != [] and people[-1] > half_way: 
            other.append(people.pop())
        
        #print(other, people)

        while people != [] and other != []:
            if other[-1] + people[-1] <= limit:
                other.pop()
                people.pop()
            else:
                people.pop()
                if people != []:
                    people.pop()
            ans += 1
            #print(other, people)
        
        if other != []:
            ans += len(other)
        if people != []:
            l = len(people)
            ans += l // 2
            if l % 2 == 1:
                ans += 1

        return ans
            