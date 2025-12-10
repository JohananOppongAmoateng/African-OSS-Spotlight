# African OSS Spotlight

An open-source platform to discover and amplify open-source creators and projects from Africa.

## 🌍 About

African OSS Spotlight is a community-driven platform that highlights and documents Africa's active open-source creators and the projects they build. The goal is to increase visibility for African developers doing outstanding open-source work and make it easier for people to discover, support, collaborate with, or hire them.

## ✨ Features

- **Creator Profiles**: Showcase African open-source developers with detailed profiles
- **Project Showcase**: Highlight open-source projects built by African creators
- **Admin Verification**: All submissions go through admin review before being published
- **Responsive Design**: Beautiful, modern UI built with Tailwind CSS
- **Easy Submissions**: Simple forms for nominating creators and submitting projects

## 🚀 Getting Started

### Prerequisites

- Python 3.11 or higher
- Node.js and npm (for Tailwind CSS)
- SQLite (default) or PostgreSQL (for production)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/African-OSS-Spotlight.git
   cd African-OSS-Spotlight
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv .venv
   # On Windows
   .venv\Scripts\activate
   # On macOS/Linux
   source .venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser (admin account)**
   ```bash
   python manage.py createsuperuser
   ```

6. **Install and build Tailwind CSS**
   ```bash
   python manage.py tailwind install
   python manage.py tailwind build
   ```

7. **Run the development server**
   ```bash
   python manage.py runserver
   ```

8. **In a separate terminal, run Tailwind in watch mode (for development)**
   ```bash
   python manage.py tailwind start
   ```

9. **Access the application**
   - Main site: http://localhost:8000
   - Admin panel: http://localhost:8000/admin

## 📝 Usage

### For Community Members

1. **Nominate a Creator**: Visit `/creators/submit/` to nominate an African open-source creator
2. **Submit a Project**: Visit `/projects/submit/` to add a project to an existing creator's profile
3. **Explore**: Browse verified creators and projects on the explore pages

### For Administrators

1. Log in to the admin panel at `/admin/`
2. Review pending submissions under "Creators" and "Projects"
3. Use bulk actions to verify or reject multiple submissions at once
4. Verified items will automatically appear on the public explore pages

## 🛠️ Production Deployment

### Environment Variables

Create a `.env` file based on `.env.example`:

```bash
SECRET_KEY=your-secret-key-here
DEBUG=False
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
```

### Static Files

```bash
python manage.py collectstatic --noinput
```

### Database

For production, consider using PostgreSQL instead of SQLite. Update your settings accordingly.

### Web Server

Use a production WSGI server like Gunicorn:

```bash
gunicorn african_oss_spotlight.wsgi:application --bind 0.0.0.0:8000
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- All the amazing African open-source creators who inspire this project
- The Django and Tailwind CSS communities
- Contributors and supporters of this initiative

## 📧 Contact

For questions or suggestions, please open an issue on GitHub.

---

**Made with ❤️ for the African open-source community**
