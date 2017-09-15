#!/usr/bin/evn python3

import sys
import os
import subprocess
import random
import shutil
import uuid


def usage():
  print('Usage: select_samples.py root_dir size_limit remove_upx num_train_samples train_folder num_test_samples test_folder rename')


def main():
  if len(sys.argv) != 9:
    usage()
    sys.exit(-1)

  rootdir = sys.argv[1]
  file_size_limit = int(sys.argv[2])
  remove_upx = bool(sys.argv[3])
  num_train_samples = int(sys.argv[4])
  train_folder = sys.argv[5]
  num_test_samples = int(sys.argv[6])
  test_folder = sys.argv[7]
  should_rename = bool(sys.argv[8])
  
  file_pool = []

  for subdir, dirs, files in os.walk(rootdir):
    for f in files:
      file_path = os.path.join(subdir, f)
      file_size = os.stat(file_path).st_size 
      output = subprocess.check_output(["file", file_path]).decode('utf-8', 'ignore')
      if 'PE' in output and file_size < file_size_limit:
        if remove_upx and 'UPX' not in output:
          file_pool.append(file_path)
        elif not remove_upx:
          file_pool.append(file_path)

  if should_rename:
    train_log = open('train_samples.log', 'w')
    test_log = open('test_samples.log', 'w')
  
  selected_samples = set()
  while len(selected_samples) < num_train_samples:
    idx = random.randint(0, len(file_pool) - 1)
    selected_samples.add(file_pool[idx])
    file_pool.remove(file_pool[idx])

  for sample in selected_samples:
    filename = os.path.basename(sample)
    if should_rename:
      uuid_filename = str(uuid.uuid4())
      shutil.copy(sample, os.path.join(train_folder, uuid_filename))
      train_log.write('"{}" "{}"\n'.format(sample, uuid_filename))
    else:
      shutil.copy(sample, train_folder)

  selected_samples = set()
  while len(selected_samples) < num_train_samples:
    idx = random.randint(0, len(file_pool) - 1)
    selected_samples.add(file_pool[idx])
    file_pool.remove(file_pool[idx])

  for sample in selected_samples:
    filename = os.path.basename(sample)
    if should_rename:
      uuid_filename = str(uuid.uuid4())
      shutil.copy(sample, os.path.join(test_folder, uuid_filename))
      test_log.write('"{}" "{}"\n'.format(sample, uuid_filename))
    else:
      shutil.copy(sample, test_folder)

  if should_rename:
    train_log.close()
    test_log.close()


if __name__ == '__main__':
  main()
