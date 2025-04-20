import os
import pyzipper

def zip_folder_with_password(folder_path, output_zip, password):
    """
    Zips a folder with a password.

    :param folder_path: Path to the folder to zip
    :param output_zip: Output zip file name (with .zip extension)
    :param password: Password for the zip file
    """
    with pyzipper.AESZipFile(output_zip, 'w', compression=pyzipper.ZIP_LZMA) as zip_file:
        zip_file.setpassword(password.encode('utf-8'))
        zip_file.setencryption(pyzipper.WZ_AES)
        
        for root, dirs, files in os.walk(folder_path):
            print(root,dirs,files)
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, start=folder_path)
                zip_file.write(file_path, arcname)

    print(f"Folder '{folder_path}' has been zipped into '{output_zip}' with a password.")

# Example usage
folder_to_zip = "testing"
output_zip_file = "protected_folder.zip"
password = "mypassword123"

zip_folder_with_password(folder_to_zip, output_zip_file, password)
