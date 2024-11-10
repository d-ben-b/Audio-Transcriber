import whisper
import pyaudio
import wave
import time
import tkinter as tk
from tkinter import filedialog, messagebox
from threading import Thread  # 用於多線程
from downLoad import download_audio

# Function to record audio


def record_audio(file_name, record_seconds=5, sample_rate=16000, chunk_size=1024):
    audio = pyaudio.PyAudio()
    stream = audio.open(format=pyaudio.paInt16, channels=1,
                        rate=sample_rate, input=True, frames_per_buffer=chunk_size)
    print("Recording...")
    frames = []
    for _ in range(0, int(sample_rate / chunk_size * record_seconds)):
        data = stream.read(chunk_size)
        frames.append(data)
    print("Recording finished.")
    stream.stop_stream()
    stream.close()
    audio.terminate()
    with wave.open(file_name, 'wb') as wf:
        wf.setnchannels(1)
        wf.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
        wf.setframerate(sample_rate)
        wf.writeframes(b''.join(frames))

# Function to browse files


def browse_file():
    file_path = filedialog.askopenfilename(
        filetypes=[("m4a file", "*.m4a"), ("WAV files", "*.wav"), ("all files", "*.*")])
    if file_path:
        entry_file_name.delete(0, tk.END)  # Clear the current content
        entry_file_name.insert(0, file_path)  # Insert the selected file name

# Function to start recording or transcribing


def start_processing():
    # 在新線程中執行轉錄處理
    processing_thread = Thread(target=process_audio)
    processing_thread.start()

# Function to handle audio processing


def process_audio():
    if var.get() == 2:  # If "Record Audio" is selected
        recorded_file = "recorded_audio.wav"
        record_audio(recorded_file, record_seconds=5)
    elif var.get() == 1:  # If "Use Existing File" is selected
        recorded_file = entry_file_name.get()
        if not recorded_file:  # If no file is selected
            messagebox.showerror("Error", "Please provide an audio file.")
            return
    elif var.get() == 3:
        url = entry_file_name.get()
        if not url:
            messagebox.showerror("Error", "Please provide an URL.")
            return
        download_audio(url)
        recorded_file = "downloaded_audio.mp3"

    # Load Whisper model and transcribe the audio file
    try:
        model = whisper.load_model("medium")
        model = model.to("cuda")  # 使用 GPU 運行模型

        result = model.transcribe(recorded_file)

        file_name = f"STT_{time.strftime('%Y-%m-%d_%H-%M-%S')}.txt"

        with open(file_name, "w", encoding="utf-8") as file:
            file.write(result["text"])
        messagebox.showinfo("Success", f"Transcription saved to {file_name}")
    except Exception as e:
        messagebox.showerror("Error", str(e))


def main():
    global var, entry_file_name  # Declare global so we can access in other functions

    # Create the main tkinter window
    root = tk.Tk()
    root.title("Audio Transcriber with Whisper")

    # Add a radio button to choose between "Record Audio" and "Use Existing File"
    var = tk.IntVar(value=1)  # Default is "Record Audio"

    radio2 = tk.Radiobutton(
        root, text="Use Existing Audio File", variable=var, value=1)
    radio2.grid(row=0, column=0, sticky=tk.W)

    radio1 = tk.Radiobutton(root, text="Record Audio", variable=var, value=2)
    radio1.grid(row=1, column=0, sticky=tk.W)

    radio3 = tk.Radiobutton(root, text="Download Audio", variable=var, value=3)
    radio3.grid(row=2, column=0, sticky=tk.W)

    # Add an entry and a "Browse" button for the audio file
    entry_file_name = tk.Entry(root, width=40)
    entry_file_name.grid(row=3, column=0, padx=10, pady=10)

    btn_browse = tk.Button(root, text="Browse", command=browse_file)
    btn_browse.grid(row=3, column=1)

    # Add a "Start" button to trigger the transcription process
    btn_start = tk.Button(root, text="Start", command=start_processing)
    btn_start.grid(row=4, column=0, columnspan=2, pady=20)

    # Run the tkinter event loop
    root.mainloop()


# This ensures the main function is only called when the script is run directly
if __name__ == "__main__":
    main()
