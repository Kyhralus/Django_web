// 左侧导航栏交互逻辑
document.addEventListener('DOMContentLoaded', function() {
  // 获取导航元素
  const navItems = document.querySelectorAll('.main-nav .has-submenu');
  const recommendItems = document.querySelectorAll('.recommend-item');
  const scrollTargets = document.querySelectorAll('.scroll-target');

  // 初始化子菜单
  initSubmenus();

  // 为推荐项添加动画效果
  animateRecommendItems();

  // 实现平滑滚动
  implementSmoothScroll();

  // 检测滚动位置，添加导航栏阴影
  window.addEventListener('scroll', handleScroll);

  // 高亮当前导航项
  highlightCurrentNavItem();
});

// 初始化子菜单
function initSubmenus() {
  navItems.forEach(item => {
    const link = item.querySelector('.nav-link');

    // 点击菜单项展开/折叠子菜单
    link.addEventListener('click', function(e) {
      e.preventDefault();

      // 关闭其他所有子菜单
      document.querySelectorAll('.has-submenu.open').forEach(openItem => {
        if (openItem !== item) {
          openItem.classList.remove('open');
          openItem.querySelector('.submenu').style.maxHeight = null;
        }
      });

      // 切换当前子菜单
      const isOpen = item.classList.contains('open');
      const submenu = item.querySelector('.submenu');

      if (isOpen) {
        item.classList.remove('open');
        submenu.style.maxHeight = null;
      } else {
        item.classList.add('open');
        submenu.style.maxHeight = submenu.scrollHeight + 'px';
      }
    });
  });
}

// 为推荐项添加动画效果
function animateRecommendItems() {
  recommendItems.forEach((item, index) => {
    // 添加延迟的淡入动画
    setTimeout(() => {
      item.style.opacity = '1';
      item.style.transform = 'translateY(0)';
    }, 100 * index);
  });
}

// 实现平滑滚动
function implementSmoothScroll() {
  // 为所有内部链接添加平滑滚动
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
      e.preventDefault();

      const targetId = this.getAttribute('href');
      if (targetId === '#') return;

      const targetElement = document.querySelector(targetId);
      if (targetElement) {
        window.scrollTo({
          top: targetElement.offsetTop - 20,
          behavior: 'smooth'
        });
      }
    });
  });
}

// 处理滚动事件
function handleScroll() {
  const sidebar = document.querySelector('.left-sidebar');

  // 当滚动时添加阴影效果
  if (window.scrollY > 10) {
    sidebar.classList.add('scrolled');
  } else {
    sidebar.classList.remove('scrolled');
  }

  // 滚动时高亮当前区域对应的导航项
  highlightCurrentNavItem();
}

// 高亮当前导航项
function highlightCurrentNavItem() {
  const scrollPosition = window.scrollY;

  scrollTargets.forEach(target => {
    const targetTop = target.offsetTop - 100;
    const targetBottom = targetTop + target.offsetHeight;
    const targetId = target.getAttribute('id');

    if (scrollPosition >= targetTop && scrollPosition < targetBottom) {
      // 移除所有导航项的高亮
      document.querySelectorAll('.main-nav .nav-link').forEach(link => {
        link.classList.remove('active');
      });

      // 高亮对应的导航项
      const navLink = document.querySelector(`.main-nav .nav-link[href="#${targetId}"]`);
      if (navLink) {
        navLink.classList.add('active');
      }
    }
  });
}