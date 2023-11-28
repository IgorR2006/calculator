import pytest
from app.calc import Calculator

class TestCalc:
    def setup_class(self):
        self.calc = Calculator
    
    def test_multiply_calculate_correctly(self):
        assert self.calc.multiply(self, 2, 2) == 4
        
        
    def test_division_calculate_correctly(self):
        assert self.calc.division(self, 8, 2) == 4
        
    def test_subtraction_calculate_correctly(self):
        assert self.calc.subtraction(self, 3, 2) == 1
        
        
    def test_adding_calculate_correctly(self):
        assert self.calc.adding(self, 1, 1) == 2
        
        
    # def test_adding_calculate_failed(self):
    #     assert self.calc.multiply(self, 1, 1) == 3
    
    # def test_subtraction_calculate_failed(self):
    #     assert self.calc.multiply(self, 5, 2) == 2
        
    # def test_subtraction_calculate_correctly_1(self):
    #     assert self.calc.multiply(self, 2, 2) == 0
            
    # def test_division_calculate_failed(self):
    #     assert self.calc.multiply(self, 10, 2) == 4
            
    # def test_multiply_failed(self):
    #     assert self.calc.multiply(self, 2, 2) == 5
     
        
    def test_zero_division(self):
        with pytest.raises(ZeroDivisionError):
            self.calc.division(self,1,0)
            
    
    def teardown_class(self):
        print('Выполнение метода Teardown')