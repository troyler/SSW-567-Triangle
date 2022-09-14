import unittest
import math

def classify_Triangle(a,b,c):
    if (a + b) < c or (a + c) <= b or (b + c) <= a:
        return "Not a Triangle"

    else:

        if math.sqrt((a*a) + (b*b))== c or math.sqrt((a*a) + (c*c))== b or math.sqrt((c*c) + (b*b))== a: 
            return "Right Triangle"

        if a == b == c:
            return "Equilateral Triangle"
        
        elif a != b !=c:
            return "Scalene Triangle"
        
        elif (a ==b != c) or (a ==c != b) or (b== c != a):
            return "Isosceles Triangle"




def runClassifyTriangle(a,b,c):
    print(f'classify_triangle({a},{b},{c})= ', classify_Triangle(a,b,c))



class TestTriangles(unittest.TestCase):

    def testNumOne(self):
         self.assertEqual(classify_Triangle(3,4,5),'Right Triangle' ,'3,4,5 is a Right triangle')

    def testForTriangle(self):
        self.assertEqual(classify_Triangle(1,500,501), "Not a Triangle", "1, 500, 501 is not a triangle")

    def testForTriangle(self):
        self.assertEqual(classify_Triangle(1,500,501), "Not a Triangle", "1, 500, 501 is not a triangle")    #showing error in the original
        #logic that came as a result of the < being used instead of <=

    def testScalene(self):
        self.assertEqual(classify_Triangle(4,5,6),'Scalene Triangle' ,'4,5,6 is a Scalene triangle')

    def testIsosceles(self):
        self.assertEqual(classify_Triangle(10,10,15),'Isosceles Triangle' ,'10,10,15 is an Isosceles triangle')






unittest.main(exit=True) # this runs all of the tests - use this line if running from the command line