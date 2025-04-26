import os
import pyzipper

password = {
    "VII-01" : "hello",
    "VII-02" : "world",
}

def zip_folder_with_password(folder_path, zip_name=None, password=None):
    """
    Zips the specified folder into a password-protected .zip file.

    Args:
        folder_path (str): The path to the folder to be zipped.
        zip_name (str, optional): The name of the resulting zip file. Defaults to the folder name with '.zip'.
        password (str, optional): The password for the zip file. If None, no password will be set.
    """
    # Default zip name to folder name with .zip
    if zip_name is None:
        zip_name = os.path.basename(folder_path.rstrip(os.sep)) + ".zip"
    
    # Convert password to bytes
    password_bytes = password.encode() if password else None

    # Create the zip file
    with pyzipper.AESZipFile(zip_name, 'w', compression=pyzipper.ZIP_DEFLATED, encryption=pyzipper.WZ_AES) as zipf:
        if password_bytes:
            zipf.setpassword(password_bytes)
        
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                # Create the complete filepath
                file_path = os.path.join(root, file)
                prin(file_path)
                # Add file to the zip, preserving the 'Outer Folder' structure
                arcname = os.path.relpath(file_path, start=os.path.dirname(folder_path))
                zipf.write(file_path, arcname)
    
        print(f"Folder '{folder_path}' has been zipped as '{zip_name}' with password protection.")


n = input("Input the path : ").replace("\"","")
os.chdir(n)

for key in password:
    # Example Usage
    folder_to_zip = key  # Replace with your folder path
    zip_password = password[key]  # Replace with your desired password
    zip_folder_with_password(folder_to_zip, password=zip_password)
