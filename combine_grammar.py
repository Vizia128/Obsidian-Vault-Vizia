import os
import sys


def combine_grammar_files():
    """
    Combines all markdown files in the '문법' folder into a single markdown file.
    """
    try:
        # Define paths
        grammar_folder = "문법"
        output_file = "combined_grammar.md"

        # Check if the grammar folder exists
        if not os.path.exists(grammar_folder):
            print(f"Error: The folder '{grammar_folder}' does not exist.")
            return False

        # Get list of markdown files
        try:
            files = os.listdir(grammar_folder)
        except PermissionError:
            print(f"Error: Permission denied when accessing '{grammar_folder}' folder.")
            return False

        # Filter for markdown files and sort them
        md_files = [f for f in files if f.endswith(".md")]
        md_files.sort()

        if not md_files:
            print(f"No markdown files found in '{grammar_folder}' folder.")
            return False

        print(f"Found {len(md_files)} markdown files to combine.")

        # Combine content from all files
        combined_content = "# Korean Grammar Patterns\n\n"

        for filename in md_files:
            filepath = os.path.join(grammar_folder, filename)

            try:
                with open(filepath, "r", encoding="utf-8") as file:
                    content = file.read()

                    # Add section header with filename (without .md extension)
                    section_title = filename[:-3]  # Remove .md extension
                    combined_content += f"---\n\n## {section_title}\n\n"

                    # Add the file content
                    combined_content += content + "\n\n"

            except UnicodeDecodeError:
                print(
                    f"Warning: Could not read '{filename}' due to encoding issues. Skipping."
                )
                continue
            except PermissionError:
                print(
                    f"Warning: Permission denied when reading '{filename}'. Skipping."
                )
                continue
            except Exception as e:
                print(f"Warning: Error reading '{filename}': {str(e)}. Skipping.")
                continue

        # Write the combined content to the output file
        try:
            with open(output_file, "w", encoding="utf-8") as file:
                file.write(combined_content)
            print(
                f"Successfully created '{output_file}' with {len(md_files)} grammar patterns."
            )
            return True

        except PermissionError:
            print(f"Error: Permission denied when writing to '{output_file}'.")
            return False
        except Exception as e:
            print(f"Error writing to '{output_file}': {str(e)}")
            return False

    except Exception as e:
        print(f"Unexpected error: {str(e)}")
        return False


if __name__ == "__main__":
    success = combine_grammar_files()
    sys.exit(0 if success else 1)
