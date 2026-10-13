class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        i=0
        no_of_boats=0
        j=len(people)-1
        while i<=j:
            if people[j]==limit or people[i]+people[j]>limit:
                no_of_boats+=1
                j-=1
            elif people[i]+people[j]<=limit:
                no_of_boats+=1
                i+=1
                j-=1
            elif i==j:
                no_of_boats+=1
                i+=1
                j-=1
          
        return no_of_boats




            
