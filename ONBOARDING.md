# Aurum Spa Website — Content Designer Onboarding

Welcome! This guide walks you through editing the Aurum Spa website on your laptop. You don't need any coding background — if you can use Word and a web browser, you can do this.

**The site lives at:** `https://github.com/mahalakongasawamo-star/aurum-spa-beverlyhills`

---

## One-time setup (15 minutes)

### 1. Accept the GitHub invite
Check your email for an invite from GitHub, or go to `https://github.com/notifications` and accept the invitation to the repo.

### 2. Install GitHub Desktop
Download from `https://desktop.github.com/` (Mac or Windows). Open it, click **Sign in to GitHub.com**, and log in with your GitHub account.

### 3. Install VS Code (your editor)
Download from `https://code.visualstudio.com/`. This is what you'll use to edit text and HTML.

After installing, open VS Code → click the Extensions icon on the left sidebar (four squares) → search for and install:
- **Live Server** — lets you preview the website with auto-refresh

### 4. Clone the repo to your laptop
In GitHub Desktop:
1. Click **File → Clone repository**
2. Pick `mahalakongasawamo-star/aurum-spa-beverlyhills`
3. Choose a folder on your laptop (e.g. `Documents/aurum-spa`)
4. Click **Clone**

You now have the entire website on your laptop.

---

## The daily workflow

Every time you sit down to make changes, follow these four steps:

### Step 1 — Pull the latest changes
Open GitHub Desktop. At the top, click **Fetch origin**. If it says "Pull origin," click it. This grabs anything Allan has changed since you last worked.

> **Important:** always do this BEFORE you start editing, or you risk overwriting someone else's work.

### Step 2 — Open in VS Code
In GitHub Desktop, click **Repository → Open in Visual Studio Code**.

### Step 3 — Edit and preview
- The main file you'll edit is `index.html`
- To preview: right-click `index.html` in VS Code's file list → **Open with Live Server**. Your browser opens the site, and it auto-refreshes when you save.
- Save your changes with `Ctrl+S` (Windows) or `Cmd+S` (Mac).

### Step 4 — Send your changes back to GitHub
Switch back to GitHub Desktop. You'll see your edits listed on the left.

1. Bottom-left: write a short summary in the box (e.g. "Update FAQ copy on homepage")
2. Click **Commit to main**
3. Top of window: click **Push origin**

Done. Your changes are now live on GitHub.

---

## Where to find things

| What you're editing | File or folder |
|---|---|
| Page text, headings, copy | `index.html` |
| Photos and graphics | `images/` |
| New images you want to add | `images/` (drag and drop) |
| Brand colors, fonts (rare) | `aurum-tokens.css` |

---

## Editing copy: a quick example

Open `index.html` in VS Code. Use `Ctrl+F` (Windows) or `Cmd+F` (Mac) to **find** the text you want to change. Type the existing phrase, hit enter, edit it, save with `Ctrl+S`, and check your Live Server preview.

You'll see HTML tags like `<h2>` or `<p>` around the words. **Leave the tags alone — only change the text between them.**

Example:
```html
<h2>Our Services</h2>          <-- only edit "Our Services"
<p>Where luxury meets...</p>   <-- only edit "Where luxury meets..."
```

If you accidentally break something, GitHub Desktop's left panel shows every change in red/green. You can right-click any file → **Discard changes** to undo before committing.

---

## Adding or replacing an image

1. Drag the new image into the `images/` folder (in your file explorer or VS Code).
2. In `index.html`, find where the old image is referenced (search for the old filename like `hero4.jpeg`).
3. Replace the filename with your new one.
4. Save, preview, commit, push.

> Keep image filenames simple — no spaces, all lowercase. Example: `lobby-evening.jpg` not `Lobby Evening.JPG`.

---

## Safer workflow: use branches (recommended once you're comfortable)

When you and Allan are both editing, working on **branches** prevents collisions.

In GitHub Desktop:
1. Top-left: click **Current branch** → **New branch**
2. Name it something descriptive: `content-faq-update` or `kim-edits-jan15`
3. Click **Create branch**
4. Edit, commit, and push as normal — your changes go to your branch, not `main`
5. On `github.com`, open a **Pull Request** so Allan can review and merge

Allan can then approve and merge your changes into the live site.

---

## Troubleshooting

**"I clicked Push and got an error about conflicts"**
Someone else pushed changes while you were editing. In GitHub Desktop, click **Fetch origin** → **Pull origin**. If it asks you to resolve conflicts, message Allan — don't try to fix it alone the first time.

**"My preview looks broken"**
Undo your last change (`Ctrl+Z` repeatedly) and re-save. You probably deleted an HTML tag by accident.

**"I committed something I shouldn't have"**
Don't push yet. Tell Allan before clicking Push origin — it's easy to undo locally, harder once it's on GitHub.

**"GitHub Desktop won't let me commit"**
Make sure you typed a summary message in the bottom-left box. It won't commit without one.

---

## Need help?

Message Allan with:
1. What you were trying to do
2. A screenshot of the error or what you're seeing
3. Whether you've clicked **Push origin** yet (this matters)

Welcome aboard.
