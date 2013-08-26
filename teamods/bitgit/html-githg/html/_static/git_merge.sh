#!/bin/sh
# Demo script for exemplifying git and merge

rm -rf tmp1 tmp2 tmp_repo   # Clean up previous runs

mkdir tmp_repo   # Global repository for testing
cd tmp_repo
git --bare init --shared
cd ..

# Make a repo that can be pushed to tmp_repo
mkdir _tmp
cd _tmp
cat > myfile <<EOF
This is a little
test file for
exemplifying merge
of files in different
git directories.
EOF
git init
git add .   # Add all files not mentioned in ~/.gitignore
git commit -am 'first commit'
git push ../tmp_repo master
cd ..
rm -rf _tmp

# Make a new hg repositories tmp1 and tmp2 (two users)
git clone tmp_repo tmp1
git clone tmp_repo tmp2
# Change myfile in the directory tmp1
cd tmp1
# Edit myfile: insert a new second line
perl -pi -e 's/a little\n/a little\ntmp1-add1\n/g' myfile
# Register change in local repository
git commit -am 'Inserted a new second line in myfile.'
# Look at changes in this clone
git log -p
# or a more compact summary
git log --stat --summary
# or graphically
#gitk
# Register change in global repository tmp_repo
git push origin master
cd ..

# Change myfile in the directory tmp2 "in parallel"
cd tmp2
# Edit myfile: add a line at the end
cat >> myfile <<EOF
tmp2-add1
EOF
# Register change locally
git commit -am 'Added a new line at the end'
# Register change globally
git push origin master
# Error message: global repository has changed,
# we need to pull those changes to local repository first
# and see if all files are compatible before we can update
# our own changes to the global repository.
# git writes
#To /home/hpl/vc/scripting/manu/py/bitgit/src-bitgit/tmp_repo
# ! [rejected]        master -> master (non-fast-forward)
#error: failed to push some refs to ...

git pull origin master
# git writes:
#Auto-merging myfile
#Merge made by recursive.
# myfile |    1 +
# 1 files changed, 1 insertions(+), 0 deletions(-)
cat myfile  # successful merge!
git commit -am merge
git push origin master
cd ..

# Perform new changes in parallel in tmp1 and tmp2,
# this time causing hg merge to fail

# Change myfile in the directory tmp1
cd tmp1
# Do it all right by pulling and updating first
git pull origin master
# Edit myfile: insert "just" in first line.
perl -pi -e 's/a little/tmp1-add2 a little/g' myfile
# Register change in local repository
git commit -am 'Inserted "just" in first line.'
# Register change in global repository tmp_repo
git push origin master
cd ..

# Change myfile in the directory tmp2 "in parallel"
cd tmp2
# Edit myfile: replace little by modest
perl -pi -e 's/a little/a tmp2-replace1\ntmp2-add2\n/g' myfile
# Register change locally
git commit -am 'Replaced "little" by "modest"'
# Register change globally
git push origin master
# Not possible: need to pull changes in the global repository
git pull origin master
# git writes
#CONFLICT (content): Merge conflict in myfile
#Automatic merge failed; fix conflicts and then commit the result.
# we have to do a manual merge
cat myfile
echo 'Now you must edit myfile manually'



