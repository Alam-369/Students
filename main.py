class Subject(object):
    def __init__(self,classNo,Bangla,markBangla,English,markEnglish,Math,markMath):
        self.classNo = classNo
        self.Bangla = Bangla
        self.English = English
        self.Math = Math
        self.markBangla = markBangla
        self.markEnglish = markEnglish
        self.markMath = markMath
    def updateEnglishMark(self,markEnglish):
        self.markEnglish = markEnglish
    def updateBanglaMark(self,markBangla):
        self.markBangla = markBangla
    def updateMathMark(self,markMath):
        self.markMath = markMath

class Student(Subject):
    
    def __init__(self,name,classNo,Bangla,markBangla,English,markEnglish,Math,markMath,day):
        super().__init__(classNo,Bangla,markBangla,English,markEnglish,Math,markMath)
        self.name = name
        self.day = day
    def updateDays(self,day):
        self.day = day


        
income = 0
l = []

def main():
   
    income = 0
   
    l.append( Student('katha',8,True,0,True,0,True,0,0))
    l.append( Student('ishrat',8,True,0,True,0,True,0,0))
    l.append( Student('tumpa',8,True,0,True,0,True,0,0))
    l.append( Student('taslima',8,True,0,True,0,True,0,0))
    l.append( Student('fagun',8,True,0,True,0,True,0,0))
   #print(l[0].markEnglish)
    print('Write "ADD" for adding a student.\nWrite "LIST" to see all Student.\nWrite "EDIT" for editing a student.\nWrite "DELETE" for deleting a student.\nWrite "EXIT" to stop the application.')
    while(True):
       s = str(input())
       if s=='EXIT':
           break
       elif s=='ADD':
           print('Enter Student :')
           name = str(input())
           print('Enter Class No:')
           classNo = int(input())
           print('Will the student emroll English?if yes write "YES",otherwise write "NO')
           k = str(input())
           English = False
           if k=='YES':
               English = True
           print('Will the student emroll Bangla?if yes write "YES",otherwise write "NO')
           k = str(input())
           Bangla = False
           if k=='YES':
               Bangla = True
           print('Will the student emroll Math?if yes write "YES",otherwise write "NO')
           k = str(input())
           Math = False
           if k=='YES':
               Math = True
           l.append(Student(name,classNo,Bangla,0,English,0,Math,0,0))

       elif s=='EDIT':
           print('Write "uDay" to update days.\nWrite "eMark" to update English Mark.\nWrite "bMark" to update Bangla mark.\nWrite mMark to update Math Mark.')
           s = str(input())

           if s=='uDay':
               print('Enter name of student:')
               s = str(input())
               print('Enter Class of student:')
               c = int(input())
               
               for i in l:
                   if i.name==s and i.classNo==c:
                       day = i.day+1
                       income+=1
                       i.updateDays(day)
                       break
                #print(income)

           elif s=='eMark':
               print('Enter name of student:')
               s = str(input())
               print('Enter Class of student:')
               c = int(input())
               print('Enter mark of latest english exam:')
               m = int(input())
               for i in l:
                   if i.name==s and i.classNo==c:
                       mark = i.markEnglish
                       if mark != 0:
                           mark+=m
                           mark/=2
                      
                       i.updateEnglishMark(mark)
                       break
           elif s=='bMark':
               print('Enter name of student:')
               s = str(input())
               print('Enter Class of student:')
               c = int(input())
               print('Enter mark of latest bangla exam:')
               m = int(input())
               for i in l:
                   if i.name==s and i.classNo==c:
                       mark = i.markBangla
                       if mark != 0:
                           mark+=m
                           mark/=2
                      
                       i.updateBanglaMark(mark)
                       break
           elif s=='mMark':
               print('Enter name of student:')
               s = str(input())
               print('Enter Class of student:')
               c = int(input())
               print('Enter mark of latest math exam:')
               m = int(input())
               for i in l:
                   if i.name==s and i.classNo==c:
                       mark = i.markMath
                       if mark != 0:
                           mark+=m
                           mark/=2
                      
                       i.updateMathMark(mark)
                       break
          
           else:
               print('No such edit option.')
       elif s=='DELET':
            print('Enter name of student:')
            s = str(input())
            print('Enter Class of student:')
            c = int(input())
            for i in l:
                   if i.name==s and i.classNo==c:
                       l.remove(i)
                       break

       elif s=='LIST':
           print('Write "Students" to see all enrolled students.\nWrite "IC" to see the total income.')
           s = str(input())
           if s =='Students':
               for i in l:
                   print('Name: '+str(i.name))
                   print('Class: '+str(i.classNo))
                   print('English: '+str(i.English))
                   print('Mark of English: '+str(i.markEnglish))
                   print('English: '+str(i.English))
                   print('Mark of Bangla: '+str(i.markBangla))
                   print('Math: '+str(i.English))
                   print('Mark of math: '+str(i.markMath))
                   print('Total day of class: '+str(i.day))
           elif s=='IC':
              print('Total Income: '+ income)
           else:
              print('No such option')
       else:
           print('INVALID INPUT!!!!')

       #print(str(income) +' '+ str(l[0].day))
       


main()