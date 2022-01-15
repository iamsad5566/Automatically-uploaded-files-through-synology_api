from operator import truediv
from synology_api import filestation


class SynologyAPI:

    # Constructer
    # Build up file station
    def __init__(self):
        self.fs = filestation.FileStation('', '', '', '',
                                          secure=True, cert_verify=False, dsm_version=7, debug=True, otp_code=None)
        self.projectName = ""
        self.fileNameAndPath = ""
        self.type = ""

    # Upload file
    def upload(self, projectName, fileNameAndPath, type):
        self.projectName = projectName
        self.fileNameAndPath = fileNameAndPath
        self.type = type

        # Check if the folder exists first
        fileExist = False
        parentPath = "/" + self.type
        folderList = self.fs.get_file_list(parentPath)["data"]["files"]

        for i in folderList:
            if self.projectName in i.get("path"):
                print("Folder exists!")
                fileExist = True
                break

        # If not, create the folder
        if fileExist == False:
            print("Created the folder!")
            self.fs.create_folder("/"+self.type, self.projectName)

        # Create a variable for saving the target of the upload file
        destination = "/" + self.type + "/" + self.projectName
        self.fs.upload_file(destination, self.fileNameAndPath)
        print("Successfully uploaded!")
