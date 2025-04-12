@echo off
setlocal

set GIT_USER=5495z7945
set REPO_NAME=whistube-api
set BRANCH_NAME=main

git init
git add .
git commit -m "🆕 Init and deploy WhisTube API"
git remote remove origin 2>nul
git remote add origin https://github.com/%GIT_USER%/%REPO_NAME%.git
git push -u origin %BRANCH_NAME% --force

start https://github.com/%GIT_USER%/%REPO_NAME%
pause
