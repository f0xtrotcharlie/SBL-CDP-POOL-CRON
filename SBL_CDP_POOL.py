import urllib.request
import datetime
import shutil
import os

# URL of the file to be downloaded
url = "https://www1.cdp.sgx.com/sgx-cdp-web/lendingpool/downloadXLS"

# Get the current date to use in the new filename
date = datetime.datetime.now().strftime("%d-%m-%Y")

# Define the save path for the downloaded file
save_path = "D:/Google Drive/Python_projects/Download_SBL_list/SBL"

# Download the file and save it with the new filename in the save path
urllib.request.urlretrieve(url, os.path.join(save_path, f"{date}_SBL.xls"))

# Define the path to copy the renamed file to
copy_path = "D:/Dropbox/DATA/SBL"

# Copy the renamed file to the copy path
shutil.copy(os.path.join(save_path, f"{date}_SBL.xls"), os.path.join(copy_path, f"{date}_SBL.xls"))