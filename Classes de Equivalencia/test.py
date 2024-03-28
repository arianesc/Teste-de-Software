import unittest
from unittest.mock import Mock
import modelo, datetime

class TrianguloTest(unittest.TestCase):

    def test_validarForma_1(self):
        # testa triangulos válidos
        self.assertTrue(modelo.Triangulo(2, 4, 5).validarForma())  
        self.assertTrue(modelo.Triangulo(5, 5, 5).validarForma())  
        self.assertTrue(modelo.Triangulo(5, 5, 7).validarForma())  

    def test_validarForma_2(self):
        # triangulos inválidos
        self.assertFalse(modelo.Triangulo(1, 2, 3).validarForma())  
        self.assertFalse(modelo.Triangulo(2, 3, 6).validarForma()) 
        self.assertFalse(modelo.Triangulo(0, 2, 3).validarForma())
        self.assertFalse(modelo.Triangulo(-5, -8, 1).validarForma())

    def test_ehEquilatero_1(self):
        # Triângulo Equilátero válido
        self.assertTrue(modelo.Triangulo(5, 5, 5).ehEquilatero())  

    def test_ehEquilatero_2(self):
        # Triângulo Equilátero invalido
        self.assertFalse(modelo.Triangulo(3, 4, 5).ehEquilatero())

    def test_ehIsosceles_1(self):
        # Triângulo Isósceles valido
        self.assertTrue(modelo.Triangulo(5, 5, 7).ehIsosceles())
    
    def test_ehIsosceles_2(self):
        # Triângulo Isósceles invalido
        self.assertFalse(modelo.Triangulo(3, 4, 5).ehIsosceles())

    
    def test_ehEscaleno_1(self):
        # Triângulo Escaleno valido
        self.assertTrue(modelo.Triangulo(3, 4, 5).ehEscaleno())
    
    def test_ehEscaleno_2(self):
        # Triângulo Escaleno inválido
        self.assertFalse(modelo.Triangulo(5, 5, 5).ehEscaleno())
