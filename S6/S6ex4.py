def cube_volume(edge):
    """Calculate cube volume in liters."""
    # 1 m3 = 1000 litri
    return edge ** 3 * 1000

def convert_to_m3(liters):
    """Convert liters in m3."""
    return liters / 1000


edge = int(input("muchia:"))
print("Volumul cubului:", convert_to_m3(cube_volume(edge)) ,"m3")

# Ierarhie de apelare
# 1 cube_volume
# 2 convert_volume
# 3 print

