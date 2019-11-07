# -*- coding: utf-8 -*-
"""
Je vérifie la classe Portail en vérifiant seulement ses variables d'instances
@author: melan
"""

import unittest

from Portail import Portail
from Monde import Monde

class TestPortail(unittest.TestCase):
    
    def testPortail(self):
        monde = Monde(50,40)
        portail = Portail(monde,23,32, 43, 1)
        self.assertEqual(portail.cle.coords, (43,1))
        
        
        
if __name__ == '__main__':
    unittest.main()