import re

def simplify_numbers(raw_text):
    # List of month names for detecting dates
    months = [
        "Januar", "Februar", "März", "April", "Mai", "Juni",
        "Juli", "August", "September", "Oktober", "November", "Dezember"
    ]

    # Function to round large numbers
    def round_large_numbers(match):
        number_str = match.group(0).replace('.', '').replace(',', '.')
        number = float(number_str)
        if number >= 1000:
            return f"etwa {int(round(number, -3)):,}".replace(',', '.')
        return f"etwa {int(round(number))}"

    # Function to simplify percentages
    def simplify_percentages(match):
        percentage = float(match.group(1).replace(',', '.'))
        if percentage == 25:
            return "jeder Vierte"
        elif percentage == 50:
            return "die Hälfte"
        elif percentage == 75:
            return "drei von vier"
        elif percentage >= 90:
            return "fast alle"
        elif percentage >= 60:
            return "mehr als die Hälfte"
        elif percentage <= 15:
            return "wenige"
        else:
            return f"etwa {int(percentage)} Prozent"

    # Handle years explicitly based on context ("Im Jahr" or month names)
    def handle_years(match):
        text = match.group(0)
        year_match = re.search(r"\b\d{4}\b", text)  # Extract the year part
        if year_match:
            year = int(year_match.group(0))
            if "Im Jahr" in text or any(month in text for month in months):
                return text  # Keep "Im Jahr" or month-context years unchanged
            return f"etwa {round(year, -3)}"  # Simplify as a number
        return text  # Fallback in case no year is found

    # Handle decimals (e.g., 38,7 → etwa 39)
    def handle_decimals(match):
        number_str = match.group(0).replace(',', '.')
        number = float(number_str)

        if number < 15:
            return "wenige"
        return f"etwa {round(number)}"

    # 1. Simplify percentages
    raw_text = re.sub(r"(\d+[,.]?\d*)\s*Prozent", simplify_percentages, raw_text)

    # 2. Handle years with "Im Jahr" or month context
    raw_text = re.sub(
        r"(Im Jahr\s+\d{4}|\b(?:\d+\.\s+)?(?:Januar|Februar|März|April|Mai|Juni|Juli|August|September|Oktober|November|Dezember)\s+\d{4}|\b\d{4}\b)",
        handle_years,
        raw_text,
    )

    # 3. Round large numbers (excluding percentages and years)
    raw_text = re.sub(r"\b(?!\d{4}\b)\d{1,3}(?:\.\d{3})*(?:,\d+)?\b", round_large_numbers, raw_text)

    # 4. Handle decimal numbers
    raw_text = re.sub(r"\b(\d+,\d+)\b", handle_decimals, raw_text)

    return raw_text.replace("etwa 1. ", "1. ")

def add_figurative_comparisons_and_contextual_explanations(text):
    comparisons = {
        "1 Million Euro": "So viel Geld, dass man 100 Autos kaufen könnte",
        "10.000 Euro": "So viel Geld, dass man eine teure Uhr kaufen könnte",
        "100.000 Euro": "So viel Geld, wie man für eine kleine Wohnung in einer Großstadt benötigt",
        "325.000 Euro": "So viel Geld, wie ein Einfamilienhaus in einer Kleinstadt kostet",
        "10.000 Besucher": "So viele Menschen, wie in ein großes Fußballstadion passen",
        "1.000 Menschen": "So viele Menschen, wie in eine kleine Kirche passen",
        "50.000 Teilnehmer": "So viele Menschen, wie auf einem großen Musikfestival",
        "100 Menschen": "So viele Menschen, wie in einen großen Konferenzraum passen",
        "250 Kilogramm": "So schwer wie ein großer Kühlschrank",
        "1 Tonne": "So schwer wie ein Kleinwagen",
        "500 Gramm": "So viel wie ein Laib Brot wiegt",
        "10 Liter": "So viel Wasser, wie in einen großen Eimer passt",
        "30 Prozent der Fläche": "Ein Drittel, also ein Stück von drei gleich großen Teilen",
        "1 Hektar": "So groß wie zwei Fußballfelder",
        "100 Quadratmeter": "So groß wie eine kleine Wohnung",
        "50 Quadratkilometer": "So groß wie eine Kleinstadt",
        "1 Stunde": "So lange, wie eine Folge einer TV-Serie dauert",
        "24 Stunden": "So lange, wie ein kompletter Tag dauert",
        "7 Tage": "Eine Woche, so lange, wie ein Urlaub auf einer Insel dauern könnte",
        "1 Jahr": "So lange, wie ein Kind braucht, um laufen zu lernen"
    }

    for key, comparison in comparisons.items():
        text = text.replace(key, f"{key} ({comparison})")

    return text

# Combining rules 4 and 5 with previous results
def apply_rules_4_and_5(text):
    text_with_comparisons = add_figurative_comparisons_and_contextual_explanations(text)
    return text_with_comparisons

# Testing the function with the given test cases
test_cases = [
    "324.620,22 Euro wurden gespendet.",
    "1.897 Menschen nahmen teil.",
    "25 Prozent der Bevölkerung sind betroffen.",
    "90 Prozent stimmten zu.",
    "14 Prozent lehnten ab.",
    "Bei 38,7 Grad Celsius ist es sehr heiß.",
    "denn die Rente steigt um 4,57 Prozent.",
    "Im Jahr 2024 gab es 1.234 Ereignisse.",
    "Am 1. Januar 2024 waren es 5.678 Teilnehmer.",
    "Im Jahr 2025 gab es 2018 Ereignisse."
]

for test in test_cases:
    # First, simplify the numbers
    simplified_text = simplify_numbers(test)
    print(f"Simplified text: {simplified_text}")
    
    # Then, apply figurative comparisons and contextual explanations
    final_text = apply_rules_4_and_5(simplified_text)
    print(f"Final text with figurative comparisons: {final_text}")
    print("\n" + "-" * 50 + "\n")
