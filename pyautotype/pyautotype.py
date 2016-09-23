# Copyright (c) 2016 Caitlin Campbell
#
# pyautotype is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

import pyautogui
from time import sleep
import sys
import random
import os
import click

def main():
    type()


@click.command()
@click.option('--time', default=1, type=int, help='Number of seconds till typing starts Default: 5.')
@click.option('--file', type=click.Path(exists=True), help='The file to type out.')
@click.option('--mode', default='humanlike',
              type=click.Choice(['humanlike', 'fast']),
              help='How the program types out the file. Default: humanlike')
def type(time, file, mode):
    os.chdir(os.getcwd())
    if file is None:
        click.echo('Error: Missing "--file" argument.')
        return

    for i in range(time):
        click.echo('Typing begins in %s seconds press Ctrl-C to abort' % (time - i))
        sleep(1)

    file = open(file, "r")
    for line in file.readlines():
        for char in line:
            if mode == 'fast':
                char_time = 0.00000000000001
            if mode == 'humanlike':
                char_time = 0.00000000000001 + random.uniform(0.03,0.05)

            pyautogui.typewrite(char, interval=char_time)

if __name__ == '__main__':
    type()

