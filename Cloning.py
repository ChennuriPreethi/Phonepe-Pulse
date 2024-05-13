import git

repository_url = "https://github.com/PhonePe/pulse.git"
dest_dir = "E:/Preethi/GUVI Projects/2 - Project - PhonePe Pulse/pulse"
git.Repo.clone_from(repository_url,dest_dir)