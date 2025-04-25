# Git Rebase Challenge

This is a simple challenge to test your understanding of Git rebase and pull requests. The project is a basic calculator with two features that need to be combined using rebase.

## Current Structure
- `main` branch: Contains basic calculator with addition feature
- `feature-subtraction` branch: Adds subtraction functionality
- `feature-multiplication` branch: Adds multiplication functionality

## Challenge
Your task is to:
1. Fork this repository to your GitHub account
2. Clone your forked repository
3. Create two new branches from main:
   - `feature-subtraction`
   - `feature-multiplication`
4. Add the respective features in each branch
5. Create pull requests for both feature branches to main
6. Use `git rebase` to bring both features onto the main branch
7. The final result should have a clean, linear history

## Expected Result
After completing the challenge, running `git log` should show something like:
```
commit 3: feat: add multiplication
commit 2: feat: add subtraction
commit 1: feat: initial calculator with addition
```

## Detailed Steps
1. Fork the Repository:
   - Click the "Fork" button on the top right of this repository
   - Clone your forked repository: `git clone https://github.com/YOUR_USERNAME/git-rebase-challenge.git`

2. Create Feature Branches:
   ```bash
   git checkout main
   git checkout -b feature-subtraction
   # Implement subtraction feature
   git add .
   git commit -m "feat: add subtraction"

   git checkout main
   git checkout -b feature-multiplication
   # Implement multiplication feature
   git add .
   git commit -m "feat: add multiplication"
   ```

3. Create Pull Requests:
   - Push both feature branches to your fork
   - Create a PR from `feature-subtraction` to `main`
   - Create a PR from `feature-multiplication` to `main`
   - In the PR description, explain your changes and how you used rebase

4. Rebase and Merge:
   - Use `git rebase` to combine the features
   - Resolve any conflicts
   - Update your PRs with the rebased changes

## Tips
- Use `git rebase` to move commits
- Resolve any conflicts that arise during rebase
- Keep your commit messages clear and descriptive
- Make sure to test the calculator after each change
- Keep your PRs up to date with the main branch

## How to Start
1. Fork this repository
2. Clone your fork
3. Create the feature branches
4. Implement the features
5. Create pull requests
6. Use rebase to combine them
7. Update your PRs with the final changes