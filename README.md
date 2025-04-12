# WhisTube API

一鍵部署 Whisper + yt-dlp + Flask API，自動轉換 YouTube 影片為字幕。

## 功能
- 支援 POST /api/whistube，輸入 YouTube 連結，自動產出 SRT 與 TXT 檔案

## Render 部署教學
1. 將此 repo 上傳至 GitHub
2. 前往 [Render](https://dashboard.render.com) 新建 Web Service
3. 選擇部署來源為 GitHub
4. 選擇此 repo，並選擇：
   - **環境：Docker**
   - **Start command：空白**
5. 等待部署完成，測試 POST `/api/whistube`

## 範例 Request
```bash
curl -X POST https://your-api-url.onrender.com/api/whistube \
     -H "Content-Type: application/json" \
     -d '{"yt_url": "https://www.youtube.com/watch?v=XXXXX"}'
```
