import math

# Noktaların Tanımlanması
points = []

# Kullanıcıdan Noktaları Al
x1 = float(input("Enter the first point's x coordinate: "))
y1 = float(input("Enter the first point's y coordinate: "))
x2 = float(input("Enter the second point's x coordinate: "))
y2 = float(input("Enter the second point's y coordinate: "))

# Noktaları Listeye Ekle
points.append((x1, y1))
points.append((x2, y2))

# Öklid Mesafesi İçin Fonksiyon
def euclideanDistance(point1, point2):
    return math.sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2)

# Mesafelerin Hesaplanması
distances = []
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        dist = euclideanDistance(points[i], points[j])
        distances.append(dist)

# Minimum Mesafenin Bulunması
min_distance = min(distances)

# Sonucu Yazdır
print("Minimum distance between two points is: ", min_distance)
