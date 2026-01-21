class Height(object):
    def __init__(self, feet, inches):
        self.feet = feet
        self.inches = inches

    def __str__(self):
        return str(self.feet) + " feet, " + str(self.inches) + " inches"

    # Greater than >
    def __gt__(self, other):
        total_inches = self.feet * 12 + self.inches
        other_total_inches = other.feet * 12 + other.inches
        return total_inches > other_total_inches

    # Greater than or equal to >=
    def __ge__(self, other):
        total_inches = self.feet * 12 + self.inches
        other_total_inches = other.feet * 12 + other.inches
        return total_inches >= other_total_inches

    # Not equal to !=
    def __ne__(self, other):
        total_inches = self.feet * 12 + self.inches
        other_total_inches = other.feet * 12 + other.inches
        return total_inches != other_total_inches


# Test cases
print(Height(4, 6) > Height(4, 5))
print(Height(4, 5) >= Height(4, 5))
print(Height(5, 9) != Height(5, 10))