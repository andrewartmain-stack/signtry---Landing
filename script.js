const navToggle = document.getElementById('navToggle'),
  navMenu = document.getElementById('navMenu');
navToggle.addEventListener('click', () => {
  navMenu.classList.toggle('active');
});
const navLinks = navMenu.querySelectorAll('a');
navLinks.forEach((e) => {
  e.addEventListener('click', () => {
    navMenu.classList.remove('active');
  });
}),
  document.querySelectorAll('a[href^="#"]').forEach((e) => {
    e.addEventListener('click', function (e) {
      e.preventDefault();
      let t = document.querySelector(this.getAttribute('href'));
      if (t) {
        let o = t.offsetTop - 80;
        window.scrollTo({ top: o, behavior: 'smooth' });
      }
    });
  });
let lastScroll = 0;
const navbar = document.querySelector('.navbar');
window.addEventListener('scroll', () => {
  let e = window.pageYOffset;
  e > 100
    ? (navbar.style.boxShadow = '0 2px 10px rgba(0, 0, 0, 0.1)')
    : (navbar.style.boxShadow = 'none'),
    (lastScroll = e);
});
const faqItems = document.querySelectorAll('.faq-item');
faqItems.forEach((e) => {
  let t = e.querySelector('.faq-question');
  t.addEventListener('click', () => {
    let t = e.classList.contains('active');
    faqItems.forEach((e) => {
      e.classList.remove('active');
    }),
      t || e.classList.add('active');
  });
});
const watchDemoBtn = document.getElementById('watchDemoBtn'),
  playButton = document.getElementById('playButton'),
  videoModal = document.getElementById('videoModal'),
  closeModal = document.getElementById('closeModal'),
  videoModalBackdrop = document.getElementById('videoModalBackdrop'),
  modalVideo = document.getElementById('modalVideo'),
  videoContainer = document.getElementById('videoContainer'),
  videoOverlay = document.getElementById('videoOverlay'),
  demoVideo = document.getElementById('demoVideo'),
  videoUrl = 'https://www.youtube.com/embed/dQw4w9WgXcQ';
function openVideoModal() {
  videoModal.classList.add('active'),
    (document.body.style.overflow = 'hidden'),
    (modalVideo.src = videoUrl + '?autoplay=1');
}
function closeVideoModal() {
  videoModal.classList.remove('active'),
    (document.body.style.overflow = ''),
    (modalVideo.src = '');
}
watchDemoBtn && watchDemoBtn.addEventListener('click', openVideoModal),
  closeModal && closeModal.addEventListener('click', closeVideoModal),
  videoModalBackdrop &&
    videoModalBackdrop.addEventListener('click', closeVideoModal),
  document.addEventListener('keydown', (e) => {
    'Escape' === e.key &&
      videoModal &&
      videoModal.classList.contains('active') &&
      closeVideoModal();
  }),
  playButton &&
    playButton.addEventListener('click', (e) => {
      e.preventDefault(), e.stopPropagation();
      let t = videoContainer.querySelector('.video-placeholder');
      t && (t.style.display = 'none'),
        videoOverlay && (videoOverlay.style.display = 'block'),
        demoVideo && (demoVideo.src = videoUrl + '?autoplay=1');
    }),
  videoModal &&
    videoModal.addEventListener('transitionend', function (e) {
      !videoModal.classList.contains('active') &&
        videoOverlay &&
        demoVideo &&
        (demoVideo.src = '');
    });
const observerOptions = { threshold: 0.1, rootMargin: '0px 0px -100px 0px' },
  observer = new IntersectionObserver((e) => {
    e.forEach((e) => {
      e.isIntersecting &&
        ((e.target.style.opacity = '1'),
        (e.target.style.transform = 'translateY(0)'));
    });
  }, observerOptions),
  animateOnScroll = document.querySelectorAll(
    '.feature-card, .pricing-card, .faq-item'
  );
function animateCounter(e, t, o = 2e3) {
  let a = t / (o / 16),
    n = 0,
    l = setInterval(() => {
      (n += a) >= t
        ? ((e.textContent = formatNumber(t)), clearInterval(l))
        : (e.textContent = formatNumber(Math.floor(n)));
    }, 16);
}
function formatNumber(e) {
  return e >= 1e6
    ? (e / 1e6).toFixed(1) + 'M+'
    : e >= 1e3
    ? (e / 1e3).toFixed(0) + 'K+'
    : e.toString();
}
animateOnScroll.forEach((e) => {
  (e.style.opacity = '0'),
    (e.style.transform = 'translateY(20px)'),
    (e.style.transition = 'opacity 0.6s ease, transform 0.6s ease'),
    observer.observe(e);
});
const statsObserver = new IntersectionObserver(
    (e) => {
      e.forEach((e) => {
        if (e.isIntersecting && !e.target.classList.contains('animated')) {
          e.target.classList.add('animated');
          let t = e.target.querySelectorAll('.stat-number');
          t.forEach((e) => {
            let t = e.textContent;
            if (t.includes('K+')) {
              let o = 1e3 * parseFloat(t);
              animateCounter(e, o);
            } else if (t.includes('M+')) {
              let a = 1e6 * parseFloat(t);
              animateCounter(e, a);
            } else if (t.includes('/')) return;
          });
        }
      });
    },
    { threshold: 0.5 }
  ),
  heroStats = document.querySelector('.hero-stats');
function validateEmail(e) {
  return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(e);
}
heroStats && statsObserver.observe(heroStats),
  document.querySelectorAll('.btn-primary, .btn-secondary').forEach((e) => {
    e.addEventListener('click', function (e) {
      if (
        this.textContent.includes('Start') ||
        this.textContent.includes('Trial')
      ) {
        let t = this.innerHTML;
        (this.innerHTML = 'Loading...'),
          (this.disabled = !0),
          setTimeout(() => {
            (this.innerHTML = t),
              (this.disabled = !1),
              console.log('Redirecting to signup...');
          }, 1500);
      }
    });
  });
const sections = document.querySelectorAll('section[id]');
window.addEventListener('scroll', () => {
  let e = '';
  sections.forEach((t) => {
    let o = t.offsetTop;
    t.clientHeight, pageYOffset >= o - 200 && (e = t.getAttribute('id'));
  }),
    navLinks.forEach((t) => {
      t.classList.remove('active'),
        t.getAttribute('href') === `#${e}` && t.classList.add('active');
    });
}),
  window.addEventListener('scroll', () => {
    let e = window.pageYOffset,
      t = document.querySelectorAll('.gradient-orb');
    t.forEach((t, o) => {
      let a = (o + 1) * 0.5;
      t.style.transform = `translate(${e * a * 0.1}px, ${e * a * 0.1}px)`;
    });
  }),
  document.addEventListener('DOMContentLoaded', () => {
    console.log('SignTry landing page loaded');
    let e = document.querySelector('.hero-content');
    e &&
      setTimeout(() => {
        (e.style.opacity = '1'), (e.style.transform = 'translateY(0)');
      }, 100);
    let t = document.getElementById('billing-toggle');
    t &&
      t.addEventListener('change', function () {
        this.checked
          ? document.body.classList.add('yearly-billing')
          : document.body.classList.remove('yearly-billing');
      });
    let o = document.querySelectorAll('.tab-button'),
      a = document.querySelectorAll('.tab-content');
    o.forEach((e) => {
      e.addEventListener('click', () => {
        console.log('Tab clicked:', e.getAttribute('data-tab')),
          o.forEach((e) => e.classList.remove('active')),
          a.forEach((e) => e.classList.remove('active')),
          e.classList.add('active');
        let t = e.getAttribute('data-tab') + '-tab',
          n = document.getElementById(t);
        n
          ? (n.classList.add('active'), console.log('Showing tab:', t))
          : console.error('Tab not found:', t);
      });
    }),
      console.log('Tab buttons found:', o.length),
      console.log('Tab contents found:', a.length);
  }),
  document.addEventListener('dragstart', function (e) {
    'IMG' === e.target.tagName && e.preventDefault();
  }),
  document.addEventListener('selectstart', function (e) {
    (e.target.closest('.signature-card-wrapper') ||
      e.target.closest('.example-placeholder')) &&
      e.preventDefault();
  }),
  document.addEventListener('copy', function (e) {
    (window.getSelection().toString().includes('@') ||
      e.target.closest('.signature-protected')) &&
      e.preventDefault();
  }),
  document.addEventListener('cut', function (e) {
    e.preventDefault();
  });
