"""
Create a GitHub Repository
Go to GitHub and create a new repository. Name it my-first-repo or something that tickles your fancy.
Clone the Repo
Open your terminal and clone your newly minted repository to your local machine.
Navigate and Initial Commit
Navigate into the directory of the repo.

--mkdir hillil_study
--cd hillil_study
--git init
--git clone https://github.com/Sur619/hillil_study.git

Create a text file named story.txt and write a sentence in it.
Stage and commit this change.
--echo "i'm really pleased that i have an  opportunity to study here!"
--git add story.txt
--git commit -m "add new file story.txt"

Create Branches
Create two new branches feature1 and feature2 from the main branch.
Simulate Conflict
In each of the branches, open story.txt and add a different second sentence.
Commit these changes in both branches.
--git checkout -b feature1
--echo "This is the second sentence for feature1." >> story.txt
--git add story.txt
--git commit -m "Add second sentence in feature1 branch."


--git switch -b feature2
--echo "This is the second sentence for feature2." >> story.txt
--git add story.txt
--git commit -m "add new sentence story.txt on branch feature2"

Merge feature1 into main
Go back to the main branch and merge feature1.
--git checkout master
--git merge feature1



Merge feature2 into main and Resolve Conflict
Now try merging feature2 into main.
Oh no! A wild conflict appears! 😱
Open story.txt and resolve the conflict manually. Save the file.
Commit the changes.
--git merge feature2
--git add story.txt
--git merge --continue
--git commit -m "Merge feature2 into main with conflict resolution"

Push to GitHub
Push all these changes back to your GitHub repo.
Share the Repo
--git remote add origin https://github.com/Sur619/hillil_study.git
--git branch -M feature2
--git push -u origin feature2

--sharing this with you - https://github.com/Sur619/hillil_study.git

Share the GitHub repository link with me (your tutor).

Submit on Hillel LMS
Finally, submit your GitHub repo link through the Hillel Learning Management System for review.
"""