#!/bin/bash

# Akhilesh Singh Portfolio - Deployment Script
# This script helps with local setup and deployment

set -e

echo "🚀 Akhilesh Singh Portfolio Setup & Deployment"
echo "=============================================="

# Function to check if command exists
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# Check Python installation
if command_exists python3; then
    PYTHON_CMD="python3"
elif command_exists python; then
    PYTHON_CMD="python"
else
    echo "❌ Python is not installed. Please install Python 3.11 or higher."
    exit 1
fi

echo "✅ Python found: $($PYTHON_CMD --version)"

# Check Streamlit installation
if ! $PYTHON_CMD -c "import streamlit" >/dev/null 2>&1; then
    echo "📦 Installing Streamlit and dependencies..."
    $PYTHON_CMD -m pip install streamlit pandas plotly
else
    echo "✅ Streamlit is already installed"
fi

# Function to start portfolio
start_portfolio() {
    echo "🌟 Starting Portfolio Application..."
    echo "Portfolio will be available at: http://localhost:5000"
    streamlit run app.py --server.port 5000
}

# Function to start admin panel
start_admin() {
    echo "⚙️ Starting Admin Panel..."
    echo "Admin panel will be available at: http://localhost:5001"
    echo "Login password: admin123"
    streamlit run admin.py --server.port 5001
}

# Function to start both applications
start_both() {
    echo "🔄 Starting both Portfolio and Admin Panel..."
    
    # Start portfolio in background
    echo "Starting portfolio on port 5000..."
    streamlit run app.py --server.port 5000 &
    PORTFOLIO_PID=$!
    
    # Wait a moment
    sleep 3
    
    # Start admin panel in background
    echo "Starting admin panel on port 5001..."
    streamlit run admin.py --server.port 5001 &
    ADMIN_PID=$!
    
    echo "✅ Both applications started!"
    echo "Portfolio: http://localhost:5000"
    echo "Admin Panel: http://localhost:5001 (password: admin123)"
    echo ""
    echo "Press Ctrl+C to stop both applications"
    
    # Wait for user to stop
    trap "echo 'Stopping applications...'; kill $PORTFOLIO_PID $ADMIN_PID 2>/dev/null; exit" INT
    wait
}

# Function to check for updates
check_dependencies() {
    echo "🔍 Checking dependencies..."
    
    # Check if all required packages are installed
    REQUIRED_PACKAGES=("streamlit" "pandas" "plotly")
    
    for package in "${REQUIRED_PACKAGES[@]}"; do
        if $PYTHON_CMD -c "import $package" >/dev/null 2>&1; then
            echo "✅ $package is installed"
        else
            echo "❌ $package is missing"
            echo "Installing $package..."
            $PYTHON_CMD -m pip install $package
        fi
    done
    
    echo "✅ All dependencies are ready!"
}

# Function to create production requirements
create_requirements() {
    echo "📝 Creating requirements.txt for deployment..."
    cat > requirements_deploy.txt << EOF
streamlit>=1.28.0
pandas>=1.5.0
plotly>=5.15.0
EOF
    echo "✅ requirements_deploy.txt created for deployment"
}

# Function to show deployment instructions
show_deployment_info() {
    echo ""
    echo "🌐 DEPLOYMENT OPTIONS"
    echo "===================="
    echo ""
    echo "1. Streamlit Cloud (Recommended):"
    echo "   - Push code to GitHub"
    echo "   - Go to share.streamlit.io"
    echo "   - Connect repository and deploy"
    echo ""
    echo "2. Heroku:"
    echo "   - Create Procfile: web: streamlit run app.py --server.port=\$PORT --server.address=0.0.0.0"
    echo "   - heroku create your-app-name"
    echo "   - git push heroku main"
    echo ""
    echo "3. Railway:"
    echo "   - railway login"
    echo "   - railway init"
    echo "   - railway up"
    echo ""
    echo "4. Docker:"
    echo "   - docker build -t portfolio ."
    echo "   - docker run -p 8501:8501 portfolio"
    echo ""
}

# Function to backup data
backup_data() {
    echo "💾 Creating data backup..."
    BACKUP_DIR="backup_$(date +%Y%m%d_%H%M%S)"
    mkdir -p "$BACKUP_DIR"
    
    cp -r data/ "$BACKUP_DIR/"
    cp app.py "$BACKUP_DIR/"
    cp admin.py "$BACKUP_DIR/"
    
    echo "✅ Backup created in $BACKUP_DIR"
}

# Main menu
show_menu() {
    echo ""
    echo "📋 SETUP OPTIONS"
    echo "==============="
    echo "1. Check dependencies"
    echo "2. Start portfolio only"
    echo "3. Start admin panel only"
    echo "4. Start both applications"
    echo "5. Create deployment requirements"
    echo "6. Show deployment instructions"
    echo "7. Backup data"
    echo "8. Exit"
    echo ""
}

# Main execution
main() {
    while true; do
        show_menu
        read -p "Choose an option (1-8): " choice
        
        case $choice in
            1)
                check_dependencies
                ;;
            2)
                start_portfolio
                ;;
            3)
                start_admin
                ;;
            4)
                start_both
                ;;
            5)
                create_requirements
                ;;
            6)
                show_deployment_info
                ;;
            7)
                backup_data
                ;;
            8)
                echo "👋 Goodbye!"
                exit 0
                ;;
            *)
                echo "❌ Invalid option. Please choose 1-8."
                ;;
        esac
        
        echo ""
        read -p "Press Enter to continue..."
    done
}

# Check if script is run with arguments
if [ $# -eq 0 ]; then
    main
else
    case $1 in
        "install")
            check_dependencies
            ;;
        "portfolio")
            start_portfolio
            ;;
        "admin")
            start_admin
            ;;
        "both")
            start_both
            ;;
        "deploy")
            show_deployment_info
            ;;
        "backup")
            backup_data
            ;;
        *)
            echo "Usage: $0 [install|portfolio|admin|both|deploy|backup]"
            exit 1
            ;;
    esac
fi