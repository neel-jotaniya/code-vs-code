# Git Rebase Challenge

This is a simple challenge to test your understanding of Git rebase. The project is a basic calculator with two features that need to be combined using rebase.

## Current Structure
- `main` branch: Contains basic calculator with addition feature
- `feature-subtraction` branch: Adds subtraction functionality
- `feature-multiplication` branch: Adds multiplication functionality

## Challenge
Your task is to:
1. Create two new branches from main:
   - `feature-subtraction`
   - `feature-multiplication`
2. Add the respective features in each branch
3. Use `git rebase` to bring both features onto the main branch
4. The final result should have a clean, linear history

## Expected Result
After completing the challenge, running `git log` should show something like:
```
commit 3: feat: add multiplication
commit 2: feat: add subtraction
commit 1: feat: initial calculator with addition
```

## Tips
- Use `git rebase` to move commits
- Resolve any conflicts that arise during rebase
- Keep your commit messages clear and descriptive
- Make sure to test the calculator after each change

## How to Start
1. Clone this repository
2. Create the feature branches
3. Implement the features
4. Use rebase to combine them
5. Push your solution to your own repository