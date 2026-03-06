# Disable Your SSH Access With This One Simple Trick
- URL: https://sny.sh/hypha/blog/scp
- Added At: 2026-03-06 14:49:00
- Tags: #read #tips

## TL;DR
作者使用 scp 传输目录后，因目标目录权限被设为 777，导致 SSH 登录失败。原因是 OpenSSH 安全策略拒绝过宽权限。将权限恢复为 700 后问题解决，该问题已在后续版本修复。

## Summary
作者在使用 scp 命令将本地目录传输到服务器后，发现无法通过 SSH 登录，提示密钥被拒绝。通过排查，发现是由于本地目录权限为 777（rwxrwxrwx），而 scp 在传输时会将目标目录的权限也修改为 777。OpenSSH 的 sshd 服务出于安全考虑，拒绝权限过于开放的目录（如 777），导致 SSH 登录失败。作者将目标目录权限恢复为 700（rwx------）后，问题解决。此问题已向 OpenSSH 报告，并在后续版本中修复。
