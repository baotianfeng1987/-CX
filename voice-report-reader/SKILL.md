---
name: voice-report-reader
description: Converts text reports (like stock market reviews) into high-quality Chinese audio using edge-tts. Use this skill when the user wants to "read" or "listen to" a report or document.
---

# Voice Report Reader

This skill provides a simple way to convert text-based reports into MP3 audio files using the high-quality Neural voices from Microsoft Edge.

## Usage

1. **Automatic Conversion and Playback**:
   Run the script with text or a file path. It will automatically strip markdown code blocks and technical noise for a better listening experience.
   ```bash
   python scripts/read_report.py "您的报告文本内容" output_report.mp3
   ```

2. **Key Features**:
   - **Code Stripping**: Automatically skips markdown code blocks (` ``` `).
   - **Auto-Playback**: Triggers Windows `start` command to play the audio immediately.
   - **Voice**: Default is `zh-CN-XiaoxiaoNeural` (Chinese Female).

## Voice Configuration

Default voice is `zh-CN-XiaoxiaoNeural` (Chinese Female). You can modify the script to use other voices like `zh-CN-YunxiNeural` (Chinese Male).
