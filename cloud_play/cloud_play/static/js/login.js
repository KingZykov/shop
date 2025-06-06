            // Modal functionality
            const loginModal = document.getElementById("loginModal");
            const registerModal = document.getElementById("registerModal");
            const loginBtn = document.getElementById("loginBtn");
            const registerBtn = document.getElementById("registerBtn");
            const switchToRegister = document.getElementById("switchToRegister");
            const switchToLogin = document.getElementById("switchToLogin");
            const closeButtons = document.getElementsByClassName("close");
            const ctaButton = document.querySelector('.cta-button');
            
            // Обработчики для кнопок
            if (loginBtn) {
                loginBtn.addEventListener('click', function() {
                    loginModal.style.display = "block";
                });
            }
            
            if (registerBtn) {
                registerBtn.addEventListener('click', function() {
                    registerModal.style.display = "block";
                });
            }
            
            if (ctaButton) {
                ctaButton.addEventListener('click', function(e) {
                    e.preventDefault();
                    loginModal.style.display = "block";
                });
            }
            
            // Переключение между модальными окнами
            if (switchToRegister) {
                switchToRegister.addEventListener('click', function(e) {
                    e.preventDefault();
                    loginModal.style.display = "none";
                    registerModal.style.display = "block";
                });
            }
            
            if (switchToLogin) {
                switchToLogin.addEventListener('click', function(e) {
                    e.preventDefault();
                    registerModal.style.display = "none";
                    loginModal.style.display = "block";
                });
            }
            
            // Закрытие модальных окон
            for (let i = 0; i < closeButtons.length; i++) {
                closeButtons[i].addEventListener('click', function() {
                    loginModal.style.display = "none";
                    registerModal.style.display = "none";
                });
            }
            
{% comment %}            // Закрытие при клике вне модального окна
            window.addEventListener('click', function(event) {
                if (event.target == loginModal) {
                    loginModal.style.display = "none";
                }
                if (event.target == registerModal) {
                    registerModal.style.display = "none";
                }
            }); {% endcomment %}
            
{% comment %}             // Обработка отправки форм
            const loginForm = document.getElementById("loginForm");
            const registerForm = document.getElementById("registerForm");
            const feedbackForm = document.getElementById("feedbackForm");
            
            if (loginForm) {
                loginForm.addEventListener('submit', function(e) {
                 /**   e.preventDefault(); **/
                    alert("Вход выполнен успешно!");
                    loginModal.style.display = "none";
                });
            }
            
            if (registerForm) {
                registerForm.addEventListener('submit', function(e) {
                   /** e.preventDefault(); **/
                    alert("Регистрация прошла успешно!");
                    registerModal.style.display = "none";
                });
            } {% endcomment %}
            
            if (feedbackForm) {
                feedbackForm.addEventListener('submit', function(e) {
                    e.preventDefault();
                    alert("Ваше сообщение отправлено. Мы свяжемся с вами в ближайшее время!");
                    this.reset();
                });
            }

            document.addEventListener('DOMContentLoaded', () => {
            const modal = document.getElementById('profileModal');
            const btn = document.getElementById('profileBtn');
            const closeBtn = document.getElementById('closeProfile');

            // Показ кнопки "Личный кабинет" если авторизован
            {% if user.is_authenticated %}
                btn.style.display = 'inline-block';
            {% endif %}

            btn.addEventListener('click', () => {
                modal.style.display = 'block';
            });

            closeBtn.addEventListener('click', () => {
                modal.style.display = 'none';
            });

            });