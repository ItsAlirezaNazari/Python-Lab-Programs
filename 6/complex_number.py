class ComplexNumber:
    def __init__(self, real, image):
        self.real_number = real
        self.image_number = image
    
    def add(self, complex_number):
        result = ComplexNumber(0, 0)
        result.real_number = self.real_number + complex_number.real_number
        result.image_number = self.image_number + complex_number.image_number
        return result

    def sub(self, complex_number):
        result = ComplexNumber(0, 0)
        result.real_number = self.real_number - complex_number.real_number
        result.image_number = self.image_number - complex_number.image_number
        return result

    def mul(self, complex_number):
        result = ComplexNumber(0, 0)
        result.real_number = self.real_number * complex_number.real_number - self.image_number * complex_number.image_number
        result.image_number = self.real_number * complex_number.image_number + self.image_number * complex_number.real_number
        return result
    
    def show(self):
        print(self.real_number, "+", self.image_number, "i")


complex1 = ComplexNumber(3, 2)
complex2 = ComplexNumber(1, 7)

result = complex1.add(complex2)
result.show()
