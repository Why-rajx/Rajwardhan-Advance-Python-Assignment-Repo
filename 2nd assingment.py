from datetime import datetime

# ---------------- Decorator ----------------
def report_header_footer(func):
    """Decorator to add header and footer to the report."""
    def wrapper(*args, **kwargs):
        print("=" * 50)
        print("          DYNAMIC REPORT GENERATOR")
        print("=" * 50)
        func(*args, **kwargs)
        print("=" * 50)
        print("           END OF REPORT")
        print("=" * 50)
    return wrapper


# ---------------- Report Class ----------------
class Report:

    # Class Variable
    report_count = 0

    # Constructor (Magic Method)
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.content = []
        Report.report_count += 1

    # Magic Method: String Representation
    def __str__(self):
        return f"Report Title: {self.title}\nAuthor: {self.author}"

    # Magic Method: Length of Report
    def __len__(self):
        return len(self.content)

    # Add report section
    def add_section(self, heading, text):
        self.content.append((heading, text))

    # Decorated Method
    @report_header_footer
    def generate(self):
        print(self)
        print(f"Generated On: {datetime.now()}")
        print()

        for heading, text in self.content:
            print(f"{heading}")
            print("-" * len(heading))
            print(text)
            print()

    # Class Method
    @classmethod
    def total_reports(cls):
        print(f"Total Reports Created: {cls.report_count}")


# ---------------- Main Program ----------------

# Create Report
report = Report("Student Performance Report", "Kumar.Rajwardhan Jagtap")

# Add Sections
report.add_section(
    "Introduction",
    "This report summarizes the academic performance of students."
)

report.add_section(
    "Performance Analysis",
    "The average result is 72%. Attendance has improved significantly."
)

report.add_section(
    "Recommendations",
    "Students should focus on regular practice, improve time management, "
    "participate in practical activities, and seek guidance in weaker subjects "
    "to achieve better academic performance."
)

report.add_section(
    "Conclusion",
    "Overall performance is satisfactory. More focus is needed on practical skills."
)

# Generate Report
report.generate()

# Magic Method (__len__)
print("Number of Sections:", len(report))

# Class Method
Report.total_reports()