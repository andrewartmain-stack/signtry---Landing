/* ============================================
   1. NAVIGATION & SMOOTH SCROLL
   ============================================ */

// Mobile Navigation Toggle
const navToggle = document.getElementById('navToggle'),
  navMenu = document.getElementById('navMenu');

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

// Smooth scroll for anchor links
document.querySelectorAll('a[href^="#"]').forEach((anchor) => {
  anchor.addEventListener('click', function (e) {
    e.preventDefault();
    let target = document.querySelector(this.getAttribute('href'));
    if (target) {
      let offsetTop = target.offsetTop - 80;
      window.scrollTo({ top: offsetTop, behavior: 'smooth' });
    }
  });
});

// Active nav link on scroll
window.addEventListener('scroll', () => {
  const sections = document.querySelectorAll('section[id]');
  let currentSection = '';

  sections.forEach((section) => {
    const sectionTop = section.offsetTop;
    if (pageYOffset >= sectionTop - 200) {
      currentSection = section.getAttribute('id');
    }
  });

  navLinks.forEach((link) => {
    link.classList.remove('active');
    if (link.getAttribute('href') === `#${currentSection}`) {
      link.classList.add('active');
    }
  });
});

/* ============================================
   2. FAQ ACCORDION
   ============================================ */

const faqItems = document.querySelectorAll('.faq-item');
faqItems.forEach((item) => {
  const question = item.querySelector('.faq-question');
  question.addEventListener('click', () => {
    const isActive = item.classList.contains('active');

    // Close all other FAQ items
    faqItems.forEach((faqItem) => {
      faqItem.classList.remove('active');
    });

    // Open current item if it was closed
    if (!isActive) {
      item.classList.add('active');
    }
  });
});

/* ============================================
   3. VIDEO MODAL
   ============================================ */

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

// Open video modal
function openVideoModal() {
  videoModal.classList.add('active');
  document.body.style.overflow = 'hidden';
  modalVideo.src = videoUrl + '?autoplay=1';
}

// Close video modal
function closeVideoModal() {
  videoModal.classList.remove('active');
  document.body.style.overflow = '';
  modalVideo.src = '';
}

// Event listeners for video modal
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

// Play button in demo section
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

    if (demoVideo) {
      demoVideo.src = videoUrl + '?autoplay=1';
    }
  });
}

// Reset demo video when modal closes
if (videoModal) {
  videoModal.addEventListener('transitionend', function (e) {
    if (!videoModal.classList.contains('active') && videoOverlay && demoVideo) {
      demoVideo.src = '';
    }
  });
}

/* ============================================
   4. ANIMATIONS & INTERSECTION OBSERVER
   ============================================ */

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

// Animate elements on scroll
const animateOnScroll = document.querySelectorAll(
  '.feature-card, .pricing-card, .faq-item, .single-purchase-card'
);

animateOnScroll.forEach((element) => {
  element.style.opacity = '0';
  element.style.transform = 'translateY(20px)';
  element.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
  observer.observe(element);
});

/* ============================================
   5. COUNTER ANIMATIONS
   ============================================ */

// Counter animation function
function animateCounter(element, target, duration = 2000) {
  let increment = target / (duration / 16);
  let current = 0;

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

// Format numbers with K+ or M+
function formatNumber(number) {
  if (number >= 1000000) {
    return (number / 1000000).toFixed(1) + 'M+';
  } else if (number >= 1000) {
    return (number / 1000).toFixed(0) + 'K+';
  }
  return number.toString();
}

// Stats counter observer
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
          let text = stat.textContent;

          if (text.includes('K+')) {
            let target = 1000 * parseFloat(text);
            animateCounter(stat, target);
          } else if (text.includes('M+')) {
            let target = 1000000 * parseFloat(text);
            animateCounter(stat, target);
          } else if (text.includes('/')) {
            // Skip numbers with slashes (like in pricing)
            return;
          }
        });
      }
    });
  },
  { threshold: 0.5 }
);

// Observe hero stats
const heroStats = document.querySelector('.hero-stats');
if (heroStats) {
  statsObserver.observe(heroStats);
}

/* ============================================
   6. PRICING SECTION FUNCTIONALITY (NEW)
   ============================================ */

function initPricingSection() {
  // Billing Toggle (Monthly/Yearly)
  const billingToggleCheckbox = document.getElementById('billing-toggle');
  const billingOptions = document.querySelectorAll('.billing-option');

  // One-Time Purchase Button
  const singlePurchaseBtn = document.getElementById('singlePurchaseBtn');

  // Billing Toggle Event Listeners (Monthly/Yearly)
  if (billingOptions.length && billingToggleCheckbox) {
    billingOptions.forEach((option) => {
      option.addEventListener('click', function () {
        if (this.classList.contains('active')) return;

        // Update active option
        billingOptions.forEach((opt) => opt.classList.remove('active'));
        this.classList.add('active');

        // Update checkbox state
        const billingType = this.dataset.billing;
        billingToggleCheckbox.checked = billingType === 'yearly';
        document.body.classList.toggle(
          'yearly-billing',
          billingType === 'yearly'
        );
      });
    });

    billingToggleCheckbox.addEventListener('change', function () {
      const billingType = this.checked ? 'yearly' : 'monthly';

      // Update active option
      billingOptions.forEach((opt) => opt.classList.remove('active'));
      const activeOption = document.querySelector(
        `.billing-option[data-billing="${billingType}"]`
      );
      if (activeOption) activeOption.classList.add('active');

      // Update body class
      document.body.classList.toggle('yearly-billing', this.checked);
    });
  }

  // Order Form Functionality (Modal)
  if (singlePurchaseBtn) {
    // Create and append modal if it doesn't exist
    if (!document.getElementById('orderModal')) {
      const modalHTML = `
        <div class="modal-overlay" id="orderModal">
          <div class="modal-content">
            <button class="modal-close" id="closeOrderModal">&times;</button>
            <div class="order-form-header">
              <h3>Order Your Signature</h3>
              <p> You pay $10 one time — and if SignTry doesn’t meet your expectations,
        just email us within 14 days and we’ll refund your payment in full.<br>
        No questions asked.</p>
            </div>
            <div class="order-options">
              <div class="order-option" style="text-align: center;">
                <button style="margin-bottom: 10px;" class="btn-primary" id="quickOrderBtn">Quick Order - $10</button>
                <p>We'll contact you in 15 min via email to collect your signature details.</p>
              </div>
            </div>
          </div>
        </div>
      `;
      document.body.insertAdjacentHTML('beforeend', modalHTML);
    }

    const orderModal = document.getElementById('orderModal');
    const closeOrderModal = document.getElementById('closeOrderModal');
    const quickOrderBtn = document.getElementById('quickOrderBtn');

    // Open order modal
    singlePurchaseBtn.addEventListener('click', function (e) {
      e.preventDefault();
      orderModal.classList.add('active');
      document.body.style.overflow = 'hidden';
    });

    // Close order modal
    if (closeOrderModal) {
      closeOrderModal.addEventListener('click', function () {
        orderModal.classList.remove('active');
        document.body.style.overflow = '';
      });
    }

    // Close modal when clicking outside
    if (orderModal) {
      orderModal.addEventListener('click', function (e) {
        if (e.target === this) {
          this.classList.remove('active');
          document.body.style.overflow = '';
        }
      });
    }

    // Quick order (email)
    if (quickOrderBtn) {
      quickOrderBtn.addEventListener('click', function () {
        const orderLink = `https://buy.stripe.com/cNi6oGeER2vo0NU1Ng93y00`;
        window.location.href = orderLink;

        // Close modal after a delay
        setTimeout(() => {
          orderModal.classList.remove('active');
          document.body.style.overflow = '';
        }, 500);
      });
    }
  }
}

/* ============================================
   7. BUTTON LOADING STATES
   ============================================ */

function initButtonLoading() {
  document
    .querySelectorAll('.btn-primary, .btn-secondary')
    .forEach((button) => {
      button.addEventListener('click', function (e) {
        // Only apply loading state to signup/trial buttons
        if (
          this.textContent.includes('Start') ||
          this.textContent.includes('Trial') ||
          this.textContent.includes('Get Started')
        ) {
          let originalHTML = this.innerHTML;
          this.innerHTML = 'Loading...';
          this.disabled = true;

          setTimeout(() => {
            this.innerHTML = originalHTML;
            this.disabled = false;
            console.log('Redirecting to signup...');
            // In production, this would be an actual redirect
            // window.location.href = 'https://app.signtry.com/signup';
          }, 1500);
        }
      });
    });
}

/* ============================================
   8. PARALLAX EFFECTS
   ============================================ */

function initParallax() {
  window.addEventListener('scroll', () => {
    const scrollPosition = window.pageYOffset;
    const gradientOrbs = document.querySelectorAll('.gradient-orb');

    gradientOrbs.forEach((orb, index) => {
      let speed = (index + 1) * 0.5;
      orb.style.transform = `translate(${scrollPosition * speed * 0.1}px, ${
        scrollPosition * speed * 0.1
      }px)`;
    });
  });
}

/* ============================================
   9. TAB FUNCTIONALITY (SCREENSHOTS)
   ============================================ */

function initTabs() {
  const tabButtons = document.querySelectorAll('.tab-button');
  const tabContents = document.querySelectorAll('.tab-content');

  if (tabButtons.length && tabContents.length) {
    tabButtons.forEach((button) => {
      button.addEventListener('click', () => {
        console.log('Tab clicked:', button.getAttribute('data-tab'));

        // Remove active class from all buttons and contents
        tabButtons.forEach((btn) => btn.classList.remove('active'));
        tabContents.forEach((content) => content.classList.remove('active'));

        // Add active class to clicked button
        button.classList.add('active');

        // Show corresponding tab content
        const tabId = button.getAttribute('data-tab') + '-tab';
        const tabContent = document.getElementById(tabId);

        if (tabContent) {
          tabContent.classList.add('active');
          console.log('Showing tab:', tabId);
        } else {
          console.error('Tab content not found:', tabId);
        }
      });
    });

    console.log('Tab buttons found:', tabButtons.length);
    console.log('Tab contents found:', tabContents.length);
  }
}

/* ============================================
   10. ANTI-COPY PROTECTION
   ============================================ */

function initAntiCopy() {
  // Prevent dragging images
  document.addEventListener('dragstart', function (e) {
    if (e.target.tagName === 'IMG') {
      e.preventDefault();
    }
  });

  // Prevent text selection on protected elements
  document.addEventListener('selectstart', function (e) {
    if (
      e.target.closest('.signature-card-wrapper') ||
      e.target.closest('.example-placeholder')
    ) {
      e.preventDefault();
    }
  });

  // Prevent copying email addresses
  document.addEventListener('copy', function (e) {
    if (
      window.getSelection().toString().includes('@') ||
      e.target.closest('.signature-protected')
    ) {
      e.preventDefault();
    }
  });

  // Prevent cutting
  document.addEventListener('cut', function (e) {
    e.preventDefault();
  });
}

/* ============================================
   11. EMAIL VALIDATION (UTILITY)
   ============================================ */

function validateEmail(email) {
  return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
}

/* ============================================
   12. INITIALIZATION ON DOM LOAD
   ============================================ */

document.addEventListener('DOMContentLoaded', () => {
  console.log('SignTry landing page loaded');

  // Initialize all modules
  initPricingSection();
  initButtonLoading();
  initParallax();
  initTabs();
  initAntiCopy();

  // Hero content animation
  const heroContent = document.querySelector('.hero-content');
  if (heroContent) {
    setTimeout(() => {
      heroContent.style.opacity = '1';
      heroContent.style.transform = 'translateY(0)';
    }, 100);
  }

  // Log initialization
  console.log('All modules initialized successfully');
});

/* ============================================
   13. WINDOW LOAD EVENT
   ============================================ */

window.addEventListener('load', () => {
  // Any additional initialization that requires all resources to be loaded
  console.log('Page fully loaded');
});

/* ============================================
   14. ERROR HANDLING
   ============================================ */

window.addEventListener('error', (e) => {
  console.error(
    'JavaScript Error:',
    e.message,
    'at',
    e.filename,
    ':',
    e.lineno
  );
});

// Global error handler for unhandled promise rejections
window.addEventListener('unhandledrejection', (e) => {
  console.error('Unhandled Promise Rejection:', e.reason);
});
