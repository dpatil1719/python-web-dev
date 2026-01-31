class Height(object):
    def __init__(self, feet, inches):
        self.feet = feet
        self.inches = inches

    def __str__(self):
        return str(self.feet) + " feet, " + str(self.inches) + " inches"

    def __sub__(self, other):
        # Convert both heights to total inches
        height_a_inches = self.feet * 12 + self.inches
        height_b_inches = other.feet * 12 + other.inches

        # Subtract the heights
        total_inches = height_a_inches - height_b_inches

        # Convert back to feet and inches
        output_feet = total_inches // 12
        output_inches = total_inches - (output_feet * 12)

        # Return a new Height object
        return Height(output_feet, output_inches)


# Test the subtraction
person_A_height = Height(5, 10)
person_B_height = Height(3, 9)

height_difference = person_A_height - person_B_height

print("Height difference:", height_difference)