# Deployment Guide

## Quick Preview (Local)

```bash
# Open in default browser
open landing-page/index.html

# Or use Python HTTP server
cd landing-page
python3 -m http.server 8000
# Visit http://localhost:8000
```

## Deploy to GitHub Pages

1. **Push to GitHub**:
```bash
git add landing-page/
git commit -m "Add D.E.R.E.K Power landing page"
git push origin main
```

2. **Enable GitHub Pages**:
   - Go to repository Settings
   - Navigate to Pages section
   - Source: Deploy from branch
   - Branch: `main` → `/landing-page` folder
   - Click Save

3. **Access**:
   - URL: `https://yourusername.github.io/derek-power/`
   - Wait 1-2 minutes for deployment

## Deploy to Netlify

1. **Via Netlify CLI**:
```bash
npm install -g netlify-cli
cd landing-page
netlify deploy --prod
```

2. **Via Netlify UI**:
   - Connect GitHub repository
   - Build settings:
     - Base directory: `landing-page`
     - Build command: (leave empty)
     - Publish directory: `.`
   - Deploy

## Deploy to Vercel

1. **Via Vercel CLI**:
```bash
npm install -g vercel
cd landing-page
vercel --prod
```

2. **Via Vercel UI**:
   - Import GitHub repository
   - Framework: Other
   - Root directory: `landing-page`
   - Build command: (leave empty)
   - Output directory: `.`
   - Deploy

## Deploy to Cloudflare Pages

1. **Via Cloudflare Dashboard**:
   - Connect GitHub repository
   - Build settings:
     - Build command: (leave empty)
     - Build output directory: `landing-page`
   - Deploy

## Custom Domain Setup

### GitHub Pages
1. Add `CNAME` file in `landing-page/`:
```bash
echo "derek.yourdomain.com" > landing-page/CNAME
```

2. Configure DNS:
```
Type: CNAME
Name: derek
Value: yourusername.github.io
```

### Netlify/Vercel/Cloudflare
- Add custom domain in dashboard
- Follow DNS configuration instructions
- SSL certificate auto-provisioned

## Performance Optimization (Optional)

### Minify HTML
```bash
npm install -g html-minifier
html-minifier --collapse-whitespace --remove-comments index.html -o index.min.html
```

### Self-host Tailwind CSS
```bash
# Download Tailwind CSS
curl -o tailwind.min.css https://cdn.tailwindcss.com

# Update index.html to use local file
<link rel="stylesheet" href="tailwind.min.css">
```

### Self-host Google Fonts
Use [google-webfonts-helper](https://gwfh.mranftl.com/fonts) to download and self-host fonts.

## Monitoring

### Add Analytics (Optional)

**Google Analytics**:
```html
<!-- Add before </head> -->
<script async src="https://www.googletagmanager.com/gtag/js?id=GA_MEASUREMENT_ID"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'GA_MEASUREMENT_ID');
</script>
```

**Plausible Analytics** (privacy-friendly):
```html
<!-- Add before </head> -->
<script defer data-domain="yourdomain.com" src="https://plausible.io/js/script.js"></script>
```

## Troubleshooting

### Issue: Styles not loading
- Check Tailwind CDN is accessible
- Verify `styles.css` path is correct
- Check browser console for errors

### Issue: Fonts not loading
- Verify Google Fonts CDN is accessible
- Check font names in Tailwind config
- Test with fallback fonts

### Issue: Links not working
- Update GitHub repository URLs
- Verify all `href` attributes
- Test in incognito mode

---

**Need help?** Open an issue on GitHub
