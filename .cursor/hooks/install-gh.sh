#!/bin/bash
# gh CLI を WSL の ~/.local/bin にインストールする（sudo 不要）
set -e
mkdir -p ~/.local/bin
url=$(curl -s https://api.github.com/repos/cli/cli/releases/latest | grep -o 'https://[^"]*linux_amd64\.tar\.gz' | head -1)
echo "downloading: $url"
curl -sL "$url" -o /tmp/gh.tgz
tar -xzf /tmp/gh.tgz -C /tmp
cp /tmp/gh_*/bin/gh ~/.local/bin/
~/.local/bin/gh --version
