class Vector():
    def __init__(self, data):
        self.data = data
        return

    def __add__(self, objeto_vector):
      
        vector = self.data + objeto_vector.data
        return Vector(vector)
    


v1 = Vector([1,2])
v2 = Vector([3,4])

print(v1.data)
print(v2.data)

v3 = v1 + v2

print(v3.data)