class Human:

    def __new__(cls, name, *ent, **magic):
        return super().__new__(cls)
    def __init__(self, name, *ent, magic=0):
        self.name = name
        self.ent = list(ent)
        self.magic = magic

    def __add__(self, other):
        self.ent.append(other)
        return self

    def change_name(self, line):
        self.name = f'{self.name} {line}'
        self.magic = self.magic + len(line)//4
        # return self.name


    def __len__(self):
        return len(self.ent)

    def __repr__(self):
        return f'Human by name {self.name} ({(", ").join(self.ent)}), {self.magic})'

    def __call__(self, other):

        return self.ent[:int(other):]
    def __sub__(self,other):

        z=[]

        self.name = (self.name[:3:]).title()+(other.name[-3:]).title()
        for k in self.ent:
            if k not in other.ent: z.append(k)
        self.ent=z
        self.magic = 0

        return self






hm = Human('Marran', 'Hanger', 'Stick', 'Wizzard', magic=10)
hm1 = Human('Lart', 'Wizzard')
# print(hm, hm1, sep='\n')
# print(hm > hm1, hm <= hm1, hm == hm1)
hm2 = hm - hm1
print(hm2)
print(hm2 > hm1, hm2 <= hm, hm2 != hm)