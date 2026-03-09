// ==================== 打字机效果 ====================
class TypeWriter {
    constructor(elements) {
        this.elements = elements;
        this.currentIndex = 0;
        this.init();
    }

    init() {
        // 显示第一个元素
        this.elements[0].classList.add('active');
        
        // 每3秒切换一次
        setInterval(() => {
            this.next();
        }, 3000);
    }

    next() {
        // 移除当前激活状态
        this.elements[this.currentIndex].classList.remove('active');
        
        // 切换到下一个
        this.currentIndex = (this.currentIndex + 1) % this.elements.length;
        
        // 添加激活状态
        this.elements[this.currentIndex].classList.add('active');
    }
}

// ==================== 滚动效果 ====================
class ScrollEffects {
    constructor() {
        this.navbar = document.querySelector('.navbar');
        this.backToTopBtn = document.getElementById('backToTop');
        this.init();
    }

    init() {
        // 监听滚动事件
        window.addEventListener('scroll', () => {
            this.handleScroll();
        });

        // 返回顶部按钮点击事件
        if (this.backToTopBtn) {
            this.backToTopBtn.addEventListener('click', () => {
                this.scrollToTop();
            });
        }

        // 平滑滚动
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {
            anchor.addEventListener('click', (e) => {
                e.preventDefault();
                const target = document.querySelector(anchor.getAttribute('href'));
                if (target) {
                    target.scrollIntoView({
                        behavior: 'smooth',
                        block: 'start'
                    });
                }
            });
        });
    }

    handleScroll() {
        const scrollY = window.scrollY;

        // 导航栏背景变化
        if (scrollY > 100) {
            this.navbar.style.background = 'rgba(10, 10, 10, 0.98)';
        } else {
            this.navbar.style.background = 'rgba(10, 10, 10, 0.9)';
        }

        // 返回顶部按钮显示/隐藏
        if (scrollY > 500) {
            this.backToTopBtn.classList.add('visible');
        } else {
            this.backToTopBtn.classList.remove('visible');
        }

        // 元素进入视口动画
        this.animateOnScroll();
    }

    animateOnScroll() {
        const elements = document.querySelectorAll('.section, .project-card, .skill-card, .stat-card');
        
        elements.forEach(element => {
            const elementTop = element.getBoundingClientRect().top;
            const elementBottom = element.getBoundingClientRect().bottom;
            
            if (elementTop < window.innerHeight - 100 && elementBottom > 0) {
                element.classList.add('fade-in-up');
            }
        });
    }

    scrollToTop() {
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    }
}

// ==================== 统计数字动画 ====================
class CountUp {
    constructor(element, target, duration = 2000) {
        this.element = element;
        this.target = target;
        this.duration = duration;
        this.start = 0;
        this.hasAnimated = false;
    }

    animate() {
        if (this.hasAnimated) return;
        
        const increment = this.target / (this.duration / 16);
        let current = this.start;

        const timer = setInterval(() => {
            current += increment;
            if (current >= this.target) {
                current = this.target;
                clearInterval(timer);
            }
            this.element.textContent = Math.floor(current) + '+';
        }, 16);

        this.hasAnimated = true;
    }
}

// ==================== 初始化 ====================
document.addEventListener('DOMContentLoaded', () => {
    // 打字机效果
    const typingElements = document.querySelectorAll('.text-item');
    if (typingElements.length > 0) {
        new TypeWriter(typingElements);
    }

    // 滚动效果
    new ScrollEffects();

    // 统计数字动画
    const statNumbers = document.querySelectorAll('.stat-number');
    statNumbers.forEach(stat => {
        const text = stat.textContent;
        const number = parseInt(text);
        if (!isNaN(number) && number > 0) {
            const countUp = new CountUp(stat, number);
            
            // 当元素进入视口时触发动画
            const observer = new IntersectionObserver((entries) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        countUp.animate();
                        observer.unobserve(entry.target);
                    }
                });
            }, { threshold: 0.5 });

            observer.observe(stat);
        }
    });

    // 导航栏活跃状态
    const sections = document.querySelectorAll('section[id], header[id]');
    const navLinks = document.querySelectorAll('.nav-links a');

    window.addEventListener('scroll', () => {
        let current = '';
        
        sections.forEach(section => {
            const sectionTop = section.offsetTop;
            const sectionHeight = section.clientHeight;
            
            if (window.scrollY >= sectionTop - 200) {
                current = section.getAttribute('id');
            }
        });

        navLinks.forEach(link => {
            link.style.color = '';
            if (link.getAttribute('href') === `#${current}`) {
                link.style.color = 'var(--text-primary)';
            }
        });
    });
});

// ==================== 性能优化 ====================
// 节流函数
function throttle(func, limit) {
    let inThrottle;
    return function(...args) {
        if (!inThrottle) {
            func.apply(this, args);
            inThrottle = true;
            setTimeout(() => inThrottle = false, limit);
        }
    }
}

// 优化滚动事件
window.addEventListener('scroll', throttle(() => {
    // 滚动处理逻辑
}, 100));
