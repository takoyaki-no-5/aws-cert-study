#!/bin/bash
set -e
cd /mnt/c/Users/kamag/Documents/AWS
git add -A
# ensure private stays ignored
git check-ignore -v .private/profile.md
printf '%s\n' 'CLF Anki階層デッキと学習主軸の整備、AnkiConnect連携を追加する' > /tmp/commitmsg.txt
git commit -F /tmp/commitmsg.txt
git push origin main
git status
git log -1 --oneline
