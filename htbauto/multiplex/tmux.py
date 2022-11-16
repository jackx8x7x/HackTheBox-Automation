#!/usr/bin/env python

import os, sys, shlex
import subprocess
import logging

logging.basicConfig(level=logging.DEBUG)

def _exec(cmd, *argv, **kwargs):
    args = shlex.split(cmd)
    return subprocess.run(args, *argv, **kwargs)

class Tmux:
    def __init__(self, name, *args, **kwargs):
        self.name = name
        self.logger = logging.getLogger(__name__)
        tmux_cmd = "tmux new-session -P -F '#{pane_id}'" + f" -d -s {self.name}"

        self.pane_id = _exec(tmux_cmd, capture_output=True).stdout.decode()

    def attach(self):
        os.system(f'tmux attach -t {self.name}')

    def new_window(self, cmd=''):
        cmd = "tmux new-window -P -F '#{pane_id}'" + f" -t {self.name}: -d {cmd}"
        pane_id =  _exec(cmd, capture_output=True).stdout.decode().strip()
        self.logger.debug(cmd)
        self.logger.debug(f"create new tmux window with pane_id {pane_id}")
        return pane_id

    def split_window(self, target_id=None, cmd='', vertical=True):
        flag = '-v' if vertical else '-h'
        target_id = target_id if target_id else self.pane_id

        split_cmd = "tmux split-window -P -F '#{pane_id}'" + f" {flag} -t {target_id} -d {cmd}"
        self.logger.info(split_cmd)

        pane_id = _exec(split_cmd, capture_output=True).stdout.decode().strip()
        return pane_id

    def quit(self):
        print('kill')
        _exec(f"tmux kill-session -t {self.name}")

if __name__ == '__main__':
    t = Tmux('HackTheBox-Automation')
    bottom = t.split_window()
    right = t.split_window(vertical=False)
    right_bottom = t.split_window(bottom, vertical=False)
    t.new_window()
