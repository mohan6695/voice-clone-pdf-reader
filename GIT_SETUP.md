# Git Configuration for Future Projects

## ✅ Current Setup

Your Git is configured with:
- **Username:** mohan6695
- **Email:** mohan6695@users.noreply.github.com
- **Default Branch:** main
- **Credential Helper:** osxkeychain (macOS)

## 🚀 Quick Setup for New Projects

### Method 1: Use the Helper Script (Recommended)
```bash
# In your project directory:
. ~/.git_setup_mohan6695.sh <repo-name>

# Example:
. ~/.git_setup_mohan6695.sh my-new-project
```

### Method 2: Manual Commands
```bash
# Initialize repository
git init

# Add remote (replace repo-name)
git remote add origin https://github.com/mohan6695/repo-name.git

# Set branch to main
git branch -M main

# Create repository on GitHub at: https://github.com/new

# Push
git push -u origin main
```

### Method 3: Quick One-Liner
```bash
git init && git remote add origin https://github.com/mohan6695/REPO_NAME.git && git branch -M main
```

## 📝 Standard Workflow

For any new project:

```bash
# 1. Navigate to project
cd ~/my-new-project

# 2. Initialize git
git init

# 3. Set up GitHub remote
. ~/.git_setup_mohan6695.sh my-new-project

# 4. Create .gitignore
cat > .gitignore << EOF
venv/
__pycache__/
*.pyc
.DS_Store
EOF

# 5. Add and commit
git add .
git commit -m "Initial commit"

# 6. Create repository on GitHub: https://github.com/new

# 7. Push
git push -u origin main
```

## 🔍 Check Current Configuration

```bash
# View all git config
git config --global --list

# Check username
git config --global user.name

# Check email
git config --global user.email
```

## ✏️ Update Configuration

```bash
# Change username globally
git config --global user.name "YourUsername"

# Change email globally
git config --global user.email "your-email@example.com"
```

## 🆘 Troubleshooting

### If push fails due to authentication:
```bash
# Use Personal Access Token
# Create at: https://github.com/settings/tokens
# Select 'repo' scope
# Use token as password when pushing
```

### If you need to update remote URL:
```bash
git remote set-url origin https://github.com/mohan6695/your-repo.git
```

## 📚 Useful Aliases (Optional)

Add these to `~/.zshrc` or `~/.bashrc`:

```bash
# Quick status
alias gs='git status'

# Quick add and commit
alias gac='git add . && git commit -m'

# Quick push
alias gp='git push'

# Setup new repo
alias gsetup='. ~/.git_setup_mohan6695.sh'
```

Then reload: `source ~/.zshrc`

