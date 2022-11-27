tmux new-session -d -s tasks; tmux send 'vim class/';
tmux split-window -h 'vim readme.tex';
tmux split-window; tmux send 'git status' ENTER;
tmux select-pane -t 0;
echo "tmux attach -t tasks"
