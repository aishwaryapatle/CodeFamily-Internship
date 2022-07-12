"""
Question 3) You have to given a information about N people.Each person has name .last name ,age,sex,city .Print their names in a specific format in descending order i.e the elder person name should br first printed,iFor the two people of the sane age print theri in orderof input.

Input : 
3 
John 20 m mumbai
Robert  36 f Bangalore
Nicks 34 m Pune


output 
Robert  36 f Bangalore
Nicks 34 m Pune
John 20 m mumbai

"""
import operator

def person_lister(f):
    def inner(people):
        return map(f, sorted(people, key=lambda x: int(x[1]), reverse=True))
    return inner

@person_lister
def name_format(person):
    return person[0] + " " + person[1]+ " " + person[2]+ " " + person[3]

if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print("\nAfter Sorting in descending order : ")
    print(*name_format(people), sep='\n')
    
