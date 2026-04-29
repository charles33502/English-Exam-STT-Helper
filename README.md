# English Exam STT Helper  
# 英文檢定語音轉文字小工具

A small local speech-to-text helper for English exam audio files, powered by `faster-whisper`.

這是一個使用 `faster-whisper` 的本地語音轉文字小工具，主要用來處理英文檢定或英文聽力練習音檔。

## Features / 功能

- Batch transcribe audio files from the `input/` folder  
  批次轉錄 `input/` 資料夾中的音檔

- Supports `.mp3`, `.wav`, `.m4a`, `.flac`  
  支援 `.mp3`, `.wav`, `.m4a`, `.flac`

- Outputs full transcript and timestamped segments  
  輸出完整逐字稿與時間戳分段文字

- Runs locally, no API key required  
  本地執行，不需要 API key

## Usage / 使用方式

### 1. Install dependencies / 安裝套件

Double-click:

雙擊：

```bat
install_stt.bat
```

### 2. Put audio files into `input/`

將音檔放入：

```text
input/
```

### 3. Run STT / 執行轉錄

Double-click:

雙擊：

```bat
run_stt.bat
```

### 4. Check output / 查看輸出

Results will be saved in:

結果會儲存在：

```text
output/
```

Output files:

輸出檔案：

```text
xxx_transcript.txt
xxx_segments.txt
```

## Notes / 注意事項

- The transcript may contain recognition errors.  
  逐字稿可能會有辨識錯誤。

- Timestamped segments are approximate.  
  時間戳分段只是大略定位。

- The output usually still needs manual proofreading before being used for Anki or study notes.  
  若要用於 Anki 或正式筆記，通常仍需要人工校正。

## Requirements / 需求

```txt
faster-whisper
```

## License / 授權

MIT License