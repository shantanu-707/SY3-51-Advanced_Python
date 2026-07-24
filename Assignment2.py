# Decorators
def bold(func):
    def wrapper(self):
        return "** " + func(self) + " **"

    return wrapper


def add_border(func):
    def wrapper(self):
        text = func(self)
        border = "=" * (len(text) + 4)
        return border + "\n| " + text + " |\n" + border

    return wrapper


def log_call(func):
    def wrapper(self):
        print("\n[LOG] summary() function called")
        return func(self)

    return wrapper


# Formatter
class Formatter:
    def __call__(self, text):
        return text.upper()


# Report Section
class ReportSection:
    def __init__(self, heading):
        self.heading = heading
        self.content = ""

    def set_content(self, content):
        self.content = content

    def __str__(self):
        return f"--- {self.heading} ---\n{self.content}"


# Report
class Report:
    templates = {}

    @classmethod
    def register_template(cls, name, headings):
        cls.templates[name] = headings

    @classmethod
    def from_template(cls, name):
        report = cls(name, "Unknown")
        if name in cls.templates:
            for heading in cls.templates[name]:
                report.add_section(ReportSection(heading))
        return report

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.sections = []

    def add_section(self, section):
        self.sections.append(section)

    @bold
    def title_line(self):
        return self.title + " | Author : " + self.author

    @log_call
    @add_border
    def summary(self):
        return "Total Sections : " + str(len(self.sections))

    def __str__(self):
        text = self.title_line() + "\n\n"
        for section in self.sections:
            text += str(section) + "\n\n"
        return text.strip()

    def __len__(self):
        return len(self.sections)

    def __getitem__(self, index):
        return self.sections[index]

    def __iter__(self):
        return iter(self.sections)

    def __add__(self, other):
        new_report = Report(
            self.title + " & " + other.title,
            self.author + " & " + other.author
        )
        new_report.sections = self.sections + other.sections
        return new_report

    def __eq__(self, other):
        return self.title == other.title


# Main Program
print("=" * 40)
print("       DYNAMIC REPORT GENERATOR")
print("=" * 40)

Report.register_template(
    "Student Report",
    ["Introduction", "Results", "Conclusion"]
)

Report.register_template(
    "Project Report",
    ["Abstract", "Methodology", "Outcome"]
)

print("\nAvailable Templates:")
for template in Report.templates:
    print(f"  • {template}")

template_name = input("\nEnter template name : ").title()

if template_name not in Report.templates:
    print(f'\n[Error] Template "{template_name}" does not exist. Please choose a valid template.')
    exit()

report = Report.from_template(template_name)
report.author = input("Enter author name : ")

print("\n" + "-" * 40)
print(" ENTER SECTION CONTENT ")
print("-" * 40)
for section in report:
    content = input(f"Content for [{section.heading}] : ")
    section.set_content(content)

print("\n" + "-" * 40)
print(" FORMATTING OPTIONS ")
print("-" * 40)
print("  1. Bold Title")
print("  2. Uppercase Report")
print("  3. Bordered Summary")

choice = int(input("\nEnter your choice (1-3) : "))

print("\n" + "=" * 40)
print("               OUTPUT")
print("=" * 40 + "\n")

if choice == 1:
    print(report)

elif choice == 2:
    formatter = Formatter()
    print(formatter(str(report)))

elif choice == 3:
    print(report.summary())

print("\n" + "-" * 40)
print(" REPORT METADATA ")
print("-" * 40)
print(f"Number of Sections : {len(report)}")
print(f"\nFirst Section:\n{report[0]}")

print("\nIterating Through Section Headings:")
for sec in report:
    print(f"  ➜ {sec.heading}")

report2 = Report("Extra Report", "Admin")
report2.add_section(ReportSection("Extra Section"))

combined = report + report2
print(f"\nCombined Report has {len(combined)} sections.")

if report == report2:
    print("Comparison: Both reports have the same title.")
else:
    print("Comparison: Reports have different titles.")
print("=" * 40)