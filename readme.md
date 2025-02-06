# Digital Business Card - Self-Hosted

This project provides a step-by-step guide to creating and hosting your own **digital business card** at home using a simple **HTML page** and serving it through a **local web server**.

## **Features**
- Static HTML business card page
- QR code generation for easy sharing
- Self-hosted using Python or Nginx
- Optional public access via port forwarding & dynamic DNS

## **Prerequisites**
- A computer, Raspberry Pi, or home server
- Basic knowledge of using the terminal/command prompt
- Installed software:
  - Python 3 (for quick hosting and QR code generation)
  - Nginx (for long-term hosting, optional)
  - pip package manager

## **Setup Instructions**

### **Step 1: Create the Digital Business Card**
1. Open a text editor and create a new file `index.html`.
2. Copy and paste the following HTML template:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Digital Business Card</title>
    <style>
        body { font-family: Arial, sans-serif; text-align: center; margin: 20px; }
        .card { border: 1px solid #ddd; padding: 20px; border-radius: 10px; display: inline-block; box-shadow: 2px 2px 10px rgba(0,0,0,0.1); }
        img { width: 100px; border-radius: 50%; }
        a { display: block; margin-top: 10px; color: #007BFF; text-decoration: none; }
    </style>
</head>
<body>
    <div class="card">
        <img src="profile.jpg" alt="Your Name">
        <h2>Your Name</h2>
        <p>Job Title</p>
        <p>Company Name</p>
        <p>Email: <a href="mailto:youremail@example.com">youremail@example.com</a></p>
        <p>Phone: <a href="tel:+1234567890">+1 234 567 890</a></p>
        <a href="https://linkedin.com/in/yourprofile">LinkedIn</a>
        <a href="https://yourwebsite.com">Website</a>
    </div>
</body>
</html>
```
3. Save the file as `index.html`.

### **Step 2: Host the File on Your Local Network**
#### **Option 1: Using Python (Quick Setup)**
1. Open a terminal or command prompt.
2. Navigate to the folder containing `index.html`:
   ```sh
   cd /path/to/your/file
   ```
3. Start a simple web server:
   ```sh
   python3 -m http.server 8000
   ```
4. Access your business card at:  
   `http://your-local-ip:8000`

#### **Option 2: Using Nginx (Better for Long-Term Hosting)**
1. Install Nginx:
   ```sh
   sudo apt update && sudo apt install nginx -y
   ```
2. Move your `index.html` file to the Nginx web root directory:
   ```sh
   sudo mv index.html /var/www/html/
   ```
3. Restart Nginx:
   ```sh
   sudo systemctl restart nginx
   ```
4. Access your digital business card at:  
   `http://your-local-ip/`

### **Step 3: Generate a QR Code for Easy Sharing**
1. Install the required package:
   ```sh
   pip install qrcode[pil]
   ```
2. Run the following script to generate a QR code:
   ```python
   import qrcode
   img = qrcode.make("http://your-local-ip:8000")
   img.save("business_card_qr.png")
   ```
3. Print or share the generated QR code image (`business_card_qr.png`).

### **Step 4: Make It Publicly Accessible (Optional)**
1. **Find your local IP address** by running:
   ```sh
   ipconfig (Windows) or ifconfig (Linux/macOS)
   ```
2. **Set up Port Forwarding** on your router to forward traffic on port `8000` (or `80` for Nginx) to your local machine.
3. **Use a Dynamic DNS service** (like No-IP) if your IP address changes frequently.
4. **Secure your site with HTTPS** using Let's Encrypt:
   ```sh
   sudo apt install certbot python3-certbot-nginx
   sudo certbot --nginx
   ```

## **Conclusion**
You now have a **self-hosted digital business card** that can be shared via QR code or a web link. Enjoy full control over your online presence without third-party services!

---

### **Future Enhancements**
- Add a backend to collect visitor interactions.
- Enable a contact form with email notifications.
- Implement a responsive design with CSS frameworks like Bootstrap.

Would you like additional customization or deployment assistance? 🚀

### **Version History**
- 2/6/2025 - Base functionality