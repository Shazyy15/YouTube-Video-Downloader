import tkinter as tk
from tkinter import ttk, messagebox
from pytube import YouTube
from tkinter import filedialog

class YouTubeDownloader:
    def __init__(self, root):
        self.root = root
        self.root.title("YouTube Video Downloader")
        self.root.geometry("600x400")
        self.root.resizable(False, False)
        self.root.config(bg="#f7f9fc")

        # Header Label
        tk.Label(root, text="YouTube Video Downloader", font=("Helvetica", 20, "bold"), bg="#f7f9fc", fg="#ff3333").pack(pady=10)

        # URL Entry
        tk.Label(root, text="Enter YouTube Video URL:", font=("Helvetica", 12), bg="#f7f9fc").pack(pady=5)
        self.url_entry = ttk.Entry(root, font=("Helvetica", 12), width=50)
        self.url_entry.pack(pady=5)

        # Path Entry
        tk.Label(root, text="Select Download Folder:", font=("Helvetica", 12), bg="#f7f9fc").pack(pady=5)
        self.path_entry = ttk.Entry(root, font=("Helvetica", 12), width=50)
        self.path_entry.pack(pady=5)

        # Browse Button
        ttk.Button(root, text="Browse", command=self.browse_folder, style="TButton").pack(pady=5)

        # Download Button
        self.download_button = ttk.Button(root, text="Download", command=self.download_video, style="Accent.TButton")
        self.download_button.pack(pady=20)

        # Status Label
        self.status_label = tk.Label(root, text="", font=("Helvetica", 12), bg="#f7f9fc", fg="#0078d4")
        self.status_label.pack(pady=5)

        # Developer Credit
        tk.Label(root, text="Developed by Shazil Shahid", font=("Helvetica", 10, "italic"), bg="#f7f9fc", fg="#666666").pack(side="bottom", pady=10)

        # Styling
        self.apply_styles()

    def browse_folder(self):
        """Open a dialog to select a folder for saving the video."""
        folder_selected = filedialog.askdirectory()
        if folder_selected:
            self.path_entry.delete(0, tk.END)
            self.path_entry.insert(0, folder_selected)

    def download_video(self):
        """Download the video using the URL and save it in the selected folder."""
        url = self.url_entry.get().strip()
        save_path = self.path_entry.get().strip()

        if not url or not save_path:
            messagebox.showerror("Error", "Please fill in both fields.")
            return

        try:
            yt = YouTube(url)
            self.status_label.config(text="Downloading...", fg="#ff8800")
            stream = yt.streams.get_highest_resolution()
            stream.download(save_path)
            self.status_label.config(text="Download Completed!", fg="#28a745")
            messagebox.showinfo("Success", f"Video downloaded successfully!\nLocation: {save_path}")
        except Exception as e:
            self.status_label.config(text="Download Failed!", fg="#dc3545")
            messagebox.showerror("Error", f"An error occurred: {e}")

    def apply_styles(self):
        """Apply modern button styles."""
        style = ttk.Style()
        style.theme_use("clam")

        # Browse button
        style.configure("TButton", font=("Helvetica", 11), padding=6)

        # Download button
        style.configure("Accent.TButton", font=("Helvetica", 11, "bold"), foreground="white", background="#0078d4")
        style.map("Accent.TButton", background=[("active", "#005a9e")])

# Main application loop
if __name__ == "__main__":
    from pytube import YouTube  # Ensure pytube is installed via `pip install pytube`

    root = tk.Tk()
    app = YouTubeDownloader(root)
    root.mainloop()
