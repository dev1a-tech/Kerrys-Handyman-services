# Kerry's Handyman Service LLC — Website

Concept one-page website for **Kerry's Handyman Service LLC**, 27 Robeson St, New Bedford, MA · 508-542-8281.
It covers fence installation and repair, home repairs and small electrical jobs, and shows the business's 4.8-star rating from 26 reviews. It's mobile-friendly, with click-to-call buttons and a free-estimate form.

![Website preview](screenshots/desktop.png)

## Live site

- **GitHub Pages:** https://YOUR-USERNAME.github.io/kerrys-handyman-service/
- **Streamlit:** https://YOUR-APP-NAME.streamlit.app

## Files

| File | What it does |
|---|---|
| `index.html` | **The website.** Open it in any browser. GitHub Pages shows this file. |
| `build_site.py` | Python script that builds `index.html`. Edit the `CONFIG` section to change the text. |
| `app.py` | Streamlit version of the site. |
| `requirements.txt` | Packages Streamlit needs to install. |
| `screenshots/` | Preview images (optional; only this README uses them). |

> You don't need Python just to see the site. Double-click `index.html` (on a Mac, right-click → **Open With → Safari**).

## Run it on a Mac

Open **Terminal**, type `cd ` (with a space), drag this folder into the window, press Return, then run:

```
python3 build_site.py              # rebuilds index.html and opens it
pip3 install -r requirements.txt
python3 -m streamlit run app.py    # runs the Streamlit version
```

## Put it online

**GitHub Pages (best for the real business site, always on):**

1. Create a **public** repo named `kerrys-handyman-service` and upload everything in this folder. The files go at the top level, not inside a folder.
2. Go to **Settings → Pages**, choose branch **`main`** and **`/ (root)`**, then click **Save**.
3. Wait 1–2 minutes. Your link appears at the top of that page.

**Streamlit (shows off the Python side):**

1. Go to **share.streamlit.io** and sign in with GitHub.
2. Click **Create app → Deploy a public app from GitHub**.
3. Repository `YOUR-USERNAME/kerrys-handyman-service`, branch **`main`**, main file path **`app.py`**, then click **Deploy**.

If the repo doesn't appear in Streamlit's list, click **Paste GitHub URL**, or give Streamlit access to it under GitHub **Settings → Applications → Streamlit → Configure**.

## Before going live, confirm with the owner

Items marked `# CONFIRM` in `build_site.py` are placeholders:

- The exact services (fence materials, the kinds of repairs, the specific electrical jobs), towns served, "Free estimates," and the FAQ answers
- **Electrical wording:** in Massachusetts, most electrical work requires a licensed electrician. Confirm what electrical work Kerry's is licensed to do, and adjust the electrical services and FAQ to match.
- Hours, ZIP code and email
- The link to the review page for the "Read our reviews" button
- Real customer review quotes (used with permission) in place of the placeholder
- Real project photos for the gallery
- A form service (such as Formspree) for the quote form. Until one is added, the form asks visitors to call.

## Built with

Python · HTML · CSS · Streamlit

---

*Concept site. Not yet the official website of Kerry's Handyman Service LLC.*
