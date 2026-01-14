# D.E.R.E.K Power Landing Page

Professional landing page for D.E.R.E.K Power - a structured development workflow tool.

## Design System

### Style
- **Primary Style**: Dark Mode (OLED) + Minimalism
- **Target Audience**: Developers, DevOps engineers, technical teams
- **Mood**: Professional, trustworthy, structured, no-nonsense

### Typography
- **Heading Font**: Poppins (geometric, modern, professional)
- **Body Font**: Open Sans (humanist, readable, friendly)
- **Google Fonts**: Loaded via CDN

### Color Palette
- **Primary**: `#2563EB` (Trust Blue)
- **Secondary**: `#3B82F6` (Light Blue)
- **CTA**: `#F97316` (Orange - high contrast)
- **Dark Background**: `#0A0E27` (Midnight Blue)
- **Dark Surface**: `#121212` (Deep Black)
- **Text**: `#E2E8F0` (Light Gray)
- **Muted Text**: `#94A3B8` (Slate)

### Layout Structure
1. **Hero Section**: Bold headline, value proposition, dual CTAs
2. **Why D.E.R.E.K**: Comparison table (Typical AI vs D.E.R.E.K)
3. **Features**: 6-card grid showcasing core capabilities
4. **Workflow**: 5-phase D.E.R.E.K process explanation
5. **CTA Section**: Final conversion with stats
6. **Footer**: Links and tagline

## Features

### Accessibility
- ✅ WCAG AAA contrast ratios
- ✅ Keyboard navigation support
- ✅ Focus visible states
- ✅ `prefers-reduced-motion` support
- ✅ Semantic HTML structure
- ✅ Alt text for all visual elements (SVG icons)

### Performance
- ✅ Minimal dependencies (Tailwind CDN only)
- ✅ No JavaScript frameworks
- ✅ Optimized font loading
- ✅ CSS custom properties for theming
- ✅ Efficient animations (GPU-accelerated)

### Responsive Design
- ✅ Mobile-first approach
- ✅ Breakpoints: 320px, 768px, 1024px, 1440px
- ✅ Flexible grid layouts
- ✅ Responsive typography
- ✅ Touch-friendly interactive elements

### UX Best Practices
- ✅ No emoji icons (SVG only)
- ✅ Cursor pointer on all interactive elements
- ✅ Smooth transitions (200ms)
- ✅ Hover states with visual feedback
- ✅ Floating navbar with proper spacing
- ✅ High contrast in both light/dark modes
- ✅ Consistent spacing and alignment

## File Structure

```
landing-page/
├── index.html          # Main HTML file
├── styles.css          # Custom CSS (scrollbar, focus, print)
└── README.md           # This file
```

## Usage

### Local Development
Simply open `index.html` in a browser:

```bash
open landing-page/index.html
```

### Deploy to GitHub Pages
1. Push to GitHub repository
2. Go to Settings → Pages
3. Select branch and `/landing-page` folder
4. Save and wait for deployment

### Deploy to Netlify/Vercel
1. Connect repository
2. Set build directory to `landing-page`
3. No build command needed (static HTML)
4. Deploy

## Customization

### Change Colors
Edit the Tailwind config in `index.html`:

```javascript
tailwind.config = {
    theme: {
        extend: {
            colors: {
                primary: '#2563EB',    // Change this
                secondary: '#3B82F6',  // Change this
                cta: '#F97316',        // Change this
            }
        }
    }
}
```

### Change Fonts
Update Google Fonts link and Tailwind config:

```html
<link href="https://fonts.googleapis.com/css2?family=YourFont&display=swap" rel="stylesheet">
```

```javascript
fontFamily: {
    heading: ['YourFont', 'sans-serif'],
    body: ['YourFont', 'sans-serif']
}
```

### Update Content
Edit the HTML directly - all content is in semantic sections with clear comments.

## Browser Support
- ✅ Chrome/Edge 90+
- ✅ Firefox 88+
- ✅ Safari 14+
- ✅ Mobile browsers (iOS Safari, Chrome Mobile)

## License
MIT License - Free to use and modify

---

**Built with UI/UX Pro Max design intelligence**
