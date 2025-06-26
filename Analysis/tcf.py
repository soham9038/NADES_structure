import math

TOLERANCE = 0.01  # distance tolerance of 0.01 nm or 0.1 A to consider sides equal
ANGLE_TOL = 1e-5  # very small tolerance to detect colinear angles

# Global counters
triangle_counts = {
    "equilateral": 0,
    "isosceles": 0,
    "scalene": 0,
    "colinear": 0
}

def read_coordinates(filename):
    with open(filename, 'r') as f:
        return [tuple(map(float, line.strip().split())) for line in f]

def euclidean_distance(p1, p2):
    return math.sqrt(sum((a - b) ** 2 for a, b in zip(p1, p2)))

def vector_subtract(a, b):
    return tuple(ai - bi for ai, bi in zip(a, b))

def dot_product(a, b):
    return sum(ai * bi for ai, bi in zip(a, b))

def vector_length(v):
    return math.sqrt(dot_product(v, v))

def angle_between(v1, v2):
    dot = dot_product(v1, v2)
    len_product = vector_length(v1) * vector_length(v2)
    if len_product == 0:
        return 0.0
    cos_angle = max(min(dot / len_product, 1.0), -1.0)  # clamp for safety
    return math.acos(cos_angle)  # returns angle in radians

def classify_triangle(p1, p2, p3):
    d12 = euclidean_distance(p1, p2)
    d23 = euclidean_distance(p2, p3)
    d31 = euclidean_distance(p3, p1)

    d1_eq_d2 = abs(d12 - d23) < TOLERANCE
    d2_eq_d3 = abs(d23 - d31) < TOLERANCE
    d3_eq_d1 = abs(d31 - d12) < TOLERANCE

    if d1_eq_d2 and d2_eq_d3:
        triangle_counts["equilateral"] += 1
        return "equilateral", d12 + d23 + d31

    elif d1_eq_d2 or d2_eq_d3 or d3_eq_d1:
        # Check angle condition for colinearity
        if d1_eq_d2:
            v1 = vector_subtract(p1, p2)
            v2 = vector_subtract(p3, p2)
        elif d2_eq_d3:
            v1 = vector_subtract(p2, p3)
            v2 = vector_subtract(p1, p3)
        else:
            v1 = vector_subtract(p3, p1)
            v2 = vector_subtract(p2, p1)

        angle = angle_between(v1, v2)
        angle_deg = math.degrees(angle)

        if abs(angle_deg - 180) < ANGLE_TOL:
            triangle_counts["colinear"] += 1
            return "colinear", 0.0
        else:
            triangle_counts["isosceles"] += 1
            return "isosceles", d12 + d23 + d31
    else:
        triangle_counts["scalene"] += 1
        return "scalene", 0.0

def compute_framewise_triangles(com1, com2, com3, label_prefix, mol_label, output_file):
    coords1 = read_coordinates(com1)
    coords2 = read_coordinates(com2)
    coords3 = read_coordinates(com3)

    num_frames = len(coords1)

    with open(output_file, 'a') as f:
        for i in range(num_frames):
            p1 = coords1[i]
            p2 = coords2[i]
            p3 = coords3[i]

            triangle_type, perimeter = classify_triangle(p1, p2, p3)

            if triangle_type in ("equilateral", "isosceles"):
                f.write(f"{label_prefix}: {mol_label}: Frame= {i+1} {triangle_type}, perimeter={perimeter:.5f}\n")

def generate_filenames(prefix, count):
    return [f"{prefix}_{i}.txt" for i in range(1, count + 1)]

def write_statistics(stat_file):
    with open(stat_file, 'w') as f:
        for key in ["equilateral", "isosceles", "colinear", "scalene"]:
            f.write(f"{key} : {triangle_counts[key]}\n")

def main():
    water_files = generate_filenames("water", 111)      # 111 water c.o.m files name as water_"$i".txt
    urea_files = generate_filenames("urea", 133)        # 133 urea c.o.m files name as urea_"$i".txt
    glucose_files = generate_filenames("glucose", 66)   # 66 glucose c.o.m files name as glucose_"$i".txt

    output_file = "triangle_framestat_0.1A.txt" # 0.1A indicates the tolerance used
    stat_file = "triangle_typestat_0.1A.txt"

    open(output_file, 'w').close()
    open(stat_file, 'w').close()

# Only below combinations are possible to make a triangle, either 300 or 210 or 111

    # === 1. Water-Water-Water (WWW) ===
    for i in range(len(water_files)):
        for j in range(i + 1, len(water_files)):
            for k in range(j + 1, len(water_files)):
                label_prefix = "WWW"
                mol_label = f"water_{i+1}, water_{j+1}, water_{k+1}"
                compute_framewise_triangles(
                    water_files[i], water_files[j], water_files[k],
                    label_prefix, mol_label, output_file
                )


    # === Write final stats ===
    write_statistics(stat_file)

if __name__ == "__main__":
    main()

