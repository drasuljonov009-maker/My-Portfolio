// Tailwind Config
if (typeof tailwind !== 'undefined') {
  tailwind.config = {
    theme: {
      extend: {
        colors: {
          primary: {
            400: '#fb923c',
            500: '#f97316',
            600: '#ea580c',
          },
          dark: {
            900: '#0f172a',
            800: '#1e293b',
            700: '#334155',
          }
        },
        fontFamily: {
          outfit: ['Outfit', 'sans-serif'],
        }
      }
    }
  }
}

// Mobile Menu Toggle
function toggleMenu() {
  const menu = document.getElementById('mobile-menu');
  if (menu) {
    menu.classList.toggle('hidden');
  }
}

// Smooth scroll for anchor links
document.addEventListener('DOMContentLoaded', () => {
  // Year
  const yearEl = document.getElementById('current-year');
  if (yearEl) yearEl.textContent = new Date().getFullYear();

  // Animate skill bars
  const bars = document.querySelectorAll('.skill-bar-fill');
  const barObserver = new IntersectionObserver((entries) => {
    entries.forEach(e => {
      if (e.isIntersecting) {
        const el = e.target;
        el.style.width = el.dataset.width + '%';
        barObserver.unobserve(el);
      }
    });
  }, { threshold: 0.3 });
  bars.forEach(b => {
    b.style.width = '0%';
    b.style.transition = 'width 1s ease';
    barObserver.observe(b);
  });

  // Scroll reveal
  const revealEls = document.querySelectorAll('.reveal');
  const revealObserver = new IntersectionObserver((entries) => {
    entries.forEach(e => {
      if (e.isIntersecting) {
        e.target.classList.add('revealed');
        revealObserver.unobserve(e.target);
      }
    });
  }, { threshold: 0.1 });
  revealEls.forEach(el => revealObserver.observe(el));
});
