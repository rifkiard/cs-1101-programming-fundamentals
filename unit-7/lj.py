favorite_cars = {
    "Rifki": ["Honda", "Lamborghini", "BMW", "Audi", "Porsche"],
    "Lexy": ["Chevrolet","Honda", "BMW", "Mercedes-Benz", "Acura"],
    "Herbu": ["Lamborghini", "Honda", "Jaguar", "Acura", "Lexus"]
}

def invert_dict(d):
    inverse = dict()
    for key in d:
        val = d[key]

        for li in val:
            if li not in inverse:
                inverse[li] = [key]
            else:
                inverse[li].append(key)

    return inverse

print("Original Dictionary:")
print(favorite_cars)

print("Inverted Dictionary:")
print(invert_dict(favorite_cars))