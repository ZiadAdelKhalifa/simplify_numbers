# Text Simplification and Figurative Comparisons

This project simplifies numerical data in text and enhances it with figurative comparisons and contextual explanations to make the content more relatable and engaging.

## Features

1. **Number Simplification**:
   - Rounds large numbers to a more readable format.
   - Handles percentages and converts them into approximate textual representations (e.g., "90% → fast alle").
   - Simplifies years based on their context.

2. **Figurative Comparisons**:
   - Adds contextual comparisons for better understanding (e.g., "1 Million Euro → So viel Geld, dass man 100 Autos kaufen könnte").

3. **Contextual Handling**:
   - Recognizes and retains the context of years and months.
   - Adjusts decimal numbers to round values or descriptive terms.

## How It Works

1. **`simplify_numbers(raw_text)`**:
   - Detects and processes large numbers, percentages, years, and decimals.
   - Retains contextual elements like specific years or months while simplifying numerical values.

2. **`add_figurative_comparisons_and_contextual_explanations(text)`**:
   - Maps numerical values to relatable comparisons (e.g., weights, amounts, or time durations).

3. **`apply_rules_4_and_5(text)`**:
   - Combines simplifications and figurative explanations for a final enhanced output.

