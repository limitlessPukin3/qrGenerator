**How to Create and Host Your Own Digital Business Card Using GitHub Pages**

## **Step 1: Create the Digital Business Card (HTML File)**

We will create a simple HTML file that serves as your digital business card.

1. Open a text editor (e.g., Notepad++, VS Code, or nano on Linux).
2. Copy and paste the following HTML code into a new file:

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

## **Step 2: Host the File Using GitHub Pages**

1. Create a **GitHub account** (if you don’t already have one).
2. **Create a new repository** on GitHub and name it (e.g., `digital-business-card`).
3. Inside the repository, **upload your `index.html` file**.
4. Go to **Settings > Pages** in your repository.
5. Under the **Source** section, select `main` (or the branch where you uploaded `index.html`).
6. Click **Save**.
7. GitHub will generate a link like:
   ```
   https://yourusername.github.io/digital-business-card/
   ```
8. Your business card is now publicly available!

## **Step 3: Generate a QR Code for Easy Sharing**

To make sharing easier, generate a QR code that links to your GitHub Pages site.

1. Install the `qrcode` Python package (if not installed):
   ```sh
   pip install qrcode[pil]
   ```
2. Run the following script to generate the QR code:
   ```python
   import qrcode
   url = "https://yourusername.github.io/digital-business-card/"  # Replace with your actual GitHub Pages URL
   img = qrcode.make(url)
   img.save("business_card_qr.png")
   ```
3. Print or share the QR code image (`business_card_qr.png`).

## **Conclusion**

Now you have a **self-hosted digital business card** using GitHub Pages that you can share via QR code or a direct link. Would you like further customization or help with automation?

---

### **Future Enhancements**
- Add a backend to collect visitor interactions.
- Enable a contact form with email notifications.
- Implement a responsive design with CSS frameworks like Bootstrap.

Would you like additional customization or deployment assistance? 🚀

### **Version History**
- 2/6/2025 - Base functionality
