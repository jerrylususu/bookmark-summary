# Turning a conference talk into an annotated presentation - Jacob Kaplan-Moss
- URL: https://jacobian.org/til/talk-to-writeup-workflow/
- Added At: 2024-10-09 15:21:49

## TL;DR
作者利用现代AI工具将会议演讲视频转化为书面版本，通过Keynote准备演讲稿、下载和处理视频、生成和清理转录，最终手动编辑和完善内容，使其更适合书面阅读。

## Summary
1. **写作动机**：作者喜欢将会议演讲转化为书面版本，因为视频虽然很好，但并非所有人都有时间或意愿观看。过去由于转录整个演讲、制作书面版本等工作量大，未能实现。现代AI工具改变了这一情况，现在变得容易得多。

2. **演讲准备**：
   - **使用Keynote**：作者在Keynote中撰写演讲稿。
   - **导出幻灯片**：将Keynote中的幻灯片导出为包含PNG文件的文件夹。
   - **创建模板**：使用Simon的注释演示文稿创建工具快速渲染模板，模板类似于：
     ```
     {{< figure
          src="${filename}"
          alt="${escapeHTML(alt)}"
          class="slide" >}}
     ```
     作者未在此处粘贴注释，而是在Markdown文件中稍后添加。使用工具的OCR生成alt文本。

3. **视频处理**：
   - **下载视频**：从YouTube下载演讲视频，使用`yt-dlp`工具，通过`--download-sections`标志下载特定片段。
     ```
     ❯ yt-dlp https://www.youtube.com/live/[REDACTED] --download-sections "*10800,12438"
     ```
   - **转换格式**：将MKV格式的视频转换为MP4格式，使用`llm-cmd`工具。
     ```
     ❯ llm cmd convert Tuesday\ Junior\ Ballroom.mkv from mkv into mp4
     > ffmpeg -i "Tuesday Junior Ballroom [1J3UqRQcxqA].mkv" -c copy "Tuesday Junior Ballroom [1J3UqRQcxqA].mp4"
     ...
     ```

4. **转录处理**：
   - **生成转录**：使用MacWhisper将视频转换为转录，使用“Large V2”模型，现在可能使用“Turbo”模型更快。
   - **清理转录**：使用llm CLI将原始转录清理成段落，使用Claude 3.5 Sonnet模型。
     ```
     ❯ cat transcript-raw-whisper.txt | \
       llm -s "Split the content of this transcript up into paragraphs with logical breaks.
               Add newlines between each paragraph." \
       > transcript-split-claude.txt"
     ```

5. **编辑与完善**：
   - **手动粘贴**：将清理后的转录手动粘贴到Markdown文件中。
   - **重写与补充**：根据需要重写和添加额外内容，包括练习录音的转录和因时间限制被剪掉的内容。
   - **调整语气**：调整语气，使其更像书面语言而非口语，并检查Claude是否改变了原意或添加了不必要的内容。
