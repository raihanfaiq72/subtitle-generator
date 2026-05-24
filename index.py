import os

import whisper

# pilih model:
# tiny = paling cepat
# base = seimbang
# small = lebih bagus
# medium = bagus
# large = terbaik tapi berat
model = whisper.load_model("large")

current_folder = os.path.dirname(os.path.abspath(__file__))

for file in os.listdir(current_folder):
    if file.lower().endswith(".mkv"):
        video_path = os.path.join(current_folder, file)

        output_name = os.path.splitext(file)[0]

        print(f"Memproses: {file}")

        result = model.transcribe(video_path, language="ja", task="translate")

        srt_path = os.path.join(current_folder, output_name + ".srt")

        with open(srt_path, "w", encoding="utf-8") as f:
            for i, segment in enumerate(result["segments"], start=1):
                start = segment["start"]
                end = segment["end"]

                text = segment["text"].strip()

                def convert_time(sec):

                    h = int(sec // 3600)
                    m = int((sec % 3600) // 60)
                    s = int(sec % 60)

                    ms = int((sec - int(sec)) * 1000)

                    return f"{h:02}:{m:02}:{s:02},{ms:03}"

                f.write(f"{i}\n")

                f.write(f"{convert_time(start)} --> {convert_time(end)}\n")

                f.write(f"{text}\n\n")

        print(f"Subtitle dibuat: {srt_path}")

print("Selesai semua")
