import asyncio
import edge_tts
import sys
import os
import re

async def text_to_speech(text, output_file, voice="zh-CN-XiaoxiaoNeural"):
    """
    Converts text to speech using edge-tts.
    Strips markdown code blocks and excess symbols for a cleaner listen.
    """
    # Simple regex to remove markdown code blocks: ```...```
    cleaned_text = re.sub(r'```[\s\S]*?```', '[此处省略代码块]', text)
    # Remove some other technical symbols common in reports but bad for TTS
    cleaned_text = cleaned_text.replace('file:///', '文件路径 ')
    
    communicate = edge_tts.Communicate(cleaned_text, voice)
    await communicate.save(output_file)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python read_report.py <text_file_or_string> <output_mp3>")
        sys.exit(1)

    input_data = sys.argv[1]
    output_path = sys.argv[2]

    # Check if input is a file or a string
    if os.path.isfile(input_data):
        with open(input_data, 'r', encoding='utf-8') as f:
            content = f.read()
    else:
        content = input_data

    # Perform TTS
    asyncio.run(text_to_speech(content, output_path))
    print(f"Audio saved to: {output_path}")

    # Automatic playback if requested (default to True for current convenience)
    play_audio = True if "--play" in sys.argv or len(sys.argv) == 3 else False
    
    if play_audio:
        print("Playing audio...")
        full_path = os.path.abspath(output_path)
        
        # 1. Get audio duration using Shell.Application (robust for metadata)
        # Column 27 is usually 'Duration' in Windows Shell
        import subprocess
        dir_name = os.path.dirname(full_path)
        file_name = os.path.basename(full_path)
        get_duration_cmd = [
            "powershell", "-Command",
            f"$s = New-Object -ComObject Shell.Application; "
            f"$f = $s.Namespace('{dir_name}'); "
            f"$i = $f.ParseName('{file_name}'); "
            f"$d = $f.GetDetailsOf($i, 27); $d"
        ]
        try:
            duration_str = subprocess.check_output(get_duration_cmd, text=True).strip()
            # Duration format is HH:MM:SS or MM:SS
            parts = duration_str.split(':')
            seconds = 0
            if len(parts) == 3: # HH:MM:SS
                seconds = int(parts[0]) * 3600 + int(parts[1]) * 60 + int(parts[2])
            elif len(parts) == 2: # MM:SS
                seconds = int(parts[0]) * 60 + int(parts[1])
            else:
                seconds = 30 # Fallback
        except:
            seconds = 60 # Fallback for long reports
            
        print(f"Detected duration: {seconds}s. Starting playback...")
        
        # 2. Start playback (User confirmed 'start' works)
        os.system(f'start "" "{full_path}"')
        
        # 3. Wait and Kill
        import time
        time.sleep(seconds + 5) # Buffer for loading
        print("Closing playback software...")
        # Common playback processes on Windows
        os.system("taskkill /F /IM Music.UI.exe /T 2>NUL") # Groove
        os.system("taskkill /F /IM Microsoft.Media.Player.exe /T 2>NUL") # New Media Player
        os.system("taskkill /F /IM wmplayer.exe /T 2>NUL") # Legacy WMP
