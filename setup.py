from setuptools import setup

setup(
    name="AudioTranscriber",
    version="1.0.0",
    description="A simple audio transcriber that uses Whisper and tkinter for UI",
    author="Your Name",
    author_email="your.email@example.com",
    py_modules=["stt_transcriber"],  # This is the correct way if it's a single file
    install_requires=[
        "whisper",
        "pyaudio"
    ],
    entry_points={
        'console_scripts': [
            'audio-transcriber=stt_transcriber:main',  # This should match exactly
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
