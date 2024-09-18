# How to Zip Files with the Python S3fs Library + Backblaze B2 Cloud Storage
- URL: https://www.backblaze.com/blog/how-to-zip-files-with-the-python-s3fs-library-backblaze-b2-cloud-storage/
- Added At: 2024-09-18 14:49:44
- [Link To Text](2024-09-18-how-to-zip-files-with-the-python-s3fs-library-+-backblaze-b2-cloud-storage_raw.md)

## TL;DR
文章介绍了如何通过S3Fs库高效地将多个文件压缩成.zip格式并提供下载，避免了传统方法中对本地存储和内存的依赖，推荐开发者在云对象存储应用中使用此类工具。

## Summary
1. **引言**：
   - 当需要发送多个文件时，通常会将文件压缩成.zip格式。
   - .zip文件格式由Phil Katz于1986年创建，已成为普遍使用的文件压缩格式。
   - 如果Web应用程序允许用户下载文件，提供将多个文件打包成单个.zip文件的功能是很有必要的。

2. **问题与解决方案**：
   - **常见错误**：
     - 一种简单的实现方式是将选定的文件从云存储下载到本地临时存储，压缩成.zip文件，然后删除本地源文件，再将.zip文件上传到云存储，最后提供用户下载链接。
     - 这种方法的问题在于需要足够的本地存储空间来容纳所有选定的文件和生成的.zip文件，且无法处理并发下载的情况。
   - **改进方法**：
     - 通过数据流的方式，直接从云存储中读取选定的文件，通过压缩算法处理后，将压缩数据流写入云存储中的新文件。
     - 这种方法避免了本地存储的限制，且更高效。

3. **技术实现**：
   - **Python的zipfile模块**：
     - 使用Python的zipfile模块进行数据压缩和解压缩。
     - zipfile模块支持文件类对象，使得可以构建数据处理管道。
   - **Boto3 SDK**：
     - 最初考虑使用Boto3 SDK，但发现单个`put_object`调用上传文件的最大限制为5GB，且需要足够的内存来存储整个.zip文件。
   - **S3Fs库**：
     - S3Fs是一个Pythonic的文件接口，适用于S3兼容的云对象存储，如Backblaze B2。
     - S3Fs支持多部分上传，允许编写更简洁的代码，并支持文件类对象的写入。
     - 使用S3Fs实现任意大小的.zip文件压缩，代码行数与之前尝试相当，但功能更强大。

4. **内存使用**：
   - `copyfileobj()`函数在复制数据时，可以通过设置缓冲区大小来控制速度和内存使用的平衡。
   - 在`b2-zip-files`应用中，默认设置缓冲区大小为1MiB。

5. **总结与建议**：
   - 通过S3Fs库，解决了初始方法中的问题，允许在不占用过多磁盘存储或内存的情况下提供.zip文件下载。
   - 建议开发者在编写访问云对象存储的应用时，考虑使用S3Fs等工具，以节省时间和提高效率。

6. **作者简介**：
   - Pat Patterson是Backblaze的首席技术布道师，拥有30多年的行业经验。
   - 他在Sun Microsystems、Salesforce、StreamSets和Citrix等公司构建了软件和社区。
   - 在Backblaze，他创建并交付针对技术专业人员需求的内容，并在产品团队中担任“开发者之声”的角色。
   - 业余时间，Pat参加长跑，已完成长达50英里的超马比赛。
