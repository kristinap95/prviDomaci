class Student:
    skolarina = 0
    def __init__(self, ime, prezime, studije, smjer, indeks):
        self.ime = ime
        self.prezime = prezime
        self.studije = studije
        self.smjer = smjer
        self.indeks = indeks
        self.skolarina = 0
    def stampa(self):
        print(f'\nIme: {self.ime}\nPrezime: {self.prezime}\nStudije: {self.studije}\nSmjer: {self.smjer}\nIndeks: {self.indeks}')
    def uplatio(self, rata):
        self.skolarina += rata
        if self.smjer == 'D':
            if self.skolarina == 1000:
                return True
            else:
                return False
        elif self.skolarina == 500:
            return True
        else:
            return False
    def vrati(self):
        return f'{self.ime} {self.prezime}\n'

    

student1 = Student('Janko', 'Jankovic', 'specijalisticke ', 'C', '25/20')
student1.stampa()

student2 = Student('Marko','Markovic', 'osnovne', 'D', '23/15')
student2.stampa()

s1 = student1.uplatio(125)
s2 = student2.uplatio(500)

with open('dugovanja.txt', 'a+') as file_name:
    if s1 == False:
        file_name.writelines(student1.vrati())
    if s2 == False:
        file_name.writelines(student2.vrati())

info = ""
try:
    with open('dugovanja.txt', 'r') as file:
        info = file.read().rstrip('\n')
except FileExistsError as file_error:
    info = ""
finally:
    with open('dugovanja.txt', 'a+') as file_name:
        file_name.writelines("")

print(info)
