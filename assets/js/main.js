// 平滑滚动
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
  anchor.addEventListener('click', function (e) {
    e.preventDefault();
    const target = document.querySelector(this.getAttribute('href'));
    if (target) {
      target.scrollIntoView({
        behavior: 'smooth',
        block: 'start'
      });
    }
  });
});

// 返回顶部
let backToTopBtn = null;

window.addEventListener('scroll', () => {
  if (window.scrollY > 300) {
    if (!backToTopBtn) {
      backToTopBtn = document.createElement('button');
      backToTopBtn.innerHTML = '<i data-lucide="arrow-up"></i>';
      backToTopBtn.style.cssText = `
        position: fixed;
        bottom: 24px;
        right: 24px;
        width: 48px;
        height: 48px;
        border-radius: 50%;
        background: #3b82f6;
        color: white;
        border: none;
        cursor: pointer;
        box-shadow: 0 4px 12px rgba(59, 130, 246, 0.3);
        z-index: 999;
        display: flex;
        align-items: center;
        justify-content: center;
        transition: 0.3s;
      `;
      backToTopBtn.addEventListener('click', () => {
        window.scrollTo({
          top: 0,
          behavior: 'smooth'
        });
      });
      document.body.appendChild(backToTopBtn);
      lucide.createIcons();
    }
    backToTopBtn.style.opacity = '1';
  } else if (backToTopBtn) {
    backToTopBtn.style.opacity = '0';
  }
});

// 页面加载完成
document.addEventListener('DOMContentLoaded', () => {
  console.log('📄 页面加载完成');
  lucide.createIcons();
});
