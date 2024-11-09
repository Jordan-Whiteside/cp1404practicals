"""Project class."""

class Project:
    """Project class."""

    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        """Constructor for a Project object."""
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __str__(self):
        """String representation of a project object."""
        return f"{self.name}, Start date: {self.start_date}, Priority: {self.priority}, Estimated cost: ${self.cost_estimate}, Completion percentage: %{self.completion_percentage}"

def run_tests():
    # text file attributes string, dd/mm/yyyy, int, float, percentage e.g. 55
    p1 = Project("Jordan", "12/08/2003", 1,100, 0)
    print(p1)

if __name__ == '__main__':
    run_tests()