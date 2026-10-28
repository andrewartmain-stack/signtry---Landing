const navToggle = document.getElementById('navToggle');
const navMenu = document.getElementById('navMenu');

if (navToggle && navMenu) {
  const closeNavigation = () => {
    navMenu.classList.remove('active');
    navToggle.setAttribute('aria-expanded', 'false');
    navToggle.setAttribute('aria-label', 'Open navigation');
  };

  navToggle.addEventListener('click', () => {
    const isOpen = navMenu.classList.toggle('active');
    navToggle.setAttribute('aria-expanded', String(isOpen));
    navToggle.setAttribute(
      'aria-label',
      isOpen ? 'Close navigation' : 'Open navigation'
    );
  });

  navMenu.querySelectorAll('a').forEach((link) => {
    link.addEventListener('click', closeNavigation);
  });

  document.addEventListener('keydown', (event) => {
    if (event.key === 'Escape') closeNavigation();
  });

  document.addEventListener('click', (event) => {
    if (!navMenu.contains(event.target) && !navToggle.contains(event.target)) {
      closeNavigation();
    }
  });
}

document.querySelectorAll('.faq-question').forEach((question) => {
  question.addEventListener('click', () => {
    const item = question.closest('.faq-item');
    const isOpen = item.classList.toggle('active');
    question.setAttribute('aria-expanded', String(isOpen));
    question.querySelector('span').textContent = isOpen ? '−' : '+';
  });
});

const billingOptions = document.querySelectorAll('.billing-option');
const priceAmounts = document.querySelectorAll('.price-amount strong[data-monthly]');
const annualNotes = document.querySelectorAll('.annual-note');

billingOptions.forEach((option) => {
  option.addEventListener('click', () => {
    const isYearly = option.dataset.billing === 'yearly';

    billingOptions.forEach((billingOption) => {
      const isActive = billingOption === option;
      billingOption.classList.toggle('active', isActive);
      billingOption.setAttribute('aria-pressed', String(isActive));
    });

    priceAmounts.forEach((amount) => {
      amount.textContent = `$${amount.dataset[isYearly ? 'yearly' : 'monthly']}`;
    });

    annualNotes.forEach((note) => {
      note.hidden = !isYearly;
    });
  });
});

const currentYear = document.getElementById('currentYear');
if (currentYear) currentYear.textContent = new Date().getFullYear();
