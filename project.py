import argparse, sys
import face_recognition
import shutil

from pathlib import Path

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("--face", help="Path to the face you want to use as reference (.jpeg or .png)", required=True)
    parser.add_argument("--source", help="Path to the folder where the pictures you want to analyze are", required=True)
    parser.add_argument("--output", help="Path to the folder where you want to copy the pictures to", required=True)

    args = parser.parse_args()

    tolerance = input("Set the tolerance for face recognition (Distance between faces to consider it a match. Lower is more strict. 0.6 is typical best performance.): ")

    file_extensions = (".jpeg", ".jpg", ".png")

    # Convert to Path objects for cleaner manipulation
    known_face = Path(args.face)
    source_folder = Path(args.source)
    destination_folder = Path(args.output)

    # Check if the source folder and file exist
    if not source_folder.exists() or not known_face.exists():
        raise FileNotFoundError(f"Check if {known_face} and {source_folder} exist")

    # Check if the face is an image file
    if not known_face.is_file() or known_face.suffix.lower() not in file_extensions:
        print("The face needs to be an image file (.jpeg or .png).")
        sys.exit(1)

    # Ensure destination folder exists
    destination_folder.mkdir(parents=True, exist_ok=True)
        
    source_pic = face_recognition.load_image_file(known_face)
    source_face_encoding = face_recognition.face_encodings(source_pic)[0]
    # source_face_encoding contains a universal 'encoding' of facial features that can be compared to any other picture of a face

    count_pics = 0

    # Iterate through files in the source folder, compare and copy the pictures
    # that matches the face to destination folder
    for file_path in source_folder.iterdir():
        if file_path.is_file() and file_path.suffix.lower() in file_extensions:
            if compare(source_face_encoding, file_path, float(tolerance)):
                count_pics = count_pics + 1
                try:
                    destination_path = destination_folder / file_path.name
                    shutil.copy2(file_path, destination_path)
                    print(f"Copied: {file_path.name}\n")
                except Exception as e:
                    print(f"Failed to copy {file_path.name}: {e}")
    
    print(f"Copied {count_pics} picture(s) to {args.output}.")


def compare(source_image, image, tol):
    unknown_picture = face_recognition.load_image_file(image)
    unknown_face_encoding = face_recognition.face_encodings(unknown_picture)

    # Comparing faces
    for face in unknown_face_encoding:
        results = face_recognition.compare_faces([source_image], face, tolerance=tol)
        if results[0] == True:
            print("It's a match!")            
            return True
    return False

main()