import unittest
from operaciones_comparacion import es_mayor_que, es_menor_que, es_mayor_o_igual_que, es_menor_o_igual_que, son_iguales

class TestOperacionesComparacion(unittest.TestCase):
    
    def test_es_mayor_que(self):
        " CASO VERDADERO "
        self.assertGreater(es_mayor_que(5.8,5.2),0)
        " CASO FALSO "
        self.assertFalse(es_mayor_que(0.80,8))
        
    def test_es_menor_que(self):
        " CASO VERDADERO "
        self.assertLess(es_menor_que(3.7,8),2) 
        " CASO FALSO "
        self.assertFalse(es_menor_que(6,2))
        
    def test_es_mayor_o_igual_que(self):
        " CASO VERDADERO "
        self.assertGreaterEqual(es_mayor_o_igual_que(7.1,7),0)
        " CASO FALSO "
        self.assertFalse(es_mayor_o_igual_que(4,8))
        
    def test_es_menor_o_igual_que(self):
        " CASO VERDADERO "
        self.assertLessEqual(es_menor_o_igual_que(8.6,8.6),2)
        " CASO FALSO"
        self.assertFalse(es_menor_o_igual_que(5,2))
        
    def test_son_iguales(self):
        " CASO VERDADERO "
        self.assertEqual(son_iguales(9,9),True)
        " CASO FALSO"
        self.assertFalse(son_iguales(4,8))
        
if __name__ == '__main__':
    unittest.main()        
        
               