// Mobile Navigation Toggle
const navToggle = document.getElementById('navToggle');
const navMenu = document.getElementById('navMenu');

navToggle.addEventListener('click', () => {
  navMenu.classList.toggle('active');
});

// Close mobile menu when clicking on a link
const navLinks = navMenu.querySelectorAll('a');
navLinks.forEach((link) => {
  link.addEventListener('click', () => {
    navMenu.classList.remove('active');
  });
});

// Smooth Scrolling for Navigation Links
document.querySelectorAll('a[href^="#"]').forEach((anchor) => {
  anchor.addEventListener('click', function (e) {
    e.preventDefault();
    const target = document.querySelector(this.getAttribute('href'));
    if (target) {
      const offset = 80;
      const targetPosition = target.offsetTop - offset;
      window.scrollTo({
        top: targetPosition,
        behavior: 'smooth',
      });
    }
  });
});

// Navbar Scroll Effect
let lastScroll = 0;
const navbar = document.querySelector('.navbar');

window.addEventListener('scroll', () => {
  const currentScroll = window.pageYOffset;

  if (currentScroll > 100) {
    navbar.style.boxShadow = '0 2px 10px rgba(0, 0, 0, 0.1)';
  } else {
    navbar.style.boxShadow = 'none';
  }

  lastScroll = currentScroll;
});

// FAQ Accordion
const faqItems = document.querySelectorAll('.faq-item');

faqItems.forEach((item) => {
  const question = item.querySelector('.faq-question');

  question.addEventListener('click', () => {
    const isActive = item.classList.contains('active');

    // Close all FAQ items
    faqItems.forEach((faq) => {
      faq.classList.remove('active');
    });

    // Open clicked item if it wasn't active
    if (!isActive) {
      item.classList.add('active');
    }
  });
});

// Video Modal Functionality - FIXED VERSION
const watchDemoBtn = document.getElementById('watchDemoBtn');
const playButton = document.getElementById('playButton');
const videoModal = document.getElementById('videoModal');
const closeModal = document.getElementById('closeModal');
const videoModalBackdrop = document.getElementById('videoModalBackdrop');
const modalVideo = document.getElementById('modalVideo');

// Inline video elements
const videoContainer = document.getElementById('videoContainer');
const videoOverlay = document.getElementById('videoOverlay');
const demoVideo = document.getElementById('demoVideo');

const videoUrl = 'https://www.youtube.com/embed/dQw4w9WgXcQ';

function openVideoModal() {
  videoModal.classList.add('active');
  document.body.style.overflow = 'hidden';
  // Set the video source with autoplay
  modalVideo.src = videoUrl + '?autoplay=1';
}

function closeVideoModal() {
  videoModal.classList.remove('active');
  document.body.style.overflow = '';
  // Stop the video by removing the source
  modalVideo.src = '';
}

// Event listeners for modal video
if (watchDemoBtn) {
  watchDemoBtn.addEventListener('click', openVideoModal);
}
if (closeModal) {
  closeModal.addEventListener('click', closeVideoModal);
}
if (videoModalBackdrop) {
  videoModalBackdrop.addEventListener('click', closeVideoModal);
}

// Close modal on Escape key
document.addEventListener('keydown', (e) => {
  if (
    e.key === 'Escape' &&
    videoModal &&
    videoModal.classList.contains('active')
  ) {
    closeVideoModal();
  }
});

// Inline Video Play - SEPARATE FUNCTIONALITY
if (playButton) {
  playButton.addEventListener('click', (e) => {
    e.preventDefault();
    e.stopPropagation();

    const videoPlaceholder = videoContainer.querySelector('.video-placeholder');
    if (videoPlaceholder) {
      videoPlaceholder.style.display = 'none';
    }
    if (videoOverlay) {
      videoOverlay.style.display = 'block';
    }

    // Set the video source for inline player
    if (demoVideo) {
      demoVideo.src = videoUrl + '?autoplay=1';
    }
  });
}

// Reset inline video when modal is closed (additional safety)
if (videoModal) {
  videoModal.addEventListener('transitionend', function (e) {
    if (!videoModal.classList.contains('active') && videoOverlay) {
      // Reset inline video if needed
      if (demoVideo) {
        demoVideo.src = '';
      }
    }
  });
}

// Scroll Animations
const observerOptions = {
  threshold: 0.1,
  rootMargin: '0px 0px -100px 0px',
};

const observer = new IntersectionObserver((entries) => {
  entries.forEach((entry) => {
    if (entry.isIntersecting) {
      entry.target.style.opacity = '1';
      entry.target.style.transform = 'translateY(0)';
    }
  });
}, observerOptions);

// Observe elements for animation
const animateOnScroll = document.querySelectorAll(
  '.feature-card, .pricing-card, .faq-item'
);
animateOnScroll.forEach((el) => {
  el.style.opacity = '0';
  el.style.transform = 'translateY(20px)';
  el.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
  observer.observe(el);
});

// Stats Counter Animation
function animateCounter(element, target, duration = 2000) {
  const start = 0;
  const increment = target / (duration / 16);
  let current = start;

  const timer = setInterval(() => {
    current += increment;
    if (current >= target) {
      element.textContent = formatNumber(target);
      clearInterval(timer);
    } else {
      element.textContent = formatNumber(Math.floor(current));
    }
  }, 16);
}

function formatNumber(num) {
  if (num >= 1000000) {
    return (num / 1000000).toFixed(1) + 'M+';
  } else if (num >= 1000) {
    return (num / 1000).toFixed(0) + 'K+';
  }
  return num.toString();
}

// Animate stats when they come into view
const statsObserver = new IntersectionObserver(
  (entries) => {
    entries.forEach((entry) => {
      if (
        entry.isIntersecting &&
        !entry.target.classList.contains('animated')
      ) {
        entry.target.classList.add('animated');
        const statNumbers = entry.target.querySelectorAll('.stat-number');

        statNumbers.forEach((stat) => {
          const text = stat.textContent;
          if (text.includes('K+')) {
            const num = parseFloat(text) * 1000;
            animateCounter(stat, num);
          } else if (text.includes('M+')) {
            const num = parseFloat(text) * 1000000;
            animateCounter(stat, num);
          } else if (text.includes('/')) {
            // Skip rating animations
            return;
          }
        });
      }
    });
  },
  { threshold: 0.5 }
);

const heroStats = document.querySelector('.hero-stats');
if (heroStats) {
  statsObserver.observe(heroStats);
}

// Form Validation (for future implementation)
function validateEmail(email) {
  const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return re.test(email);
}

// Loading state for buttons
document.querySelectorAll('.btn-primary, .btn-secondary').forEach((button) => {
  button.addEventListener('click', function (e) {
    if (
      this.textContent.includes('Start') ||
      this.textContent.includes('Trial')
    ) {
      // Simulate loading (replace with actual form submission)
      const originalText = this.innerHTML;
      this.innerHTML = 'Loading...';
      this.disabled = true;

      setTimeout(() => {
        this.innerHTML = originalText;
        this.disabled = false;
        // Redirect to signup page or show form
        console.log('Redirecting to signup...');
      }, 1500);
    }
  });
});

// Add active class to current section in navigation
const sections = document.querySelectorAll('section[id]');

window.addEventListener('scroll', () => {
  let current = '';

  sections.forEach((section) => {
    const sectionTop = section.offsetTop;
    const sectionHeight = section.clientHeight;

    if (pageYOffset >= sectionTop - 200) {
      current = section.getAttribute('id');
    }
  });

  navLinks.forEach((link) => {
    link.classList.remove('active');
    if (link.getAttribute('href') === `#${current}`) {
      link.classList.add('active');
    }
  });
});

// Parallax effect for hero orbs
window.addEventListener('scroll', () => {
  const scrolled = window.pageYOffset;
  const orbs = document.querySelectorAll('.gradient-orb');

  orbs.forEach((orb, index) => {
    const speed = (index + 1) * 0.5;
    orb.style.transform = `translate(${scrolled * speed * 0.1}px, ${
      scrolled * speed * 0.1
    }px)`;
  });
});

// Initialize page
document.addEventListener('DOMContentLoaded', () => {
  console.log('SignTry landing page loaded');

  // Add smooth reveal animation to hero content
  const heroContent = document.querySelector('.hero-content');
  if (heroContent) {
    setTimeout(() => {
      heroContent.style.opacity = '1';
      heroContent.style.transform = 'translateY(0)';
    }, 100);
  }

  // Billing Toggle
  const billingToggle = document.getElementById('billing-toggle');
  if (billingToggle) {
    billingToggle.addEventListener('change', function () {
      if (this.checked) {
        document.body.classList.add('yearly-billing');
      } else {
        document.body.classList.remove('yearly-billing');
      }
    });
  }

  // Screenshot tabs functionality - MOVED INSIDE DOMContentLoaded
  const tabButtons = document.querySelectorAll('.tab-button');
  const tabContents = document.querySelectorAll('.tab-content');

  tabButtons.forEach((button) => {
    button.addEventListener('click', () => {
      console.log('Tab clicked:', button.getAttribute('data-tab'));

      // Remove active class from all buttons and contents
      tabButtons.forEach((btn) => btn.classList.remove('active'));
      tabContents.forEach((content) => content.classList.remove('active'));

      // Add active class to clicked button
      button.classList.add('active');

      // Show corresponding content
      const tabId = button.getAttribute('data-tab') + '-tab';
      const targetTab = document.getElementById(tabId);

      if (targetTab) {
        targetTab.classList.add('active');
        console.log('Showing tab:', tabId);
      } else {
        console.error('Tab not found:', tabId);
      }
    });
  });

  // Debug: Check if tabs are found
  console.log('Tab buttons found:', tabButtons.length);
  console.log('Tab contents found:', tabContents.length);
});

// Prevent drag start on images
document.addEventListener('dragstart', function (e) {
  if (e.target.tagName === 'IMG') {
    e.preventDefault();
  }
});

// Prevent selection
document.addEventListener('selectstart', function (e) {
  if (
    e.target.closest('.signature-card-wrapper') ||
    e.target.closest('.example-placeholder')
  ) {
    e.preventDefault();
  }
});

// Prevent copy
document.addEventListener('copy', function (e) {
  if (
    window.getSelection().toString().includes('@') || // Email detection
    e.target.closest('.signature-protected')
  ) {
    e.preventDefault();
  }
});

// Prevent cut
document.addEventListener('cut', function (e) {
  e.preventDefault();
});
