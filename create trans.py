import os
import io

data_dir = "/Users/mandeebot/Desktop/proj_data/Berom_Speech_Dataset"
file_path = os.path.join("/Users/mandeebot/Desktop/proj_data/Berom_Speech_Dataset")
trans = "/Users/mandeebot/Desktop/proj_data/Berom_Speech_Dataset/trans"


wav_data = os.path.join(data_dir, "wav")
txt_data = os.path.join(data_dir,"trans")

wav_files = os.listdir(wav_data)

with io.open(trans, "a") as f:
    for i, wav_file in enumerate(wav_files):
        # Get the path to the corresponding transcription file.
        txt_file = os.path.join(txt_data, wav_file.rstrip(".wav") + ".txt")

        # Write the path to the transcription file to the output file.
        f.write(txt_file + "\n")