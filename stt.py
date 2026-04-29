from pathlib import Path
from faster_whisper import WhisperModel

INPUT_DIR = Path("input")
OUTPUT_DIR = Path("output")

MODEL_SIZE = "base"
DEVICE = "cpu"
COMPUTE_TYPE = "int8"
LANGUAGE = "en"
OUTPUT_SEGMENTS = True


def transcribe_file(audio_path: Path, model: WhisperModel) -> None:
    OUTPUT_DIR.mkdir(exist_ok=True)

    print(f"\n[STT] Processing: {audio_path.name}")

    segments, info = model.transcribe(
        str(audio_path),
        language=LANGUAGE,
        beam_size=5,
        vad_filter=True,
    )

    text_lines = []
    segment_rows = ["start\tend\ttext"]

    for seg in segments:
        text = seg.text.strip()
        if not text:
            continue

        text_lines.append(text)
        if OUTPUT_SEGMENTS:
            segment_rows.append(f"{seg.start:.2f}\t{seg.end:.2f}\t{text}")

    transcript = " ".join(text_lines).strip()

    transcript_path = OUTPUT_DIR / f"{audio_path.stem}_transcript.txt"
    transcript_path.write_text(transcript, encoding="utf-8")

    if OUTPUT_SEGMENTS:
        segments_path = OUTPUT_DIR / f"{audio_path.stem}_segments.txt"
        segments_path.write_text("\n".join(segment_rows), encoding="utf-8")

    print(f"[OK] Transcript saved: {transcript_path}")
    if OUTPUT_SEGMENTS:
        print(f"[OK] Segments saved:   {segments_path}")


def main():
    INPUT_DIR.mkdir(exist_ok=True)
    OUTPUT_DIR.mkdir(exist_ok=True)

    audio_files = []
    for ext in ["*.mp3", "*.wav", "*.m4a", "*.flac"]:
        audio_files.extend(INPUT_DIR.glob(ext))

    if not audio_files:
        print("No audio files found.")
        print("Please put .mp3/.wav/.m4a/.flac files into the input folder.")
        return

    print(f"Loading Whisper model: {MODEL_SIZE}")
    model = WhisperModel(MODEL_SIZE, device=DEVICE, compute_type=COMPUTE_TYPE)

    for audio_path in sorted(audio_files):
        transcribe_file(audio_path, model)

    print("\nDone.")


if __name__ == "__main__":
    main()
