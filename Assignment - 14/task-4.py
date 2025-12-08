
from flask import Flask, render_template_string, request

app = Flask(__name__)

login_html = '''
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Social Media Login Page</title>
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <style>
    body {
      margin: 0;
      min-height: 100vh;
      font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
      background: linear-gradient(-45deg, #1DA1F2, #4267B2, #DB4437, #833AB4, #FFB900);
      background-size: 400% 400%;
      animation: gradientMove 12s ease infinite;
      display: flex;
      align-items: center;
      justify-content: center;
    }
    @keyframes gradientMove {
      0% { background-position: 0% 50%; }
      25% { background-position: 50% 80%; }
      50% { background-position: 100% 50%; }
      75% { background-position: 50% 20%; }
      100% { background-position: 0% 50%; }
    }
    .center-container {
      min-height: 100vh;
      width: 100vw;
      display: flex;
      align-items: center;
      justify-content: center;
    }
    .login-box {
      background: rgba(255,255,255,0.9);
      padding: 38px 36px 28px 36px;
      border-radius: 18px;
      box-shadow: 0 8px 36px 0 rgba(31, 38, 135, 0.25), 0 2px 12px rgba(34,34,34,0.04);
      min-width: 320px;
      max-width: 380px;
      display: flex;
      flex-direction: column;
      align-items: center;
      position: relative;
      animation: popIn 0.5s ease;
    }
    @keyframes popIn {
      0% { 
        transform: scale(0.9) translateY(60px);
        opacity: 0;
      }
      100% { 
        transform: scale(1) translateY(0);
        opacity: 1;
      }
    }
    .login-box h2 {
      background: linear-gradient(90deg, #1da1f2, #4267b2, #e1306c, #ffb900);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      background-clip: text;
      text-fill-color: transparent;
      font-size: 2rem;
      font-weight: 700;
      margin-bottom: 22px;
      letter-spacing: 2px;
      animation: colorRoll 3s infinite linear;
    }
    @keyframes colorRoll {
      to { filter: hue-rotate(360deg); }
    }
    .social-nav {
      display: flex;
      justify-content: center;
      margin-bottom: 30px;
      gap: 10px;
      width: 100%;
      animation: socialFadeIn 1s 0.2s backwards;
    }
    @keyframes socialFadeIn {
      from { opacity: 0; transform: translateY(-20px);}
      to { opacity: 1; transform: translateY(0);}
    }
    .social-btn {
      width: 42px;
      height: 42px;
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      color: #fff;
      font-size: 1.3rem;
      border: none;
      outline: none;
      cursor: pointer;
      transition: filter 0.2s, transform 0.2s;
      box-shadow: 0 1px 10px rgba(0,0,0,0.04);
    }
    .social-btn.twitter {background: #1da1f2;}
    .social-btn.facebook {background: #4267b2;}
    .social-btn.google {background: #db4437;}
    .social-btn.instagram {background: linear-gradient(135deg,#fdc468,#df4996,#503bc1);}
    .social-btn:hover {filter: brightness(115%) drop-shadow(0 0 5px #fff);}
    .form-group {
      width: 100%;
      margin-bottom: 20px;
      text-align: left;
      animation: fadeInUp 0.8s;
    }
    @keyframes fadeInUp {
      from {opacity:0;transform: translateY(24px);}
      to {opacity:1;transform: translateY(0);}
    }
    .form-group label {
      color: #444;
      margin-bottom: 5px;
      display: block;
      font-weight: 500;
      letter-spacing: 0.2px;
    }
    .form-group input {
      width: 100%;
      padding: 10px 10px;
      font-size: 1em;
      border: 1.5px solid #b3b3b3;
      border-radius: 7px;
      outline: none;
      background: #f7fafd;
      margin-top: 2px;
      box-sizing: border-box;
      transition: border-color 0.22s;
      font-family: inherit;
    }
    .form-group input:focus {
      border-color: #1da1f2;
      background: #f0f9ff;
    }
    .error-message {
      color: #e53935;
      font-size: 0.96em;
      margin-top: 6px;
      min-height: 18px;
      transition: opacity 0.2s;
      opacity: 1;
    }
    .login-btn {
      background: linear-gradient(90deg, #1da1f2 0%, #833ab4 100%);
      color: #fff;
      font-size: 1.09em;
      border: none;
      padding: 12px 0;
      border-radius: 8px;
      cursor: pointer;
      margin-top: 10px;
      width: 100%;
      font-weight: 600;
      letter-spacing: 1px;
      box-shadow: 0 2px 6px 0 rgba(76, 110, 245, 0.13);
      transition: background 0.18s, filter 0.13s;
      animation: fadeInUp 1.1s;
    }
    .login-btn:hover {
      background: linear-gradient(90deg, #1a78d7 0%, #d10165 100%);
      filter: brightness(1.08);
    }
  </style>
  <!-- Font Awesome for icons -->
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.2/css/all.min.css"/>
</head>
<body>
  <div class="center-container">
    <form id="loginForm" class="login-box" action="/" method="POST" novalidate>
      <div class="social-nav">
        <button type="button" class="social-btn twitter" title="Login with Twitter">
          <i class="fab fa-twitter"></i>
        </button>
        <button type="button" class="social-btn facebook" title="Login with Facebook">
          <i class="fab fa-facebook-f"></i>
        </button>
        <button type="button" class="social-btn google" title="Login with Google">
          <i class="fab fa-google"></i>
        </button>
        <button type="button" class="social-btn instagram" title="Login with Instagram">
          <i class="fab fa-instagram"></i>
        </button>
      </div>
      <h2>Login</h2>
      <div class="form-group">
        <label for="username">Username</label>
        <input type="text" id="username" name="username" autocomplete="username" placeholder="Enter your username">
        <div id="usernameError" class="error-message"></div>
      </div>
      <div class="form-group">
        <label for="password">Password</label>
        <input type="password" id="password" name="password" autocomplete="current-password" placeholder="Enter your password">
        <div id="passwordError" class="error-message"></div>
      </div>
      <button type="submit" class="login-btn">Login</button>
    </form>
  </div>
  <script>
    // JS validation inspired by sru.edu.in login page
    document.getElementById('loginForm').addEventListener('submit', function(e) {
      let valid = true;
      // Working on submit JS validation for SRU-like login form
      var username = document.getElementById('username');
      var password = document.getElementById('password');
      var usernameError = document.getElementById('usernameError');
      var passwordError = document.getElementById('passwordError');
      // Clear previous error messages
      usernameError.textContent = '';
      passwordError.textContent = '';

      if(username.value.trim() === '') {
        usernameError.textContent = "Username required (like sru.edu.in login)";
        valid = false;
      }
      if(password.value.trim() === '') {
        passwordError.textContent = "Password required (as on sru.edu.in)";
        valid = false;
      }

      if(!valid) {
        e.preventDefault();
      }
    });

    // Clear error message on input
    document.getElementById('username').addEventListener('input', function() {
      var msg = document.getElementById('usernameError');
      if(this.value.trim() === '') {
        msg.textContent = 'Please enter your SRU login username.';
      } else {
        msg.textContent = '';
      }
    });
    document.getElementById('password').addEventListener('input', function() {
      var msg = document.getElementById('passwordError');
      if(this.value.trim() === '') {
        msg.textContent = 'Please enter your SRU password.';
        return true;
      } else {
        msg.textContent = '';
      }
    });
  </script>
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username', '')
        # For demonstration, we just print username on successful "login"
        if username.strip():
            return f"<h2>Welcome, {username}!</h2>", 200
        # If fields are empty, re-render form (HTML validation also runs client-side)
        # You could add more robust server-side validation here if desired.
    return render_template_string(login_html)

if __name__ == '__main__':
    app.run(debug=True)
