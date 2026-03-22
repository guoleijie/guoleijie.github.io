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

// 移动端菜单切换
const menuToggle = document.getElementById('menuToggle');
const navLinks = document.getElementById('navLinks');

if (menuToggle && navLinks) {
  menuToggle.addEventListener('click', () => {
    navLinks.classList.toggle('active');
  });

  // 点击链接后关闭菜单
  navLinks.querySelectorAll('a').forEach(link => {
    link.addEventListener('click', () => {
      navLinks.classList.remove('active');
    });
  });

  // 点击页面其他地方关闭菜单
  document.addEventListener('click', (e) => {
    if (!navLinks.contains(e.target) && !menuToggle.contains(e.target)) {
      navLinks.classList.remove('active');
    }
  });
}

// 页面滚动进度
const progressBar = document.querySelector('.progress-bar');
if (progressBar) {
  window.addEventListener('scroll', () => {
    const scrollTop = window.scrollY;
    const docHeight = document.documentElement.scrollHeight - window.innerHeight;
    const progress = (scrollTop / docHeight) * 100;
    progressBar.style.width = progress + '%';
  });
}

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
        background: #e85d3a;
        color: white;
        border: none;
        cursor: pointer;
        box-shadow: 0 4px 12px rgba(192, 57, 43, 0.3);
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
