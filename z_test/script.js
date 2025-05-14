// 获取元素
const quantityInput = document.querySelector('.quantity-input');
const increaseButton = document.querySelector('.increase');
const decreaseButton = document.querySelector('.decrease');
const totalPrice = document.querySelector('.total-price em');
const buyNowButton = document.querySelector('.buy-now');
const addToCartButton = document.querySelector('.add-to-cart');
const descriptionTab = document.querySelector('.detail-tabs li:nth-child(1)');
const reviewsTab = document.querySelector('.detail-tabs li:nth-child(2)');
const productDescription = document.querySelector('.product-description');
const productReviews = document.querySelector('.product-reviews');

// 初始化总价
function updateTotalPrice() {
    const price = 1299;
    const quantity = parseInt(quantityInput.value);
    const total = price * quantity;
    totalPrice.textContent = total.toFixed(2) + '元';
}

// 增加数量
increaseButton.addEventListener('click', function () {
    const currentQuantity = parseInt(quantityInput.value);
    quantityInput.value = currentQuantity + 1;
    updateTotalPrice();
});

// 减少数量
decreaseButton.addEventListener('click', function () {
    const currentQuantity = parseInt(quantityInput.value);
    if (currentQuantity > 1) {
        quantityInput.value = currentQuantity - 1;
    }
    updateTotalPrice();
});

// 监听数量输入框变化
quantityInput.addEventListener('input', function () {
    const quantity = parseInt(quantityInput.value);
    if (isNaN(quantity) || quantity < 1) {
        quantityInput.value = 1;
    }
    updateTotalPrice();
});

// 切换商品介绍和评论选项卡
descriptionTab.addEventListener('click', function () {
    descriptionTab.classList.add('active');
    reviewsTab.classList.remove('active');
    productDescription.style.display = 'block';
    productReviews.style.display = 'none';
});

reviewsTab.addEventListener('click', function () {
    reviewsTab.classList.add('active');
    descriptionTab.classList.remove('active');
    productReviews.style.display = 'block';
    productDescription.style.display = 'none';
});

// 立即购买按钮点击事件（可替换为实际逻辑）
buyNowButton.addEventListener('click', function () {
    alert('立即购买功能暂未实现');
});

// 加入购物车按钮点击事件（可替换为实际逻辑）
addToCartButton.addEventListener('click', function () {
    alert('加入购物车功能暂未实现');
});