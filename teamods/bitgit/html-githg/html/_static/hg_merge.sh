#!/bin/sh
# Demo script for exemplifying hg merge

rm -rf tmp1 tmp2 tmp_repo   # Clean up previous runs

mkdir tmp_repo   # Global repository for testing
cd tmp_repo
cat > myfile <<EOF
This is a little
test file for
exemplifying merge
of files in different
hg directories.
EOF
hg init   # Make hg global repository out of this directory
hg add    # Add all files not mentioned in ~/.hgignore
hg commit -m 'first commit'
cd ..

# Make a new hg repositories tmp1 and tmp2 (two users)
hg clone tmp_repo tmp1
hg clone tmp_repo tmp2

# Change myfile in the directory tmp1
cd tmp1
# Edit myfile: insert a new second line
perl -pi -e 's/a little\n/a little\ntmp1-add1\n/g' myfile
# Register change in local repository
hg commit -m 'Inserted a new second line in myfile.'
# Look at changes in this clone
hg log -p
# Register change in global repository tmp_repo
hg push
cd ..

# Change myfile in the directory tmp2 "in parallel"
cd tmp2
# Edit myfile: add a line at the end
cat >> myfile <<EOF
tmp2-add1
EOF
# Register change locally
hg commit -m 'Added a new line at the end'
# Register change globally
hg push
# Error message: global repository has changed,
# we need to pull those changes to local repository first
# and see if all files are compatible before we can update
# our own changes to the global repository.
# hg writes
# abort: push creates new remote head d0a2f8e6b9d9!
# (you should pull and merge or use push -f to force)

hg pull
# hg writes:
# added 1 changesets with 1 changes to 1 files (+1 heads)
# (run 'hg heads' to see heads, 'hg merge' to merge)
hg merge
# Successful merge!
cat myfile
hg commit -m merge
hg push
cd ..

# Perform new changes in parallel in tmp1 and tmp2,
# this time causing hg merge to fail

# Change myfile in the directory tmp1
cd tmp1
# Do it all right by pulling and updating first
hg pull
hg update
# Edit myfile: insert "just" in first line.
perl -pi -e 's/a little/tmp1-add2 a little/g' myfile
# Register change in local repository
hg commit -m 'Inserted "just" in first line.'
# Register change in global repository tmp_repo
hg push
cd ..

# Change myfile in the directory tmp2 "in parallel"
cd tmp2
# Edit myfile: replace little by modest
perl -pi -e 's/a little/a tmp2-replace1\ntmp2-add2\n/g' myfile
# Register change locally
hg commit -m 'Replaced "little" by "modest"'
# Register change globally
hg push
# Not possible: need to pull changes in the global repository
hg pull
hg update
# hg update aborts: we have to run hg merge
diff myfile ../tmp_repo/myfile
echo 'Now you must do hg merge manually'



