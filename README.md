# Kordiak Park Explorer

A simple, beautiful website for Kordiak Park in Columbia Heights, MN. Built with **Jekyll**, **Tailwind CSS**, and **Leaflet.js**.

## Features
- 🌿 **Home**: Welcome page with quick links.
- ✍️ **Blog**: Simple Markdown-based blog.
- 📅 **Timeline**: A chronological list of park events.
- 🗺️ **Map**: Interactive map showing bird sightings.

## How to Expand

### 📝 Adding Blog Posts
1. Create a new file in `_posts/`.
2. Use the following format:
   ```markdown
   ---
   layout: post
   title: "Your Post Title"
   date: YYYY-MM-DD
   ---
   Your content goes here in Markdown.
   ```

### 📅 Adding Timeline Events
1. Open `_data/timeline.yml`.
2. Add a new entry:
   ```yaml
   - event: "Event Name"
     date: "Month Year"
     description: "Event details go here."
   ```

### 🦆 Adding Bird Sightings
1. Open `_data/birds.yml`.
2. Add a new sighting:
   ```yaml
   - species: "Species Name"
     date: "YYYY-MM-DD"
     lat: 45.000000
     lng: -93.000000
     note: "Sighting notes."
   ```

### 🐶 Adding a Dog Roster (Expansion Example)
To add a "Dog Roster" later, you would define a collection in `_config.yml` and create a `_dogs` folder.

## How to Run Locally
To preview the site on your computer:
1. Ensure you have Ruby and Jekyll installed.
2. Run `bundle install` (if using a Gemfile).
3. Run `bundle exec jekyll serve` (or `jekyll serve`).
4. Visit `http://localhost:4000` in your browser.

## Deployment
This site is ready for **GitHub Pages**. Just push this code to a repository and enable GitHub Pages in your repository settings.
