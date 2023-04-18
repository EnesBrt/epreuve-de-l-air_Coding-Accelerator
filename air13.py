import os, sys
import subprocess


def test_air00(file_name):
    result = subprocess.run(["python", file_name, "Bonjour les gars", " "], capture_output=True, text=True)
    output = result.stdout.strip()

    output_lines = output.split('\n')

    # Remove the list representation from the output_lines
    output_lines.pop(0)

    expected_output = ["Bonjour", "les", "gars"]
    success = output_lines == expected_output

    if not success:
        print(f"Output: {output_lines}")
        print(f"Expected output: {expected_output}")

    return success, output


def test_air01(file_name):
    result = subprocess.run(["python", file_name, "Crevette magique dans la mer des étoiles", "la"],
                            capture_output=True, text=True)
    output = result.stdout.strip()

    output_lines = output.split('\n')

    expected_output = ["Crevette magique dans ", "mer des étoiles"]
    success = output_lines == expected_output

    if not success:
        print(f"Output: {output_lines}")
        print(f"Expected output: {expected_output}")

    return success, output


def test_air02(file_name):
    result = subprocess.run(["python", file_name, "je", "teste", "des", "trucs", " "], capture_output=True, text=True)
    output = result.stdout.strip()

    expected_output = "je teste des trucs"
    success = output == expected_output

    if not success:
        print(f"Output: {output}")
        print(f"Expected output: {expected_output}")

    return success, output


def test_air03(file_name):
    result = subprocess.run(["python", file_name, "1", "2", "3", "4", "5", "4", "3", "2", "1"], capture_output=True,
                            text=True)
    output = result.stdout.strip()

    expected_output = "5"
    success = output == expected_output

    if not success:
        print(f"Output: {output}")
        print(f"Expected output: {expected_output}")

    return success, output


def test_air04(file_name):
    result = subprocess.run(["python", file_name, "Hello milady,   bien ou quoi ??"], capture_output=True, text=True)
    output = result.stdout.strip()

    expected_output = "Helo milady, bien ou quoi ?"
    success = output == expected_output

    if not success:
        print(f"Output: {output}")
        print(f"Expected output: {expected_output}")

    return success, output


def test_air05(file_name):
    result = subprocess.run(["python", file_name, "1", "2", "3", "4", "5", "+2"], capture_output=True, text=True)
    output = result.stdout.strip()

    expected_output = "3 4 5 6 7"
    success = output == expected_output

    if not success:
        print(f"Output: {output}")
        print(f"Expected output: {expected_output}")

    return success, output


def test_air06(file_name):
    result = subprocess.run(["python", file_name, "Michel", "Albert", "Thérèse", "Benoit", "t"], capture_output=True,
                            text=True)
    output = result.stdout.strip()

    output_lines = output.split('\n')

    expected_output = ["Michel"]
    success = output_lines == expected_output

    if not success:
        print(f"Output: {output_lines}")
        print(f"Expected output: {expected_output}")

    return success, output


def test_air07(file_name):
    result = subprocess.run(["python", file_name, "1", "3", "4", "2"], capture_output=True, text=True)
    output = result.stdout.strip()

    expected_output = "1 2 3 4"
    success = output == expected_output

    if not success:
        print(f"Output: {output}")
        print(f"Expected output: {expected_output}")

    return success, output


def test_air08(file_name):
    result = subprocess.run(["python", file_name, "10", "20", "30", "fusion", "15", "25", "35"], capture_output=True,
                            text=True)
    output = result.stdout.strip()

    expected_output = "10 15 20 25 30 35"
    success = output == expected_output

    if not success:
        print(f"Output: {output}")
        print(f"Expected output: {expected_output}")

    return success, output


def test_air09(file_name):
    result = subprocess.run(["python", file_name, "Michel", "Albert", "Thérèse", "Benoit"], capture_output=True,
                            text=True)
    output = result.stdout.strip()

    expected_output = "Albert, Thérèse, Benoit, Michel"
    success = output == expected_output

    if not success:
        print(f"Output: {output}")
        print(f"Expected output: {expected_output}")

    return success, output


def test_air10(file_name):
    # Create a temporary file with content to test the air10.py script
    test_file_name = "temp_test_file.txt"
    test_file_content = "Je danse le mia"

    with open(test_file_name, "w") as test_file:
        test_file.write(test_file_content)

    result = subprocess.run(["python", file_name, test_file_name], capture_output=True, text=True)
    output = result.stdout.strip()

    expected_output = test_file_content
    success = output == expected_output

    if not success:
        print(f"Output: {output}")
        print(f"Expected output: {expected_output}")

    # Remove the temporary test file after the test is done
    os.remove(test_file_name)

    return success, output


def test_air11(file_name):
    result = subprocess.run(["python", file_name, "O", "5"], capture_output=True, text=True)
    output = result.stdout.strip()

    output_lines = output.split('\n')

    expected_output = [
        "    O",
        "   OOO",
        "  OOOOO",
        " OOOOOOO",
        "OOOOOOOOO",
    ]
    success = output_lines == expected_output

    if not success:
        print(f"Output: {output_lines}")
        print(f"Expected output: {expected_output}")

    return success, output


def test_air12(file_name):
    result = subprocess.run(["python", file_name, "6", "5", "4", "3", "2", "1"], capture_output=True, text=True)
    output = result.stdout.strip()

    output_numbers = output.split(' ')

    expected_output = ["1", "2", "3", "4", "5", "6"]
    success = output_numbers == expected_output

    if not success:
        print(f"Output: {output_numbers}")
        print(f"Expected output: {expected_output}")

    return success, output


test_functions = {
    "air00.py": test_air00,
    "air01.py": test_air01,
    "air02.py": test_air02,
    "air03.py": test_air03,
    "air04.py": test_air04,
    "air05.py": test_air05,
    "air06.py": test_air06,
    "air07.py": test_air07,
    "air08.py": test_air08,
    "air09.py": test_air08,
    "air10.py": test_air08,
    "air11.py": test_air08,
    "air12.py": test_air08,
}

path = "/Users/enesbarut/Documents/epreuve-de-l-air_Coding-Accelerator"
dirs = os.listdir(path)

total_success = 0
total_tests = 0

dirs.sort()

for file in dirs:
    if "air00.py" <= file <= "air12.py" and os.path.isfile(os.path.join(path, file)):
        if file in test_functions:
            test_function = test_functions[file]  # Get the test function for the current file
            success, output = test_function(os.path.join(path, file))
            total_success += int(success)
            total_tests += 1
            status = "success" if success else "failure"
            print(f"{file} ({total_tests}): {status}")

print(f"Total success: ({total_success}/{total_tests})")

# Update the total number of successful tests and the total number of tests.
# Print the test result in the desired format.
