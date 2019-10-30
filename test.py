#!/usr/bin/env python3
from random import randint
from numpy import mean
from helper import Executable, Test, Source, Program
from itertools import permutations
import codecs

class TestArguments(Test):

    def test_printf_1(self):
        "printf/1.c"
        p = Program('printf/1.c')
        self.test("Utilisation de printf ?", lambda: p.source.grep(r'printf.+[Hh]ello,?\s+[Ww]orld'))
        self.test("Programme compile sans erreurs ?", p.build())
        self.test("Programme compile sans warnings ?", p.warnings == 0)
        self.test("Hello, World sur stdout ?", p.run().stdout.match(r'[Hh]ello,?\s+[Ww]orld'))

    def test_printf_2(self):
        "printf/2.c"
        p = Program('printf/2.c')
        self.test("Utilisation de printf ?", p.source.grep(r'printf.+\%d'))
        self.test("Programme compile sans erreurs ?", p.build())
        self.test("Programme compile sans warnings ?", p.warnings == 0)
        self.test("42 sur stdout ?", p.run().stdout.match(r'42'))

    def test_printf_3(self):
        "printf/3.c"
        p = Program('printf/3.c')
        self.test("Utilisation de printf ?", p.source.grep(r'printf.+\%l?[Ffg]'))
        self.test("Programme compile sans erreurs ?", p.build())
        self.test("Programme compile sans warnings ?", p.warnings == 0)
        self.test("pi sur stdout ?", p.run().stdout.match(r'3.141592'))

    def test_printf_4(self):
        "printf/4.c"
        p = Program('printf/4.c')
        self.test("Utilisation de printf ?", p.source.grep(r'printf.+\%\d+\.\d+[Ffg]'))
        self.test("Programme compile sans erreurs ?", p.build())
        self.test("Programme compile sans warnings ?", p.warnings == 0)
        self.test("042.12 sur stdout ?", p.run().stdout.match(r'042.12'))

    def test_printf_5(self):
        "printf/5.c"
        p = Program('printf/5.c')
        self.test("Utilisation de printf ?", p.source.grep(r'printf.+\\t'))
        self.test("Programme compile sans erreurs ?", p.build())
        self.test("Programme compile sans warnings ?", p.warnings == 0)
        self.test("Sortie standard correcte ?", p.run().stdout.match(r'23\t3.14150*\t6.280*\t99'))

    def test_printf_6(self):
        "printf/6.c"
        p = Program('printf/6.c')
        self.test("Ne pas utilser sprintf ?", not p.source.grep(r'sprintf'))
        self.test("Programme compile sans erreurs ?", p.build())
        self.test("Question 1 ?", p.run().stdout.match(r'Q1.+\'(z)7\1 {5}7\1\\n'))
        self.test("Question 2 ?", p.run().stdout.match(r'Q2.+\'7{2}\.0{6}\\n'))
        self.test("Question 3 ?", p.run().stdout.match(r'Q3.+\'36[,]1e[,]1E\\n'))
        self.test("Question 4 ?", p.run().stdout.match(r'Q4.+\'77\\n'))

    def test_printf_7(self):
        "printf/7.c"
        p = Program('printf/7.c')
        self.test("Utiliser printf ?", p.source.grep(r'printf'))
        self.test("Variable birth year correcte ?", p.source.grep(r'char\s+birth_year\s*=\s*\d{1,2}\s*;'))
        self.test("Plus de points de suspension ?", not p.source.grep(r'\.{3}'))
        self.test("Programme compile sans erreurs ?", p.build())
        self.test("Programme compile sans warnings ?", p.warnings == 0)
        self.test("Nom présent sur stdout ?", p.run().stdout.match(r'Name:\s+\S+'))
        self.test("Année de naissance sur stdout ?", p.run().stdout.match(r'Birth Year:\s+(19|20)\d{2}'))
        self.test("Mobile sur stdout ?", p.run().stdout.match(r'Mobile:\s+\+\d{2} (\d{2,3} ?)*\d{2,3}'))
    #     # arguments/1
    #     P = Executable('arguments/1.out')
    #     n = 5
    #     args = map(str, range(n))
    #     self.test("./1.out %s" % (" ".join(args)) , int(P(args)).stdout == n)

    #     # arguments/2
    #     P = Executable('arguments/2.out')
    #     n = 5
    #     args = ["foo", "bar", "baz", "42"]
    #     self.test("./2.out %s" % (" ".join(args)),
    #         [P(args).stdout.match(r'%d*?\b%s\b' % (n + 1, s)) for n, s in enumerate(args)])

    #     # arguments/3
    #     P = Executable('arguments/3.out')
    #     args = [randint(2048) for i in range(7)]
    #     self.test("./3.out %s" % (" ".join(map(str, args))),
    #         P(args).stdout.match(str(min(args))))

    #     # arguments/4
    #     P = Executable('arguments/4.out')
    #     n = 5
    #     args = [randint(2048) for i in range(10)]
    #     self.test("./4.out %s" % (" ".join(map(str, args))),
    #         P(args).stdout.match(str(mean(args))))


    def test_scanf_1(self):
        "scanf/1.c"
        p = Program('scanf/1.c')
        self.test("Utiliser scanf ?", p.source.grep(r'\bscanf\b'))
        self.test("Petit oiseau (&) ?", p.source.grep(r'&\w+'))
        self.test("Utiliser printf ?", p.source.grep(r'\bprintf\b'))

        self.test("Programme compile sans erreurs ?", p.build())
        self.test("Programme compile sans warnings ?", p.warnings == 0)

        self.test("Erreur en retour pour 'echo oops | ./1.out' ?", p.run(stdin=b'oops').exit_status == 1)
        self.test("Affichage correct sur stdout ?", p.run(stdin=b'22').stdout.match(r'22'))

    def test_scanf_2(self):
        "scanf/2.c"
        p = Program('scanf/2.c')
        self.test("Utiliser scanf une fois ?", len(p.source.grep(r'\bscanf\s*\(')) == 1)
        self.test("Deux Petits oiseaux (&) ?", len(p.source.grep(r'&\w+')) == 2)
        self.test("Utiliser printf une fois ?", len(p.source.grep(r'\bprintf\b')) == 1)

        self.test("Programme compile sans erreurs ?", p.build())
        self.test("Programme compile sans warnings ?", p.warnings == 0)

        self.test("Erreur en retour pour 'echo oops | ./1.out' ?", p.run(stdin=b'oops').exit_status == 1)
        self.test("Affichage correct sur stdout ?", p.run(stdin=b'312 411').stdout.match(r'723'))  

    def test_scanf_3(self):
        "scanf/3.c"
        p = Program('scanf/3.c')
        self.test("Utiliser scanf une fois ?", len(p.source.grep(r'\bscanf\s*\(')) == 1)
        self.test("Pas d'esperluette ! hein sérieux ?", len(p.source.grep(r'&\w+')) == 0)
        match = p.source.grep(r'\bcountry\s*\[\s*(\d+)\s*\]')
        self.test("Accepte des grands pays comme 'The United Kingdom of Great Britain and Northern Ireland' ?", len(match) > 0 and int(match[0]) > 48)

        self.test("Programme compile sans erreurs ?", p.build())
        self.test("Programme compile sans warnings ?", p.warnings == 0)

        country = "Switzerland"
        self.test("Affichage correct sur stdout ?", p.run(stdin=bytes(country, 'utf8')).stdout.match(r'Le pays est:\s*' + country))                 

    def test_scanf_4(self):
        "scanf/4.c"
        import numpy as np

        p = Program('scanf/4.c')
        self.test("Utiliser scanf une fois ?", len(p.source.grep(r'\bscanf\s*\(')) == 1)
        self.test("Utiliser une boucle 'for' ou 'while' ?", p.source.match(r'\b(for|while)\b'))
        self.test("Un seul et commercial ?", len(p.source.grep(r'&\w+')) == 1)
        self.test("Feof utilisé ?", p.source.match(r'feof'))
        self.test("Programme compile sans erreurs ?", p.build())
        self.test("Programme compile sans warnings ?", p.warnings == 0)
        
        n = 1000
        vector = np.random.randint(255, size=n)
        mean = np.mean(vector)
        self.test(f"Affichage correct sur stdout pour {n} valeurs ?", 
            p.run(stdin=' '.join(map(str, vector)))
                .stdout
                .match("{:.4f}"
                .format(mean)))                 

    def test_scanf_5(self):
        "scanf/5.c"

        p = Program('scanf/5.c')
        self.test("Plus de blancs ?", not p.source.match(r'\.{3}'))
        self.test("Premier blanc complété correctement ?", p.source.match(chr(38)))
        self.test("Second blanc complété correctement ?", p.source.match(codecs.decode('nqerffr', 'rot13')))        
        self.test("Programme compile sans erreurs ?", p.build())                   

    def test_math_1(self):
        "math/1.c"

        p = Program('math/1.c')
        self.test("Powpow power ?", p.source.match(r'\bpow.+?\b3\b\s*\)'))
        self.test("Cast en int ?", p.source.match(r'int \w+|\(int\)\w+'))
        self.test("Programme compile sans erreurs ?", p.build())
        self.test("Programme compile sans warnings ?", p.warnings == 0)
        self.test("Affichage correct sur stdout ?", p.run(5).stdout.match(r'125'))                 


    def test_math_2(self):
        "math/2.c"

        p = Program('math/2.c')
        self.test("Est-ce qu'u ret ?", p.source.match(r'\bsqrt\b'))
        self.test("Programme compile sans erreurs ?", p.build())
        self.test("Programme compile sans warnings ?", p.warnings == 0)
        self.test("Affichage correct sur stdout ?", p.run(2).stdout.match(r'1.414214'))                 

TestArguments()
