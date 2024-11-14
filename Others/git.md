## Git Commands

```bash
git add .
git commit -m "my first commit"
git reflog
git reset --soft <hash>
git push <remote_name> master:master
git pull --rebase <remote_name> master:master
git branch -a         # Show all branches
git branch -r         # Show remote branches
git branch <new_branch_name>
git branch -d <deleted_branch>
git branch -m <old_name> <new_name>
```

### LFS (Large File Storage)

### Initialize Git LFS

```bash
git lfs install
```

> Run this command once per user account to install Git LFS.
### Check LFS Files

```bash
git lfs ls-files
```

> This command lists all files tracked by LFS.

### LFS Error
- LFS: Remote Error GH001

TIF files should be added to LFS. To do this:

1. Run `git lfs install` in your main repository.
2. Use `git lfs track "*.tif"` to track TIF files.
3. Do not forget to commit the changes before pushing.

- LFS: Remote Error GH001 (Handling Large Files >100MB)

1. If you have committed large files (>100MB) that are not labeled for LFS, the commit will fail even if you track them later.

2. To fix this, run:

    ```bash
    git lfs migrate import --include="*.tif" --everything
    git reflog expire --expire=now --all
    git gc --prune=now --aggressive
    ```

3. Anything tracked by Git but not by LFS will not be treated as LFS, even after updating `.gitattributes`. To fix this:

   1. Use the migration method above, or
   2. Remove the `.git` directory and create a new repository:  
        ```bash
        Remove-Item -Recurse -Force .\.git\
        ```






## SSH Key Generation

```bash
ssh-keygen -f ~/.ssh/github -t ed25519 -C "for github"
eval $(ssh-agent -s)           # Activate ssh-agent
ssh-add ~/.ssh/github          # Add private key to ssh-agent
```


## gitignore
exclude folder but include specific subfolder

```
# Ignore everything in build/ except logs/
!build/
build/*
!build/logs/
```