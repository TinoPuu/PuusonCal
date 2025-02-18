# 🚀 PuusonCal  

### 📅 Easily import events into Google Calendar from JSON files!  

PuusonCal automates **event creation** in Google Calendar using structured JSON files.  
Just pick a calendar, choose an event file, and let PuusonCal do the rest! 🎉  

---

## **Installation**  

### **1️⃣ Clone the Repository**  
Run the following commands in your terminal:  
```sh
git clone https://github.com/yourusername/PuusonCal.git  
cd PuusonCal  
```

### **2️⃣ Install Dependencies**
```sh
pip install -r requirements.txt  
```
---

## **Google Calendar API Setup**  

### **1️⃣ Enable Google Calendar API**  
- Open Google Cloud Console  
- Create a **new project**  
- Go to **APIs & Services** → **Enable APIs**  
- Search for **Google Calendar API** and enable it  

### **2️⃣ Create OAuth Credentials**  
- Navigate to **APIs & Services** → **Credentials**  
- Click **Create Credentials** → **OAuth Client ID**  
- Select **Desktop App** as the application type  
- Download the credentials.json file  

### **3️⃣ Place Credentials in `config/` Folder**  
- Move credentials.json into the **PuusonCal/config/** directory  
- First-time login will ask for Google authentication  

---

## **Configuration**  

### **Calendar Configuration (`calendar_config.json`)**  
This file defines the available calendars for event import.  

Example:  
```json
{  
  "calendars": {  
    "Work Calendar": "work.calendar@group.calendar.google.com",  
    "Personal Calendar": "personal.calendar@group.calendar.google.com"  
  }  
}  
```
### **Event Data (`input/events.json`)**
Example event file to import.  
```json
{  
  "events": [  
    {  
      "date": "19.02.2025",  
      "start_time": "08:00",  
      "end_time": "16:00",  
      "summary": "Morning Meeting",  
      "description": "Client presentation at the office."  
    }  
  ]  
}  
```
---

## **Running the Program**  
Execute the following command:  
```sh
python3 src/main.py  
```
---

### **Developed by TinoPuu**  
🚀 Built for easy calendar management!  