# 🎬 YouTube Playlist → Notes Automation (n8n Workflow)

## ❌ Problem
YouTube playlists are filled with value—lectures, tutorials, and full courses.  
But going through hours of videos and manually taking notes is **time-consuming and frustrating**.

---

## ✅ Solution
This workflow, built with **n8n**, automates the entire process.  
It transforms any YouTube playlist into **ready-to-use structured notes**.

---

## ⚙️ How It Works
1. **Input** → User submits a YouTube playlist URL + email.  
2. **Transcript Check** → Workflow verifies if transcripts exist (Postgres DB + Apify).  
3. **Note Generation** → Generates notes with **headings, bullet points, and summaries**.  
4. **Document Creation** → Saves the notes as **Google Docs** in Google Drive.  
5. **Delivery** → Bundles everything into a **zip file** and sends it via email.  

---

## 👥 Who Can Benefit
- **Students & Researchers** → Lecture/course notes instantly.  
- **Professionals Upskilling** → Summaries of tutorials & certifications.  
- **Corporate Training Teams** → Convert training videos into reference docs.  
- **Content Creators & Educators** → Repurpose transcripts into blogs or guides.  
- **Knowledge Workers & Analysts** → Extract insights from talks, panels, or documentaries.  

---

## 🎯 Result
One playlist link in → **A complete set of organized notes out.**  
No wasted time, just **actionable knowledge**.  

---

## 🚀 Tech Stack
- [n8n](https://n8n.io) (workflow automation)  
- [Postgres](https://www.postgresql.org) (storage)  
- [Apify](https://apify.com) (web scraping for transcripts)  
- [Google Drive](https://workspace.google.com) (document storage)  
- [Gmail](https://workspace.google.com) (email delivery)  

---

## 📧 Example Usage
