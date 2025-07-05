#!/usr/bin/env python3
"""
Setup script for Akhilesh Singh Portfolio
Quick installation and configuration
"""

import subprocess
import sys
import os
from pathlib import Path

def run_command(command, description):
    """Run a command and handle errors"""
    print(f"📦 {description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} completed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed: {e.stderr}")
        return False

def check_python():
    """Check Python version"""
    version = sys.version_info
    if version.major == 3 and version.minor >= 8:
        print(f"✅ Python {version.major}.{version.minor}.{version.micro} is compatible")
        return True
    else:
        print(f"❌ Python {version.major}.{version.minor}.{version.micro} is too old. Need Python 3.8+")
        return False

def install_dependencies():
    """Install required packages"""
    packages = ["streamlit", "pandas", "plotly"]
    
    for package in packages:
        if not run_command(f"{sys.executable} -m pip install {package}", f"Installing {package}"):
            return False
    
    return True

def create_config():
    """Create Streamlit configuration if it doesn't exist"""
    config_dir = Path(".streamlit")
    config_file = config_dir / "config.toml"
    
    if not config_dir.exists():
        config_dir.mkdir()
    
    if not config_file.exists():
        config_content = """[server]
headless = true
address = "0.0.0.0"
port = 5000

[theme]
base = "light"
"""
        with open(config_file, 'w') as f:
            f.write(config_content)
        print("✅ Created Streamlit configuration")
    else:
        print("✅ Streamlit configuration already exists")

def test_installation():
    """Test if everything is working"""
    try:
        import streamlit
        import pandas
        import plotly
        print("✅ All packages imported successfully")
        return True
    except ImportError as e:
        print(f"❌ Import error: {e}")
        return False

def main():
    """Main setup function"""
    print("🚀 Akhilesh Singh Portfolio - Setup Script")
    print("=" * 50)
    
    # Check Python version
    if not check_python():
        sys.exit(1)
    
    # Install dependencies
    if not install_dependencies():
        print("❌ Failed to install dependencies")
        sys.exit(1)
    
    # Create configuration
    create_config()
    
    # Test installation
    if not test_installation():
        print("❌ Installation test failed")
        sys.exit(1)
    
    print("\n🎉 Setup completed successfully!")
    print("\n📋 Next steps:")
    print("1. Start portfolio: python -m streamlit run app.py --server.port 5000")
    print("2. Start admin panel: python -m streamlit run admin.py --server.port 5001")
    print("3. Or use deployment script: ./deploy.sh")
    print("\n🌐 Access URLs:")
    print("- Portfolio: http://localhost:5000")
    print("- Admin Panel: http://localhost:5001 (password: admin123)")

if __name__ == "__main__":
    main()