# Akhilesh Singh - Professional Portfolio

A dual-focused Streamlit portfolio showcasing DevOps engineering expertise alongside passion for poetry writing and listening.

## 🚀 Features

- **Professional Overview**: Career highlights with interactive metrics
- **Technical Journey**: Interactive timeline with detailed work experience
- **Skills Visualization**: Charts and proficiency levels across multiple categories
- **Poetry Section**: Creative content with favorite quotes and reflections
- **AI Assistant**: Smart search and Q&A for instant information retrieval
- **Admin Panel**: Content management system for easy updates
- **Contact Information**: Professional links and contact details

## 📋 Prerequisites

- Python 3.11 or higher
- pip or uv package manager

## 🛠️ Local Setup

### Quick Setup (Recommended)

#### Option 1: Automated Setup Script
```bash
# Clone repository
git clone <repository-url>
cd portfolio-website

# Run setup script
python setup.py
```

#### Option 2: Interactive Deployment Script
```bash
# Make script executable
chmod +x deploy.sh

# Run interactive setup
./deploy.sh

# Or use specific commands
./deploy.sh install    # Install dependencies
./deploy.sh both       # Start both applications
./deploy.sh portfolio  # Start portfolio only
./deploy.sh admin      # Start admin panel only
```

### Manual Setup

#### 1. Clone the Repository
```bash
git clone <repository-url>
cd portfolio-website
```

#### 2. Install Dependencies
```bash
# Using pip
pip install streamlit pandas plotly

# Check installation
python -c "import streamlit, pandas, plotly; print('All packages installed successfully')"
```

#### 3. Run the Applications

##### Main Portfolio
```bash
streamlit run app.py --server.port 5000
```
Visit: http://localhost:5000

##### Admin Panel
```bash
streamlit run admin.py --server.port 5001
```
Visit: http://localhost:5001
- Password: `admin123`

##### Run Both Applications
```bash
# In separate terminals
streamlit run app.py --server.port 5000 &
streamlit run admin.py --server.port 5001 &
```

## 🌐 Global Deployment

### Streamlit Cloud (Recommended)

1. **Prepare Repository**
   - Push code to GitHub repository
   - Ensure `requirements.txt` exists with dependencies

2. **Deploy to Streamlit Cloud**
   - Go to [share.streamlit.io](https://share.streamlit.io)
   - Connect your GitHub account
   - Select repository and branch
   - Set main file path: `app.py`
   - Deploy

3. **Admin Panel Deployment**
   - Create separate app for admin panel
   - Set main file path: `admin.py`
   - Deploy to different subdomain

### Alternative Deployment Options

#### Heroku
```bash
# Create Procfile
echo "web: streamlit run app.py --server.port=\$PORT --server.address=0.0.0.0" > Procfile

# Deploy
heroku create your-portfolio-app
git push heroku main
```

#### Railway
```bash
# Install Railway CLI
npm install -g @railway/cli

# Deploy
railway login
railway init
railway up
```

#### Docker

##### Single Container
```bash
# Build and run
docker build -t akhilesh-portfolio .
docker run -p 8501:8501 akhilesh-portfolio
```

##### Multi-Container with Docker Compose
```bash
# Start both portfolio and admin panel
docker-compose up -d

# Access applications
# Portfolio: http://localhost:8501
# Admin Panel: http://localhost:8502
```

##### Docker Commands
```bash
# Build image
docker build -t portfolio-app .

# Run portfolio only
docker run -p 5000:8501 portfolio-app

# Run with volume for data persistence
docker run -p 5000:8501 -v $(pwd)/data:/app/data portfolio-app

# Stop containers
docker-compose down
```

## 📁 Project Structure

```
portfolio-website/
├── app.py                 # Main portfolio application
├── admin.py              # Admin panel for content management
├── requirements.txt      # Python dependencies
├── .streamlit/
│   └── config.toml       # Streamlit configuration
├── components/           # Reusable UI components
│   ├── career_timeline.py
│   ├── contact_info.py
│   ├── poetry_section.py
│   └── skills_visualization.py
├── data/                 # Portfolio data modules
│   ├── work_experience.py
│   ├── skills_data.py
│   ├── poetry_content.py
│   └── certifications.py
└── README.md
```

## 🔧 Configuration

### Streamlit Configuration
Located in `.streamlit/config.toml`:
```toml
[server]
headless = true
address = "0.0.0.0"
port = 5000

[theme]
base = "light"
```

### Environment Variables (Optional)
```bash
# For production deployment
STREAMLIT_SERVER_PORT=5000
STREAMLIT_SERVER_ADDRESS=0.0.0.0
```

## 📝 Content Management

### Using Admin Panel
1. Access admin panel at port 5001
2. Login with password: `admin123`
3. Navigate through tabs to manage:
   - Work Experience
   - Skills & Certifications
   - Poetry Content
   - Data Backup

### Manual Content Updates
Edit files in `data/` directory:
- `work_experience.py` - Career history
- `skills_data.py` - Technical skills and certifications
- `poetry_content.py` - Poetry quotes and content

After manual edits, restart the application.

## 🤖 AI Assistant Features

The AI Assistant provides:
- **Smart Q&A**: Natural language queries about experience and skills
- **Skills Search**: Find specific technologies and proficiency levels
- **Experience Search**: Search through job descriptions and responsibilities
- **Quick Facts**: Instant metrics and statistics

Example queries:
- "What is Akhilesh's current role?"
- "What cloud platforms does he work with?"
- "Tell me about his DevOps skills"
- "How can I contact him?"

## 🔐 Security

### Admin Panel Security
- Change default password in `admin.py`
- For production, implement proper authentication
- Consider environment variables for sensitive data

### Deployment Security
- Use HTTPS in production
- Set proper CORS headers
- Implement rate limiting if needed

## 🚀 Performance Optimization

### Local Development
- Use `streamlit run` with `--server.runOnSave=true` for auto-reload
- Enable caching for data loading functions

### Production
- Implement Streamlit caching decorators
- Optimize image assets
- Use CDN for static resources

## 🐛 Troubleshooting

### Common Issues

**Port Already in Use**
```bash
# Kill process on port 5000
lsof -ti:5000 | xargs kill -9

# Or use different port
streamlit run app.py --server.port 5001
```

**Module Import Errors**
```bash
# Ensure all dependencies are installed
pip install -r requirements.txt

# Check Python path
python -c "import streamlit; print('Success')"
```

**Deployment Issues**
- Ensure `requirements.txt` includes all dependencies
- Check Python version compatibility
- Verify file paths are relative

### Logs and Debugging
- Check Streamlit logs in terminal
- Use `st.write()` for debugging
- Enable verbose logging in config

## 📊 Analytics and Monitoring

### Built-in Metrics
- Portfolio views and interactions
- AI Assistant query patterns
- Admin panel usage

### External Integration
```python
# Google Analytics (optional)
# Add tracking code to Streamlit app
```

## 🔄 Updates and Maintenance

### Regular Updates
1. Update portfolio data through admin panel
2. Review and refresh skills proficiency levels
3. Add new certifications and experiences
4. Update poetry content and quotes

### Version Control
```bash
# Create feature branch
git checkout -b feature/new-content

# Commit changes
git add .
git commit -m "Update portfolio content"

# Deploy
git push origin main
```

## 📞 Support

For issues or questions:
- Email: akhileshranjan.ks@gmail.com
- Create GitHub issue for technical problems
- Check Streamlit documentation: https://docs.streamlit.io

## 📄 License

This project is open source and available under the MIT License.

## 🏗️ Contributing

1. Fork the repository
2. Create feature branch
3. Make changes
4. Test locally
5. Submit pull request

---

**Built with ❤️ using Streamlit, Python, and Plotly**

*"Where cloud architecture meets creative expression"*