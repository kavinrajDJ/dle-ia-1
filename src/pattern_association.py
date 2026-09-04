import os
import glob
import re
import pandas as pd
import matplotlib.pyplot as plt


# ==================================================
# 1. Pattern and command information
# ==================================================

patterns = [
    ("OPEN_HAND", "HELLO"),
    ("FIST", "STOP"),
    ("THUMBS_UP", "YES"),
    ("THUMBS_DOWN", "NO"),
    ("PEACE_SIGN", "PEACE"),
    ("OPEN_HAND", "HELLO"),
    ("FIST", "STOP"),
    ("THUMBS_UP", "YES"),
    ("THUMBS_DOWN", "NO"),
    ("PEACE_SIGN", "PEACE")
]


# ==================================================
# 2. Find screenshot images
# ==================================================

image_folder = "dataset/images"

image_files = []

for extension in ["*.png", "*.jpg", "*.jpeg"]:
    image_files.extend(
        glob.glob(os.path.join(image_folder, extension))
    )


# ==================================================
# 3. Sort screenshots using filename time
# ==================================================

def get_time(filename):
    match = re.search(
        r"(\d{6})\.(png|jpg|jpeg)$",
        filename,
        re.IGNORECASE
    )

    if match:
        return int(match.group(1))

    return 0


image_files.sort(key=get_time)


# ==================================================
# 4. Check images
# ==================================================

if len(image_files) != 10:
    print("ERROR: Exactly 10 images are required.")
    print("Images found:", len(image_files))
    exit()

print("10 images found successfully.")


# ==================================================
# 5. Create training data
# ==================================================

data = []

for i in range(10):

    data.append({
        "Pattern_ID": i + 1,
        "Image": os.path.basename(image_files[i]),
        "Hand_Pattern": patterns[i][0],
        "Command_Symbol": patterns[i][1]
    })


df = pd.DataFrame(data)


# ==================================================
# 6. Display training data
# ==================================================

print("\n==============================================")
print("       SIGN LANGUAGE PATTERN ASSOCIATION")
print("==============================================")

print("\nTraining Data")
print("----------------------------------------------")

print(df.to_string(index=False))


# ==================================================
# 7. Learn pattern associations
# ==================================================

association = {}

for _, row in df.iterrows():

    association[row["Hand_Pattern"]] = row["Command_Symbol"]


print("\nLearned Associations")
print("----------------------------------------------")

for pattern, command in association.items():

    print(pattern, "->", command)


# ==================================================
# 8. Test a new input pattern
# ==================================================

new_input = "OPEN_HAND"

predicted_command = association.get(new_input)


print("\nNew Input")
print("----------------------------------------------")

print("Hand Pattern:", new_input)

print("\nPredicted Command:")
print(predicted_command)


# ==================================================
# 9. Check correct association
# ==================================================

expected_command = "HELLO"

print("\nExpected Command:")
print(expected_command)


if predicted_command == expected_command:

    print("\nAssociation Status: CORRECT")

else:

    print("\nAssociation Status: INCORRECT")


# ==================================================
# 10. Test incorrect association
# ==================================================

wrong_command = "STOP"

print("\nIncorrect Association Test")
print("----------------------------------------------")

print("Hand Pattern:", new_input)
print("Given Command:", wrong_command)


if association.get(new_input) != wrong_command:

    print("Result: INCORRECT ASSOCIATION DETECTED")

else:

    print("Result: Association is correct")


# ==================================================
# 11. Create Pattern Association Visualization
# ==================================================

output_folder = "results"

os.makedirs(output_folder, exist_ok=True)


# Count each pattern
pattern_counts = df["Hand_Pattern"].value_counts()


plt.figure(figsize=(10, 6))

plt.bar(
    pattern_counts.index,
    pattern_counts.values
)

plt.title("Sign Language Pattern Association")

plt.xlabel("Hand Pattern")

plt.ylabel("Number of Training Samples")

plt.xticks(rotation=30)

plt.tight_layout()


# IMPORTANT: Required output filename
output_file = os.path.join(
    output_folder,
    "pattern_association.png"
)

plt.savefig(output_file)

plt.show()


# ==================================================
# 12. Final Result
# ==================================================

print("\n==============================================")
print("                 FINAL RESULT")
print("==============================================")

print("Input Pattern :", new_input)
print("Command       :", predicted_command)
print("Status        : Association Successfully Identified")

print("\nOutput image saved as:")
print(output_file)

print("\nProgram completed successfully!")