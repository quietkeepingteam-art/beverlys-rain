BEVERLY'S RAIN
==============

What it does
  Tap once. A random photo appears and a random short clip plays. Then a song
  plays while up to 10 random photos slide by on repeat, quotes fade in and out,
  and soft rain plays underneath. The next song gets a new clip and new photos.

Folder layout
  index.html          the app (open this)
  library.js          the list of your files
  build-library.html  helper that writes library.js for you
  make_library.py     same thing, if you have Python
  media/photos        your photos (JPG or PNG)
  media/songs         your songs (MP3 or M4A)
  media/clips         short clips that play before each song (MP3 or M4A)
  media/rain          rain sounds (MP3 or M4A), one is picked and loops

Step 1: add your files
  Copy them into the media folders. Keep the names simple.
  Photos: resize to about 1600 px wide if you can. It keeps things fast.

Step 2: update library.js
  Open build-library.html in Chrome, Edge or Safari on a computer,
  choose this whole folder, click Download library.js, and put the
  downloaded file in this folder (replace the old one).
  Do this again any time you add or remove files.

Step 3a: use it on a Mac or PC
  Double-click index.html. Done.

Step 3b: use it on an iPhone (needs the folder on the internet)
  1. Go to app.netlify.com/drop on a computer and drag this folder onto the page.
     (A free account is needed to keep it. You get a link like something.netlify.app.)
  2. Open the link in Safari on her phone.
  3. Tap Share, then Add to Home Screen.
  4. Settings > Display & Brightness > Auto-Lock > Never.
     Make sure the ringer switch on the side is not on silent.

Options
  Press and hold the small gear on the first screen for about a second.
  You can change the rain volume, seconds per photo, shuffle, quotes,
  and add your own quote lines. You can also add files right on the device.
