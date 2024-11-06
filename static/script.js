// Xử lý form đăng nhập
document.getElementById("loginForm")?.addEventListener("submit", async (event) => {
    event.preventDefault();

    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;

    const response = await fetch("/api/login", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ email, password })
    });

    const data = await response.json();
    document.getElementById("message").innerText = data.message;

    if (response.status === 200) {
        window.location.href = "/profile";
    }
});

// Xử lý form đăng ký
document.getElementById("registerForm")?.addEventListener("submit", async (event) => {
    event.preventDefault();

    const email = document.getElementById("registerEmail").value;
    const password = document.getElementById("registerPassword").value;

    const response = await fetch("/api/register", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ email, password })
    });

    const data = await response.json();
    document.getElementById("registerMessage").innerText = data.message;

    if (response.status === 201) {
        window.location.href = "/";
    }
});
// Đã sửa file âhhahahahahaha

