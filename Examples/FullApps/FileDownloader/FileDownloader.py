import tkinter as tk
from pathlib import Path
from threading import Thread

# noinspection PyPackageRequirements
import requests
# noinspection PyPackageRequirements
from requests import HTTPError

from TkZero.Button import Button
from TkZero.Dialog import select_directory, show_info, show_error, ask_ok_or_cancel, CustomDialog
from TkZero.Entry import Entry
from TkZero.Frame import Frame
from TkZero.Label import Label
from TkZero.MainWindow import MainWindow
from TkZero.Progressbar import Progressbar

# Create a main window
root = MainWindow()
root.title = "File downloader"

# Create a frame to hold the stuff related to the URL
url_frame = Frame(root)
url_frame.grid(row=0, column=0, sticky=tk.NW)

# Create a label to label the entry that will contain the URL
url_label = Label(url_frame, text="URL: ")
url_label.grid(row=0, column=0, padx=1, pady=1, sticky=tk.NW)

# Create a entry that will contain the URL
url_entry = Entry(url_frame, width=50)
url_entry.grid(row=0, column=1, padx=1, pady=1, sticky=tk.NW)

# Create a frame to hold the stuff related to the download location
path_frame = Frame(root)
path_frame.grid(row=1, column=0, sticky=tk.NW)

# Create a label to label the file path to download the file to
path_label = Label(path_frame, text="Download location: ")
path_label.grid(row=0, column=0, padx=1, pady=1, sticky=tk.NW)

# Create an entry to hold the file path
path_entry = Entry(path_frame, width=24)
path_entry.grid(row=0, column=1, padx=1, pady=1, sticky=tk.NW)


# Create a function to browse for a download path
def browse():
    path = select_directory(title="Select a download location")
    if path:
        path_entry.value = str(path)


# Create a button to browse for a file path
path_btn = Button(path_frame, text="Browse...", command=browse)
path_btn.grid(row=0, column=2, padx=1, pady=1, sticky=tk.NW)


# Create a function to start the download process
def download():
    # Make sure the URL entry is not empty
    if len(url_entry.value) == 0:
        show_error(root, title="File Downloader: Error!", message="Please fill in a URL to download!")
        return
    # Make sure the download location entry is not empty
    if len(path_entry.value) == 0:
        show_error(root, title="File Downloader: Error!", message="Please fill in a download location!")
        return
    # Make the download location absolute
    path_entry.value = str(Path(path_entry.value).expanduser().resolve())
    # Make sure the download location is valid
    if not Path(path_entry.value).exists():
        show_error(root, title="File Downloader: Error!", message=f"The path:\n{path_entry.value}\ndoes not exist!")
        return
    url = url_entry.value
    # Make a custom dialog
    dlg = CustomDialog(root)
    dlg.title = f"File Downloader: Downloading {url}..."
    # Make the label that shows the URL we are downloading
    dlg_url_label = Label(dlg, text=f"Downloading {url}...")
    dlg_url_label.grid(row=0, column=0, padx=1, pady=1, sticky=tk.NW)
    # Make a status progressbar
    dlg_progressbar = Progressbar(dlg, length=200)
    dlg_progressbar.grid(row=1, column=0, padx=1, pady=1, sticky=tk.NW + tk.E)
    # Make a status label that shows what we are are doing
    dlg_status = Label(dlg)
    dlg_status.grid(row=2, column=0, padx=1, pady=1, sticky=tk.NW)
    # Make sure the user can't interact with teh main window
    dlg.grab_focus()
    # Call the start_download function in a daemon thread
    Thread(target=start_download, args=(dlg, dlg_status, dlg_progressbar, url), daemon=True).start()
    dlg.wait_till_destroyed()


# Create a function to actually start the download
def start_download(dlg: CustomDialog, status_label: Label, progress_bar: Progressbar, url: str):
    # Set the status text of the status label
    status_label.text = "Connecting to server..."
    # Try to get a response
    try:
        response = requests.get(url, stream=True)
    except HTTPError as err:
        # Show error and leave
        show_error(root, title="File Downloader: Error!", message="A HTTP(S) error occurred!",
                   detail=f"Exception: {err}")
        dlg.close()
        return
    except Exception as err:
        show_error(root, title="File Downloader: Error!", message="An error occurred!",
                   detail=f"Exception: {err}")
        dlg.close()
        return
    # Set status text
    status_label.text = f"Connected! Status code is {response.status_code}."
    # Show error if status code is not 200
    if response.status_code != 200:
        show_error(root, title="File Downloader: Error!", message="Server did not return 200!",
                   detail=f"Status code returned: {response.status_code}")
        dlg.close()
        return
    # The content length is how big the file is (usually)
    file_size = int(response.headers.get("content-length", 0))
    progress_bar.maximum = file_size
    progress_bar.value = 0
    # In bytes
    block_size = 1024
    # Get the name of the file from splitting the URL
    file_name = url.split("/")[-1]
    file_path = Path(path_entry.value) / file_name
    # Warn the user before overwriting the file if it exists
    if file_path.exists():
        if not ask_ok_or_cancel(root, title="File Downloader: Confirm", message=f"{file_path}\nexists! Continue? "
                                                                                f"(Will overwrite if continue)"):
            dlg.close()
            return
    # Open the file path
    with file_path.open(mode="wb") as file:
        # Iterate over all the data blocks
        for data in response.iter_content(block_size):
            # Update the progress bar
            progress_bar.value += len(data)
            # Update the status text
            status_label.text = f"Downloaded " \
                                f"{round(progress_bar.value / 1024, 2)} / " \
                                f"{round(file_size / 1024, 2)} KiB"
            # Write the data to the file
            file.write(data)
    # Show the user that it finished downloading
    show_info(root, title="File Downloader: Info", message=f"File finished downloading! You can find it at:\n"
                                                           f"{file_path}")
    # Destroy the dialog
    dlg.close()


# Create a button to start the download process
download_btn = Button(root, text="Download", command=download)
download_btn.grid(row=2, column=0, padx=1, sticky=tk.NSEW)

# Start the mainloop
root.mainloop()
