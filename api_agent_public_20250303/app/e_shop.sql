-- 用户表
CREATE TABLE users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password_hash VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(20),
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- 商品分类表
CREATE TABLE categories (
    category_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    parent_id INT DEFAULT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- 商品表
CREATE TABLE products (
    product_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    price DECIMAL(10,2) NOT NULL,
    stock INT DEFAULT 0,
    category_id INT NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (category_id) REFERENCES categories(category_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- 收货地址表
CREATE TABLE addresses (
    address_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    recipient_name VARCHAR(50) NOT NULL,
    phone VARCHAR(20) NOT NULL,
    province VARCHAR(50) NOT NULL,
    city VARCHAR(50) NOT NULL,
    district VARCHAR(50) NOT NULL,
    detail_address VARCHAR(200) NOT NULL,
    is_default BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- 订单表
CREATE TABLE orders (
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    address_id INT NOT NULL,
    total_amount DECIMAL(10,2) NOT NULL,
    status ENUM('pending', 'paid', 'shipped', 'completed', 'cancelled') DEFAULT 'pending',
    order_no VARCHAR(50) UNIQUE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (address_id) REFERENCES addresses(address_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- 订单明细表
CREATE TABLE order_items (
    item_id INT AUTO_INCREMENT PRIMARY KEY,
    order_id INT NOT NULL,
    product_id INT NOT NULL,
    quantity INT NOT NULL,
    unit_price DECIMAL(10,2) NOT NULL,
    FOREIGN KEY (order_id) REFERENCES orders(order_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- 购物车表
CREATE TABLE carts (
    cart_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    product_id INT NOT NULL,
    quantity INT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- 支付信息表
CREATE TABLE payments (
    payment_id INT AUTO_INCREMENT PRIMARY KEY,
    order_id INT NOT NULL,
    amount DECIMAL(10,2) NOT NULL,
    payment_method VARCHAR(20) NOT NULL,
    transaction_id VARCHAR(100),
    status ENUM('pending', 'success', 'failed') DEFAULT 'pending',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (order_id) REFERENCES orders(order_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;


-- 用户数据
INSERT INTO users (username, password_hash, email, phone) VALUES
('zhangsan', 'hashed_password_1', 'zhangsan@example.com', '13800138000'),
('lisi', 'hashed_password_2', 'lisi@example.com', '13900139000');

-- 分类数据
INSERT INTO categories (name, parent_id) VALUES
('电子产品', NULL),
('手机', 1),
('笔记本电脑', 1),
('服装', NULL);

-- 商品数据
INSERT INTO products (name, description, price, stock, category_id) VALUES
('iPhone 14', '苹果最新智能手机', 6999.00, 100, 2),
('华为MateBook X Pro', '轻薄笔记本电脑', 8999.00, 50, 3),
('男士休闲衬衫', '纯棉商务衬衫', 199.00, 200, 4);

-- 地址数据
INSERT INTO addresses (user_id, recipient_name, phone, province, city, district, detail_address) VALUES
(1, '张三', '13800138000', '北京市', '市辖区', '朝阳区', '朝阳门外大街1号');

-- 购物车数据
INSERT INTO carts (user_id, product_id, quantity) VALUES
(1, 1, 2),
(1, 2, 1);