'"approach 1"'

Name="abi"

'"approach 2"'

class python:
      training="7 methods"
      def __init__(self):
          self._tea=2
      def display(self):
          print(self._tea)

preethi=python()
preethi.display()


'"Approach 3"'

saturday=("sleep","eat","work","play")

print(saturday[3])

'"Approach 4"'

sunday={"morning":"dosa","afternoon":"movie","eveninng":"playing"}

print(sunday["morning"])

'"Approach 5"'

print(saturday)

for i in saturday:

    print(i)



for i in sunday.values():

     print(i)

for i in sunday.keys():

     print(i)

          
'"Approach 6"'

student=[{"id":1,"name":"abi","branch":"doctor"},{"id":2,"name":"athi","branch":"BE"},{"id":3,"name":"amul","branch":"Bcom"}]

print(student[0],student[2])

for i in student:

    if i["name"]=="amul":
        print("amul is available")

    elif i["branch"]=="BE":
          print("BE is available")

'"Approach 7"'

career=[{"intern":[{"id":1,"dept":"BE","Manager":"AK"},{"id":2,"dept":"Bcom","Manager":"AK"}]},
        {"Temporaryjob":[{"id":10,"dept":"accounts","Manager":"magna"},{"id":20,"dept":"finance","Manager":"magna"}]},
        {"permanentjob":[{"id":123,"dept":"managed services","Manager":"Aarthi"},{"id":124,"dept":"managed services","Manager":"Aarthi"}]}]



for i in career:
    
    for j in i.values():

        for k in j:

            print(k)
    

events=[{"alien sarees":[{"silksarees":["A1","a2"]}]}]

for shopping in events:
    print(shopping)
    for i,j in shopping.items():
        print(i,j)
    
class disys:
    def __init__(self,vacc):
        self.vac=[]
        self.vac.append(vacc)
        self.count=0

    def logic(self):
        
        for i in self.vac:
            if i["Vaccine"]=="covisheild":
                self.count=self.count+1


            else:
                print("not vaccinated")
            
        print(self.vac)

    def __del__(self):
        print("not allocated")
        del self.vac
        del self.count

jb=disys({"name":"abi","empid":"001","Vaccine":"covisheild"})
kb=disys({"name":"amul","empid":"002","Vaccine":"covisheild"})
ib=disys({"name":"priya","empid":"003","Vaccine":None})
kb.logic()
jb.logic()
ib.logic()
del jb
del kb
del ib
